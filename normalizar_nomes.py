#!/usr/bin/env python3
import os
import re
import unicodedata

# Diretório onde estão os arquivos
diretorio = 'analise_fichamento/artigos'

# Função para normalizar nomes de arquivos
def normalizar_nome(nome_original):
    # Garantir que mantemos a extensão
    nome_base, extensao = os.path.splitext(nome_original)
    
    # Normalizar o prefixo para "fichamento_" (tudo minúsculo)
    if nome_base.lower().startswith('fichamento'):
        # Remover qualquer prefixo existente (fichamento:, Fichamento_, etc.)
        if ':' in nome_base[:15]:
            nome_base = nome_base.split(':', 1)[1].strip()
        elif '_' in nome_base[:15]:
            nome_base = nome_base.split('_', 1)[1].strip()
        else:
            # Remover "fichamento" ou variações sem separador
            prefixos = ['fichamento', 'Fichamento']
            for prefixo in prefixos:
                if nome_base.startswith(prefixo):
                    nome_base = nome_base[len(prefixo):].strip()
                    break
    
    # Decidir se mantém acentos ou não (neste caso, vamos manter para preservar o idioma)
    # Normalizar: substituir espaços e outros separadores por underscores
    nome_normalizado = nome_base.strip()
    
    # Substituir caracteres especiais por underscores, mas preservar acentos
    nome_normalizado = re.sub(r'[^\w\s\-áàâãéèêíìîóòôõúùûçÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ]', '', nome_normalizado)
    
    # Substituir sequências de caracteres específicos
    nome_normalizado = nome_normalizado.replace(' - ', '_')
    nome_normalizado = nome_normalizado.replace('(', '')
    nome_normalizado = nome_normalizado.replace(')', '')
    nome_normalizado = nome_normalizado.replace(' ', '_')
    
    # Remover underscores múltiplos
    nome_normalizado = re.sub(r'_{2,}', '_', nome_normalizado)
    
    # Adicionar prefixo "fichamento_" novamente
    return f"fichamento_{nome_normalizado}{extensao}"

# Listar todas as alterações planejadas
alteracoes = []
for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.md') and ('fichamento' in arquivo.lower() or 'Fichamento' in arquivo):
        novo_nome = normalizar_nome(arquivo)
        if novo_nome != arquivo:
            alteracoes.append((arquivo, novo_nome))

# Exibir alterações planejadas
print(f"Normalizando arquivos em: {diretorio}")
print(f"Total de arquivos a serem renomeados: {len(alteracoes)}")
print("\nAlterações planejadas:")
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