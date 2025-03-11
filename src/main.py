import os
import json
import sqlite3
from crewai import LLM, Crew, Process
from crewai_tools import PDFSearchTool  # 📌 Importando a ferramenta correta
from config import (
    DB_FILE, TEMA_ANALISE, solicitacoes, template, controles, restricoes,
    create_agent_leitor, leitor_task,
    create_agent_revisor, revisor_task,
    create_agent_correlacao, correlacao_task
)

# 🔹 Diretório dos PDFs
PDF_FOLDER = os.path.abspath("PDFs")  # Caminho absoluto para evitar problemas
pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]

# 🔹 Configuração do LLM
gpt = LLM(
    model="ollama/qwen2.5:14b",
    base_url="http://localhost:11434"
)

# 🔹 Criar conexão com banco de dados SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# 🔹 Processar cada PDF individualmente
for pdf_file_name in pdf_files:
    file_path = os.path.join(PDF_FOLDER, pdf_file_name)

    # 🔹 Verificar se o arquivo realmente existe antes de continuar
    if not os.path.exists(file_path):
        print(f"❌ ERRO: O arquivo {file_path} não foi encontrado! Pulando...")
        continue
    else:
        print(f"📄 Processando arquivo: {file_path}")  # Debug para garantir que o caminho está certo

    # 🔹 Criar a ferramenta PDFSearchTool com o arquivo atual
    pdf_tool = PDFSearchTool(file_path)

    # 🔹 Criar os agentes para este PDF específico
    agente_leitor = create_agent_leitor(gpt, pdf_tool)
    agente_revisor = create_agent_revisor(gpt)
    agente_correlacao = create_agent_correlacao(gpt)

    # 🔹 Criar as tarefas associadas
    tarefas = [
        leitor_task(agente_leitor),
        revisor_task(agente_revisor),
        correlacao_task(agente_correlacao)
    ]

    # 🔹 Criar e executar a equipe de agentes para este PDF
    crew = Crew(
        agents=[agente_leitor, agente_revisor, agente_correlacao],
        tasks=tarefas,
        process=Process.sequential,
        verbose=True
    )

    print(f"\n🚀 Iniciando processamento do arquivo: {file_path}")

    # 🔹 Executar o CrewAI, passando todas as variáveis necessárias
    resultados = crew.kickoff(inputs={
        "file_path": file_path,  # Passando caminho correto do arquivo para os agentes
        "solicitacoes": solicitacoes,
        "template": template,
        "controles": controles,
        "restricoes": restricoes
    })

    # 🔹 Obter os resultados do CrewAI
    resultados_dict = resultados.json_dict
    print(resultados_dict)
    print(pdf_file_name)
    # 🔹 Inserir os dados extraídos no banco de dados
    cursor.execute("""
    INSERT INTO artigos (titulo, autores, gap, resumo, objetivos, metodologia, resultados, limitacoes, conclusoes, avaliacao, correlacao, topicos_principais)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    pdf_file_name,
    resultados_dict.get("Autores", "Desconhecido"),
    resultados_dict.get("GAP", "Não identificado"),
    resultados_dict.get("Resumo", "Não disponível"),
    resultados_dict.get("Objetivos", "Não informados"),
    resultados_dict.get("Metodologia", "Não descrita"),
    resultados_dict.get("Resultados", "Sem resultados detalhados"),
    resultados_dict.get("Limitações", "Não especificadas"),
    resultados_dict.get("Conclusoes", "Conclusão não mencionada"),
    resultados_dict.get("Avaliacao", "Sem avaliação"),
    int(resultados_dict.get("Correlação", 0)),  # Garante que seja um número inteiro
    json.dumps(resultados_dict.get("Tópicos_Principais", []))  # Armazena lista como JSON
    ))
    conn.commit()


    print(f"✅ {pdf_file_name} processado e salvo no banco de dados com correlação {resultados_dict.get('Correlação', 0)}/10!")

# 🔹 Fechar conexão com o banco de dados
conn.close()
print("\n🚀 Todos os PDFs foram processados e armazenados no banco de dados!")
