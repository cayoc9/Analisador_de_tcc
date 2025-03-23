import os
import sys
import argparse
import traceback
import gc
import psutil
from pathlib import Path
from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption

def parse_arguments():
    """Configura e processa argumentos de linha de comando."""
    parser = argparse.ArgumentParser(description='Converter PDFs para Markdown usando Docling')
    parser.add_argument('--input-dir', type=str, default='PDFs',
                        help='Diretório contendo os arquivos PDF (padrão: PDFs)')
    parser.add_argument('--output-dir', type=str, default='MD_',
                        help='Diretório para salvar os arquivos Markdown (padrão: MD_)')
    parser.add_argument('--max-size', type=int, default=30,
                        help='Tamanho máximo do arquivo em MB antes de alertar (padrão: 30MB)')
    parser.add_argument('--min-memory', type=float, default=1.0,
                        help='Quantidade mínima de memória disponível em GB (padrão: 1.0GB)')
    parser.add_argument('--skip-large', action='store_true',
                        help='Pular automaticamente arquivos muito grandes')
    parser.add_argument('--artifacts-path', type=str, default=None,
                        help='Caminho para artefatos de modelo (opcional)')
    return parser.parse_args()

def setup_directories(input_dir, output_dir):
    """Configura os diretórios de entrada e saída, garantindo que existam."""
    PDF_FOLDER = os.path.abspath(input_dir)
    MD_FOLDER = os.path.abspath(output_dir)
    
    if not os.path.exists(PDF_FOLDER):
        print(f"⚠️ Diretório de entrada '{input_dir}' não existe. Criando...")
        os.makedirs(PDF_FOLDER)
        print(f"✅ Diretório criado. Por favor, adicione seus PDFs em: {PDF_FOLDER}")
        return None, None
    
    if not os.path.exists(MD_FOLDER):
        print(f"📁 Criando diretório de saída: {MD_FOLDER}")
        os.makedirs(MD_FOLDER)
    
    return PDF_FOLDER, MD_FOLDER

def check_memory():
    """Verifica a memória disponível no sistema."""
    memory = psutil.virtual_memory()
    memory_gb = memory.available / (1024 * 1024 * 1024)
    print(f"📊 Memória disponível: {memory_gb:.2f} GB")
    return memory_gb

def verificar_pdf(file_path):
    """Verifica se o PDF tem características que podem causar problemas."""
    try:
        # Usando docling para verificar o PDF
        from pypdf import PdfReader
        
        with open(file_path, 'rb') as f:
            try:
                pdf = PdfReader(f)
                if pdf.is_encrypted:
                    return False, "PDF está protegido por senha"
                # Verificar se consegue acessar o conteúdo
                num_paginas = len(pdf.pages)
                print(f"📄 PDF tem {num_paginas} páginas")
                return True, None
            except Exception as e:
                return False, f"Erro ao ler PDF: {str(e)}"
    except ImportError:
        # Se pypdf não estiver disponível, continuamos mesmo assim
        print("⚠️ Biblioteca pypdf não encontrada, pulando verificação detalhada do PDF")
        return True, None
    except Exception as e:
        return False, f"Falha ao verificar PDF: {str(e)}"

