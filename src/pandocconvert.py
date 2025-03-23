import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path
import traceback
from pypdf import PdfReader, PdfWriter

# Caminhos das pastas
PDF_FOLDER = os.path.abspath("src/PDFs")
MD_FOLDER = os.path.abspath("src/MD_")

print("🚀 Iniciando conversão de PDFs para Markdown usando Pandoc...")

# Verificar se Pandoc está instalado
try:
    subprocess.run(["pandoc", "--version"], check=True, stdout=subprocess.PIPE)
    print("✅ Pandoc está instalado e pronto para uso")
except (subprocess.SubprocessError, FileNotFoundError):
    print("❌ Pandoc não está instalado. Por favor, instale com: sudo apt-get install pandoc")
    sys.exit(1)

# Criar a pasta MD se não existir
if not os.path.exists(MD_FOLDER):
    os.makedirs(MD_FOLDER)

# Lista os arquivos PDF na pasta
pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]

# Ordenar por tamanho (menor para maior) para começar com arquivos menores
pdf_files_with_size = [(f, os.path.getsize(os.path.join(PDF_FOLDER, f))) for f in pdf_files]
pdf_files_with_size.sort(key=lambda x: x[1])
pdf_files = [f[0] for f in pdf_files_with_size]

print(f"🔍 Encontrados {len(pdf_files)} arquivos PDF.")
print("📊 Arquivos ordenados por tamanho (os menores serão processados primeiro)")

# Função para verificar se o PDF está protegido ou corrompido
def verificar_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            pdf = PdfReader(f)
            if pdf.is_encrypted:
                return False, "PDF está protegido por senha"
            # Verificar se consegue acessar o conteúdo
            num_paginas = len(pdf.pages)
            print(f"📄 PDF tem {num_paginas} páginas")
            # Tenta acessar o texto da primeira página para verificar integridade
            try:
                texto_primeira_pagina = pdf.pages[0].extract_text()
                if not texto_primeira_pagina:
                    return False, "Não foi possível extrair texto do PDF (possível imagem ou PDF scanneado)"
            except Exception as e:
                return False, f"Erro ao extrair texto: {str(e)}"
            return True, None
    except Exception as e:
        return False, f"Falha ao abrir PDF: {str(e)}"

# Função para processar um único arquivo usando Pandoc
def process_single_pdf(pdf_file_name):
    file_path = os.path.join(PDF_FOLDER, pdf_file_name)
    md_file_name = os.path.splitext(pdf_file_name)[0] + ".md"
    md_file_path = os.path.join(MD_FOLDER, md_file_name)
    
    # Verificação do tamanho do arquivo
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # tamanho em MB
    print(f"📄 Tamanho do arquivo: {file_size:.2f} MB")
    
    # Verificar se o PDF é válido
    valido, erro = verificar_pdf(file_path)
    if not valido:
        print(f"⚠️ Problema com o PDF: {erro}")
        return False, erro
    
    # Usar um diretório temporário para arquivos intermediários
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            # Comando Pandoc para converter PDF para Markdown
            cmd = [
                "pandoc",
                "--from=pdf",
                "--to=markdown",
                "--standalone",
                "--wrap=none",  # Evita quebras de linha automáticas
                file_path,
                "-o", md_file_path
            ]
            
            print(f"🔍 Convertendo {pdf_file_name} para Markdown usando Pandoc...")
            result = subprocess.run(
                cmd, 
                check=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True,
                timeout=300  # 5 minutos de timeout
            )
            
            # Verificar se o arquivo foi criado e tem conteúdo
            if os.path.exists(md_file_path) and os.path.getsize(md_file_path) > 0:
                print(f"✅ Convertido: {pdf_file_name} -> {md_file_name}")
                return True, None
            else:
                error_msg = "Arquivo de saída vazio ou não criado"
                print(f"❌ Falha na conversão: {error_msg}")
                return False, error_msg
                
        except subprocess.CalledProcessError as e:
            error_msg = f"Erro do Pandoc (código {e.returncode}): {e.stderr}"
            print(f"❌ Falha na conversão: {error_msg}")
            return False, error_msg
            
        except subprocess.TimeoutExpired:
            error_msg = "Conversão excedeu o tempo limite (5 minutos)"
            print(f"❌ Falha na conversão: {error_msg}")
            return False, error_msg
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Erro ao processar: {error_msg}")
            traceback.print_exc()
            return False, error_msg

# Processamento principal
count = 0
sucessos = 0
falhas = 0
arquivos_com_falha = []
erros_por_arquivo = {}

for pdf_file_name in pdf_files:
    count += 1
    print(f"\n🔍 Processando arquivo {count} de {len(pdf_files)}: {pdf_file_name}")
    
    # Processar o arquivo
    success, error = process_single_pdf(pdf_file_name)
    
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