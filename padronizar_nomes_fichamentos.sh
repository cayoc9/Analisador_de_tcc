#!/bin/bash

# Script para padronizar nomes dos fichamentos de PPCs
# Criado em: $(date +"%d/%m/%Y")

# Diretório dos fichamentos
DIR="/home/cayo/repos/tcc/Analisador_de_tcc/analise_fichamento/ppc"

# Verifica se o diretório existe
if [ ! -d "$DIR" ]; then
    echo "Diretório $DIR não encontrado!"
    exit 1
fi

# Navega para o diretório
cd "$DIR"

# Renomeia os arquivos
mv "Fichamento do PPC de Licenciatura em Computação - IFRJ Campus Pinheiral.md" "fichamento_licenciatura_computacao_IFRJ.md" 2>/dev/null
mv "Fichamento do PPC de Licenciatura em Computação - IFMS Campus Jardim.md" "fichamento_licenciatura_computacao_IFMS.md" 2>/dev/null
mv "FICHAMENTO DO PPC DE LICENCIATURA EM COMPUTAÇÃO - UnB.md" "fichamento_licenciatura_computacao_UnB.md" 2>/dev/null
mv "FICHAMENTO DO PPC DE LICENCIATURA EM COMPUTAÇÃO - IFTO CAMPUS PORTO NACIONAL.md" "fichamento_licenciatura_computacao_IFTO.md" 2>/dev/null
mv "fichamento_UNIVERSIDADE FEDERAL RURAL DO SEMI-ÁRIDO - PPC_2018.md" "fichamento_licenciatura_computacao_UFERSA.md" 2>/dev/null
mv "fichamento_UNIVERSIDADE FEDERAL RURAL DA AMAZÔNIA - PPC_computao_belem_2023_fichamento.md" "fichamento_licenciatura_computacao_UFRA.md" 2>/dev/null
mv "fichamento_UNIVERSIDADE FEDERAL DO VALE DO SÃO FRANCISCO - PPC-CCICOMP_fichamento.md" "fichamento_licenciatura_computacao_UNIVASF.md" 2>/dev/null
mv "fichamento_UNIVERSIDADE FEDERAL DO SUL DA BAHIA - PPC-LI-MatematicaComputacao-2016-revisado-1_fichamento.md" "fichamento_licenciatura_matematica_computacao_UFSB.md" 2>/dev/null
mv "fichamento_PPC_IFBA_Licenciatura_Computacao.md" "fichamento_licenciatura_computacao_IFBA.md" 2>/dev/null

# Conta o número de arquivos padronizados
echo "Arquivos padronizados com sucesso!"
echo "Total de arquivos na pasta: $(ls -l | grep -c "^-")"
echo "Nomenclatura atual dos arquivos:"
ls -1 *.md