def process_single_pdf(pdf_file_name, pdf_folder, md_folder, args, retry_count=0):
    """Processa um único arquivo PDF e converte para Markdown."""
    file_path = os.path.join(pdf_folder, pdf_file_name)
    
    # Verificação do tamanho do arquivo
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # tamanho em MB
    print(f"📄 Tamanho do arquivo: {file_size:.2f} MB")
    
    if file_size > args.max_size:
        print(f"⚠️ Atenção: O arquivo {pdf_file_name} é grande ({file_size:.2f} MB)")
        if args.skip_large:
            print(f"⏭️ Pulando arquivo grande conforme configuração")
            return False, "Arquivo muito grande (pulado pelo usuário)"
    
    # Verificar se o PDF tem problemas conhecidos
    ok, erro = verificar_pdf(file_path)
    if not ok:
        print(f"⚠️ Problema detectado no PDF: {erro}")
        return False, erro
    
    # Verificar memória disponível
    avail_memory = check_memory()
    if avail_memory < args.min_memory + 1.0:  # 1GB a mais para margem de segurança
        print(f"⚠️ Pouca memória disponível ({avail_memory:.2f} GB). Forçando coleta de lixo...")
        gc.collect()  # Forçar coleta de lixo
        avail_memory = check_memory()
        if avail_memory < args.min_memory:
            print("❌ Memória insuficiente para continuar. Pulando este arquivo.")
            return False, "Memória insuficiente"
    
    try:
        # Configurar opções da pipeline
        pipeline_options = PdfPipelineOptions()
        
        # Desativar geração de imagens para economizar memória
        pipeline_options.generate_page_images = False
        
        # Definir caminho para artefatos se fornecido
        if args.artifacts_path:
            pipeline_options.artifacts_path = args.artifacts_path
        
        # Criar o conversor com as opções específicas
        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )
        
        print(f"🔍 Convertendo {pdf_file_name} para Markdown (tentativa {retry_count + 1})")
        result = converter.convert(file_path)
        
        if result and hasattr(result, 'document'):
            print(f"✅ Conversão bem-sucedida para {pdf_file_name}")
            
            # Exportar para markdown
            try:
                markdown_content = result.document.export_to_markdown()
                
                # Nome do arquivo Markdown correspondente
                md_file_name = os.path.splitext(pdf_file_name)[0] + ".md"
                md_file_path = os.path.join(md_folder, md_file_name)
                
                # Salvar o conteúdo no arquivo Markdown
                with open(md_file_path, "w", encoding="utf-8") as md_file:
                    md_file.write(markdown_content)
                
                print(f"✅ Convertido: {pdf_file_name} -> {md_file_name}")
                return True, None
            except Exception as export_err:
                print(f"❌ Erro ao exportar para Markdown: {str(export_err)}")
                traceback.print_exc()
                return False, f"Erro na exportação: {str(export_err)}"
        else:
            error_msg = "Resultado inválido ou nulo"
            print(f"❌ Falha na conversão: {error_msg}")
            return False, error_msg
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Erro ao processar: {error_msg}")
        traceback.print_exc()
        
        # Se for a primeira tentativa e parece ser um erro de memória, tentar novamente com GC
        if retry_count == 0 and any(word in error_msg.lower() for word in ["memory", "memória", "alocação"]):
            print("🔄 Tentando forçar liberação de memória e tentar novamente...")
            gc.collect()
            return process_single_pdf(pdf_file_name, pdf_folder, md_folder, args, retry_count=1)
        
        # Classificar o tipo de erro para relatório mais detalhado
        if "barramento" in error_msg.lower():
            error_type = "Erro no barramento (falha grave de acesso à memória)"
        elif "memory" in error_msg.lower() or "memória" in error_msg.lower():
            error_type = "Erro de memória"
        else:
            error_type = f"Erro: {error_msg}"
        
        return False, error_type

def main():
    """Função principal do script."""
    args = parse_arguments()
    
    print("🚀 Iniciando conversão de PDFs para Markdown usando Docling...")
    
    # Configurar diretórios
    pdf_folder, md_folder = setup_directories(args.input_dir, args.output_dir)
    if not pdf_folder:
        return
    
    # Lista os arquivos PDF na pasta
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"⚠️ Nenhum arquivo PDF encontrado em '{pdf_folder}'")
        print(f"   Por favor, adicione seus PDFs e execute novamente.")
        return
    
    # Ordenar por tamanho (menor para maior) para começar com arquivos menores
    pdf_files_with_size = [(f, os.path.getsize(os.path.join(pdf_folder, f))) for f in pdf_files]
    pdf_files_with_size.sort(key=lambda x: x[1])
    pdf_files = [f[0] for f in pdf_files_with_size]
    
    print(f"🔍 Encontrados {len(pdf_files)} arquivos PDF.")
    print("📊 Arquivos ordenados por tamanho (os menores serão processados primeiro)")
    
    # Processamento principal
    count = 0
    sucessos = 0
    falhas = 0
    arquivos_com_falha = []
    erros_por_arquivo = {}
    
    for pdf_file_name in pdf_files:
        count += 1
        print(f"\n🔍 Processando arquivo {count} de {len(pdf_files)}: {pdf_file_name}")
        
        # Garantir que o sistema está em bom estado antes de cada conversão
        gc.collect()
        
        # Processar o arquivo
        success, error = process_single_pdf(pdf_file_name, pdf_folder, md_folder, args)
        
        if success:
            sucessos += 1
        else:
            falhas += 1
            arquivos_com_falha.append(pdf_file_name)
            erros_por_arquivo[pdf_file_name] = error
        
        print(f"--- Concluído {count}/{len(pdf_files)} ---")
    
    print("\n📊 Resumo da conversão:")
    print(f"Total de arquivos: {len(pdf_files)}")
    print(f"Sucessos: {sucessos}")
    print(f"Falhas: {falhas}")
    
    if falhas > 0:
        print("\nArquivos com falha:")
        for arquivo in arquivos_com_falha:
            erro = erros_por_arquivo.get(arquivo, "Erro desconhecido")
            print(f"- {arquivo}: {erro}")
    
    print("\n✨ Processo finalizado!")
    
    if falhas > 0 and sucessos == 0:
        print("\n⚠️ Todos os arquivos falharam. Considere usar o script pandocconvert.py como alternativa.")

if __name__ == "__main__":
    main()
