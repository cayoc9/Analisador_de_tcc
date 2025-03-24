#!/usr/bin/env python3
import os
import re

# Diretório onde estão os arquivos
diretorio = 'analise_fichamento/livros'

# Função para normalizar nomes de arquivos
def normalizar_nome(nome_original):
    # Garantir que mantemos a extensão
    nome_base, extensao = os.path.splitext(nome_original)
    
    # Se o arquivo já começa com "fichamento_", preservamos isso
    if nome_base.startswith('fichamento_'):
        nome_base = nome_base[11:]  # Remove o prefixo para normalizar o resto
    
    # Normalizar: remover caracteres especiais e substituir espaços por underscores
    nome_normalizado = re.sub(r'[^\w\s\-]', '', nome_base)  # Remove caracteres especiais
    nome_normalizado = nome_normalizado.replace(' - ', '_')  # Substitui " - " por "_"
    nome_normalizado = nome_normalizado.replace(' ', '_')  # Substitui espaços por underscores
    nome_normalizado = re.sub(r'_{2,}', '_', nome_normalizado)  # Remove underscores múltiplos
    
    # Adicionar prefixo "fichamento_" novamente
    return f"fichamento_{nome_normalizado}{extensao}"

# Listar todas as alterações planejadas
alteracoes = []
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.md') and 'fichamento_' in arquivo:
        novo_nome = normalizar_nome(arquivo)
        if novo_nome != arquivo:
            alteracoes.append((arquivo, novo_nome))

# Exibir alterações planejadas
print("Alterações planejadas:")
for original, novo in alteracoes:
    print(f"  {original} -> {novo}")

# Confirmar com o usuário
confirmacao = input("\nExecutar estas alterações? (s/n): ")
if confirmacao.lower() == 's':
    # Executar as alterações
    for original, novo in alteracoes:
        caminho_original = os.path.join(diretorio, original)
        caminho_novo = os.path.join(diretorio, novo)
        os.rename(caminho_original, caminho_novo)
    print("\nAlterações concluídas com sucesso!")
else:
    print("\nOperação cancelada.") 