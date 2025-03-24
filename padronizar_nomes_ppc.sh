#!/bin/bash

# Script para padronizar nomes dos fichamentos de PPCs
# Criado para implementar padrão: fichamento_ppc_curso_instituicao.md
# Todas as renomeações são definidas manualmente para maior controle

# Diretório dos fichamentos
DIR="/home/cayo/repos/tcc/Analisador_de_tcc/analise_fichamento/ppc"
cd "$DIR" || { echo "Diretório não encontrado"; exit 1; }

# Backup da pasta (opcional, descomente se quiser backup)
# cp -r "$DIR" "${DIR}_backup_$(date +%Y%m%d_%H%M%S)"

# Mapeamento manual de cada arquivo
# Formato: mv "nome_antigo.md" "nome_novo.md" 2>/dev/null || echo "Erro ao renomear: nome_antigo.md"

# ARQUIVOS COM ANÁLISE NO TÍTULO (remover análise, adicionar ppc)
mv "fichamento_Análise do PPC de Licenciatura em Ciência da Computação (UFPB) sob a Perspectiva da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_ciencia_computacao_ufpb.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação a Distância da UECE.md" \
   "fichamento_ppc_licenciatura_computacao_ead_uece.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação da UEPG - NUTEAD.md" \
   "fichamento_ppc_licenciatura_computacao_uepg.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação da UFPB (2012).md" \
   "fichamento_ppc_licenciatura_computacao_ufpb_2012.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação da UFPI sob a Perspectiva da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_ufpi.md" 2>/dev/null

mv "Fichamento_ Analise do PPC de Licenciatura em Computação da UPE - Análise da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_upe.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação EaD da UFSM.md" \
   "fichamento_ppc_licenciatura_computacao_ead_ufsm.md" 2>/dev/null

mv "fichamento_Análise do PPC de Licenciatura em Computação UFPR Palotina sob a Perspectiva da Aprendizagem Autodirigida (SDL).md" \
   "fichamento_ppc_licenciatura_computacao_ufpr.md" 2>/dev/null

mv "Fichamento_Analise do PPC de Licenciatura em Computação - Universidade Estácio de Sá.md" \
   "fichamento_ppc_licenciatura_computacao_estacio.md" 2>/dev/null

mv "fichamento_Análise do PPC_ Licenciatura em Computação e Robótica Educativa da UFRGS.md" \
   "fichamento_ppc_licenciatura_computacao_robotica_ufrgs.md" 2>/dev/null

# FICHAMENTOS REGULARES (adicionar ppc)
mv "Fichamento do PPC de Licenciatura em Computação e Informática da UNILAB_ Uma Análise Sob a Perspectiva da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_informatica_unilab.md" 2>/dev/null

mv "Fichamento do PPC de Licenciatura em Computação - IF Sertão Pernambucano.md" \
   "fichamento_ppc_licenciatura_computacao_ifsertao_pe.md" 2>/dev/null

mv "Fichamento do PPC de Licenciatura em Computação - IFSULDEMINAS ETAPA 1_ MAPEAMENTO ONTOLÓGICO DO DOCUMENTO.md" \
   "fichamento_ppc_licenciatura_computacao_ifsuldeminas.md" 2>/dev/null

mv "Fichamento do PPC de Licenciatura em Computação - IF Sul-Rio-Grandense.md" \
   "fichamento_ppc_licenciatura_computacao_ifsul.md" 2>/dev/null

# ARQUIVOS JÁ PADRONIZADOS (adicionar apenas ppc)
mv "fichamento_licenciatura_computacao_IFBA.md" \
   "fichamento_ppc_licenciatura_computacao_ifba.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_IFMS.md" \
   "fichamento_ppc_licenciatura_computacao_ifms.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_IFRJ.md" \
   "fichamento_ppc_licenciatura_computacao_ifrj.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_IFTO.md" \
   "fichamento_ppc_licenciatura_computacao_ifto.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_UFERSA.md" \
   "fichamento_ppc_licenciatura_computacao_ufersa.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_UFRA.md" \
   "fichamento_ppc_licenciatura_computacao_ufra.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_UnB.md" \
   "fichamento_ppc_licenciatura_computacao_unb.md" 2>/dev/null

mv "fichamento_licenciatura_computacao_UNIVASF.md" \
   "fichamento_ppc_licenciatura_computacao_univasf.md" 2>/dev/null

mv "fichamento_licenciatura_matematica_computacao_UFSB.md" \
   "fichamento_ppc_licenciatura_matematica_computacao_ufsb.md" 2>/dev/null

# ARQUIVOS COM PPC NO TÍTULO (padronizar formato)
mv "fichamento_PPC de Licenciatura em Computação da UEL.md" \
   "fichamento_ppc_licenciatura_computacao_uel.md" 2>/dev/null

mv "fichamento_PPC de Licenciatura em Computação da UNIR sob a Perspectiva da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_unir.md" 2>/dev/null

mv "fichamento_PPC de Licenciatura em Computação do Claretiano - Centro Universitário_ Foco na Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_claretiano.md" 2>/dev/null

mv "fichamento_PPC de Licenciatura em Computação do IFTM sob a Perspectiva da Aprendizagem Autodirigida.md" \
   "fichamento_ppc_licenciatura_computacao_iftm.md" 2>/dev/null

mv "fichamento_PPC de Licenciatura em Computação - UFGD (2017).md" \
   "fichamento_ppc_licenciatura_computacao_ufgd_2017.md" 2>/dev/null

mv "fichamento_PPC de Licenciatura em Informática das Faculdades Integradas Simonsen.md" \
   "fichamento_ppc_licenciatura_informatica_simonsen.md" 2>/dev/null

mv "fichamento_PPC do Curso Superior em Computação (Licenciatura) do IFB.md" \
   "fichamento_ppc_licenciatura_computacao_ifb.md" 2>/dev/null

mv "fichamento_PPC_IFPB_Licenciatura_Computacao.md" \
   "fichamento_ppc_licenciatura_computacao_ifpb.md" 2>/dev/null

mv "fichamento_PPC - Licenciatura em Ciências da Computação do IF Baiano.md" \
   "fichamento_ppc_licenciatura_ciencias_computacao_ifbaiano.md" 2>/dev/null

# Verificação final
echo "Padronização concluída! Arquivos na pasta:"
ls -1 | grep "^fichamento_ppc" | sort
echo "Total de fichamentos padronizados: $(ls -1 | grep "^fichamento_ppc" | wc -l)"
