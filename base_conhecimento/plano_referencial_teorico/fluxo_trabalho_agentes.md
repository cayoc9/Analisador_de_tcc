# Fluxo de Trabalho: Construção do Referencial Teórico

Este documento descreve o fluxo de trabalho detalhado para a construção do referencial teórico sobre Self-Directed Learning (SDL) no contexto do ensino de Computação, coordenando as interações entre o Curador de Knowledge Base e o Cartógrafo Conceitual.

## Visão Geral do Processo

```
┌─────────────────┐     ┌────────────────────┐     ┌───────────────────┐
│                 │     │                    │     │                   │
│    CURADOR      │────▶│    CARTÓGRAFO      │────▶│    ORIENTADOR     │
│ KNOWLEDGE BASE  │     │    CONCEITUAL      │     │                   │
│                 │◀────│                    │◀────│                   │
└─────────────────┘     └────────────────────┘     └───────────────────┘
       │                        │                          │
       │                        │                          │
       ▼                        ▼                          ▼
┌─────────────────┐     ┌────────────────────┐     ┌───────────────────┐
│  ORGANIZAÇÃO    │     │   MAPEAMENTO E     │     │    VALIDAÇÃO E    │
│     DE DADOS    │     │     ANÁLISE        │     │    ORIENTAÇÃO     │
└─────────────────┘     └────────────────────┘     └───────────────────┘
```

## Detalhamento das Responsabilidades

### Curador de Knowledge Base

- **Função principal**: Extrair, organizar e estruturar conhecimento da literatura
- **Entradas**: Literatura científica, documentos acadêmicos, recursos pedagógicos
- **Saídas**: Conceitos estruturados, matrices de relações, dados para análise
- **Ferramentas**: Templates estruturados, técnicas de extração de conhecimento
- **Métricas de qualidade**: Abrangência, precisão, estruturação, contextualização

### Cartógrafo Conceitual

- **Função principal**: Analisar, mapear e integrar conhecimento em estruturas significativas
- **Entradas**: Dados estruturados do Curador, feedback do Orientador
- **Saídas**: Mapas conceituais, análises de interdependências, diagnósticos
- **Ferramentas**: Técnicas de mapeamento conceitual, análise de relações
- **Métricas de qualidade**: Coerência, integração, profundidade analítica, relevância contextual

### Orientador

- **Função principal**: Validar, orientar e garantir alinhamento com objetivos de pesquisa
- **Entradas**: Produtos do Cartógrafo, questões dos agentes
- **Saídas**: Feedback, direcionamentos, validação
- **Critérios de avaliação**: Rigor científico, alinhamento com objetivos, potencial de contribuição

## Fluxo Detalhado de Atividades

### Fase 1: Mapeamento Conceitual Integrado

1. **Início: Curador**

   - Executa Prompt 1: Levantamento de Conceitos Fundamentais
   - Preenche template_conceitos_fundamentais.md
   - Envia ao Cartógrafo

2. **Cartógrafo**

   - Recebe documento de conceitos fundamentais
   - Executa Prompt 4: Desenvolvimento do Mapa Conceitual Integrado
   - Desenvolve mapa conceitual preliminar
   - Envia ao Orientador para feedback

3. **Orientador**

   - Analisa mapa conceitual
   - Fornece feedback sobre estrutura, completude e relevância
   - Devolve ao Cartógrafo

4. **Cartógrafo**
   - Refina mapa conceitual com base no feedback
   - Finaliza primeira versão do mapa
   - Envia ao Curador e Orientador

### Fase 2: Análise de Interdependências

1. **Início: Curador**

   - Executa Prompt 2: Matriz de Competências e Perfil do Aluno
   - Preenche template_matriz_interdependencias.md
   - Envia ao Cartógrafo

2. **Cartógrafo**

   - Recebe matriz de interdependências
   - Executa Prompt 5: Análise de Interdependências
   - Desenvolve análise preliminar
   - Envia ao Orientador para feedback

3. **Orientador**

   - Analisa documento de interdependências
   - Fornece feedback sobre relações, lacunas e oportunidades
   - Devolve ao Cartógrafo

4. **Cartógrafo**
   - Refina análise com base no feedback
   - Finaliza matriz de interdependências
   - Envia ao Curador e Orientador

### Fase 3: Diagnóstico de Completude

1. **Início: Curador**

   - Executa Prompt 3: Meta-análise Teórica para Diagnóstico de Completude
   - Preenche template_diagnostico_completude.md
   - Envia ao Cartógrafo

2. **Cartógrafo**

   - Recebe documento de meta-análise
   - Executa Prompt 6: Diagnóstico de Completude Teórica
   - Desenvolve diagnóstico preliminar
   - Envia ao Orientador para feedback

3. **Orientador**

   - Analisa diagnóstico de completude
   - Fornece feedback sobre lacunas, recomendações e prioridades
   - Devolve ao Cartógrafo

4. **Cartógrafo**
   - Refina diagnóstico com base no feedback
   - Finaliza diagnóstico de completude
   - Envia ao Curador e Orientador

### Fase 4: Verificação Cruzada e Consolidação

1. **Cartógrafo**

   - Executa Prompt 7: Alinhamento com Perguntas de Pesquisa
   - Preenche documento_verificacao_cruzada.md
   - Envia ao Orientador

2. **Orientador**

   - Analisa verificação cruzada
   - Fornece feedback final sobre alinhamento com objetivos
   - Aprova ou solicita ajustes finais

3. **Cartógrafo e Curador**
   - Realizam ajustes finais conforme feedback
   - Consolidam todos os documentos no referencial teórico final
   - Submetem para aprovação final do Orientador

## Protocolos de Comunicação

### Formato de Entrega de Documentos

- Todos os documentos devem seguir os templates especificados
- Cada entrega deve incluir metadados (versão, autor, data)
- Documentos devem ser nomeados seguindo o padrão: `[fase]_[tipo]_[versão].md`

### Ciclo de Feedback

- Tempo de resposta máximo: 48 horas
- Feedback deve ser específico, acionável e construtivo
- Sugestões devem incluir exemplos quando possível

### Resolução de Divergências

1. Identificação clara da divergência
2. Apresentação de evidências/argumentos de ambas as partes
3. Consulta ao Orientador para arbitragem
4. Documentação da resolução para referência futura

## Indicadores de Progresso

### Marcos de Qualidade

- **Mapa conceitual aprovado**: Estrutura clara, conceitos-chave identificados, relações estabelecidas
- **Matriz de interdependências completa**: Relações identificadas, lacunas mapeadas, oportunidades destacadas
- **Diagnóstico de completude validado**: Lacunas priorizadas, recomendações claras, alinhamento verificado

### Métricas de Avanço

- Porcentagem de conceitos mapeados
- Número de relações identificadas
- Cobertura de perguntas de pesquisa
- Lacunas preenchidas vs. identificadas

## Metadados do Documento

**Versão:** 1.0  
**Autor:** Engenheiro de Prompts  
**Data de criação:** [data]  
**Última atualização:** [data]  
**Status:** Ativo
