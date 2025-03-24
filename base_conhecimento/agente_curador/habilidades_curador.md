# Estratégias Avançadas de Prompting para o Agente Curador de Knowledge Base

Como Engenheiro de Prompt, desenvolvi estratégias específicas para potencializar as habilidades do Curador de Knowledge Base, garantindo maior qualidade e precisão nas suas atividades de gestão da base de conhecimentos sobre aprendizagem autodirigida.

## 1. Prompts para Normalização e Validação de Referências

### Prompt 1.1: Normalização Estruturada de Referências

```markdown
Como especialista em gestão de referências acadêmicas, execute uma normalização estruturada nas seguintes referências sobre [TEMA ESPECÍFICO]:

[LISTA DE REFERÊNCIAS EM FORMATO BRUTO]

Para cada referência:

1. PADRONIZAÇÃO FORMAL:

   - Corrija o formato segundo normas ABNT
   - Verifique a ordem correta dos elementos (autores, título, periódico, ano, etc.)
   - Normalize capitalização de títulos e nomes próprios

2. ENRIQUECIMENTO DE METADADOS:

   - Adicione DOI se disponível (consulte bases como CrossRef)
   - Inclua palavras-chave padronizadas (entre 3-5)
   - Verifique e complete informações faltantes (volume, número, páginas)

3. DESAMBIGUAÇÃO:

   - Identifique possíveis variações de nome de autores (ex: "Silva, J." vs "Silva, João")
   - Padronize nomes de instituições e periódicos
   - Resolva abreviações inconsistentes

4. CLASSIFICAÇÃO PRELIMINAR:

   - Tipo de publicação (artigo, livro, capítulo, etc.)
   - Período (anterior a 2000, 2000-2010, 2011-presente)
   - Idioma original
   - Categoria temática principal (utilize as categorias: [LISTA DE CATEGORIAS])

5. VERIFICAÇÃO DE ACESSIBILIDADE:
   - Status de disponibilidade (público, acesso restrito, indisponível)
   - URL permanente ou identificador estável
   - Indicação de repositório interno onde o texto completo está armazenado

Forneça a saída em formato CSV no arquivo [gerenciamento_de_referências.csv](../../../analise_fichamento/resumos_csv/Gerenciamento_Referencias.csv) com colunas claramente identificadas para cada elemento acima.
```

### Prompt 1.2: Validação de Integridade de Referências

```markdown
Como auditor de qualidade de bases bibliográficas, avalie criticamente as seguintes referências:

[LISTA DE REFERÊNCIAS EM FORMATO ESTRUTURADO]

Execute uma análise completa de integridade seguindo estas etapas:

1. VERIFICAÇÃO DE COMPLETUDE:

   - Identifique campos obrigatórios ausentes por tipo de referência
   - Quantifique o percentual de completude para cada referência (score 0-100%)
   - Sinalize campos críticos faltantes com prioridade ALTA/MÉDIA/BAIXA

2. DETECÇÃO DE INCONSISTÊNCIAS:

   - Identifique discrepâncias entre campos relacionados (ex: data online vs impressa)
   - Verifique inconsistências de formato dentro do mesmo tipo de campo
   - Detecte valores improváveis ou impossíveis (ex: datas futuras, páginas inválidas)

3. VALIDAÇÃO DE EXISTÊNCIA:

   - Para cada DOI ou URL, indique se é acessível/válido
   - Verifique existência do periódico em bases de indexação
   - Confirme a existência dos autores em bases acadêmicas quando possível

4. DIAGNÓSTICO DE QUALIDADE:
   - Classifique cada referência como: ÍNTEGRA, NECESSITA REVISÃO, PROBLEMÁTICA
   - Para cada problema identificado, sugira ação corretiva específica
   - Priorize as referências que necessitam intervenção imediata

Forneça um relatório estruturado com estatísticas gerais e detalhamento por referência, adequado para direcionar ações de manutenção da base.
```

## 2. Prompts para Detecção e Gestão de Redundâncias

### Prompt 2.1: Identificação Multi-nível de Duplicidades

```markdown
Como especialista em deduplicação de dados bibliográficos, analise este conjunto de referências para identificar redundâncias em múltiplos níveis:

[CONJUNTO DE REFERÊNCIAS EM FORMATO ESTRUTURADO]

Execute uma análise progressiva em 4 níveis:

1. DUPLICAÇÃO EXATA:

   - Identifique entradas completamente idênticas
   - Agrupe por coincidência perfeita de DOI, título e autores
   - Recomende exclusão direta mantendo a entrada mais completa

2. DUPLICAÇÃO SUBSTANCIAL:

   - Detecte variações mínimas do mesmo trabalho (ex: diferenças de capitalização, pontuação)
   - Identifique mesmo conteúdo com diferentes metadados
   - Aplique algoritmos de similaridade (Levenshtein, cosine similarity) para títulos
   - Sugira mesclar informações, mantendo a entrada mais rica em metadados

3. VARIANTES DA MESMA OBRA:

   - Identifique diferentes edições do mesmo material
   - Detecte versões preprint/postprint do mesmo artigo
   - Reconheça traduções da mesma obra
   - Recomende manter todas com anotação de relacionamento

4. REDUNDÂNCIA CONCEITUAL:
   - Identifique trabalhos do mesmo autor que apresentam o mesmo estudo em diferentes periódicos
   - Detecte publicações que são subconjuntos de outras mais abrangentes
   - Identifique artigos que evoluíram para capítulos de livros
   - Sugira manter conforme relevância e completude, com anotações de relacionamento

Para cada grupo de redundâncias, forneça:

- Identificadores únicos de cada entrada relacionada
- Nível de confiança na detecção (0-100%)
- Recomendação específica (manter, excluir, mesclar, anotar)
- Justificativa para a recomendação

Apresente os resultados em formato tabular, agrupados por tipo de redundância e ordenados por prioridade de intervenção.
```

### Prompt 2.2: Consolidação Inteligente de Entradas Redundantes

```markdown
Como especialista em fusão de dados bibliográficos, consolide as seguintes entradas identificadas como redundantes:

[GRUPOS DE REFERÊNCIAS REDUNDANTES]

Para cada grupo, execute uma consolidação inteligente seguindo estas etapas:

1. SELEÇÃO DE ENTRADA PRINCIPAL:

   - Identifique a entrada mais completa em termos de metadados
   - Priorize versões com DOI ou identificadores persistentes
   - Prefira versões publicadas sobre preprints
   - Entre versões equivalentes, selecione a mais recente

2. ENRIQUECIMENTO CRUZADO:

   - Extraia campos exclusivos ou mais completos das entradas secundárias
   - Preserve todas as palavras-chave únicas
   - Mantenha notas e anotações de todas as fontes
   - Combine URLs e identificadores alternativos

3. RECONCILIAÇÃO DE CONFLITOS:

   - Em caso de informações conflitantes, aplique estas regras de prioridade:
     - Metadados de publicações com DOI > sem DOI
     - Informação de fonte original > fonte secundária
     - Dados mais detalhados > dados genéricos
     - Versão mais recente > versão mais antiga (para atualizações)

4. GERAÇÃO DE REGISTRO UNIFICADO:
   - Crie uma entrada unificada com todos os campos harmonizados
   - Adicione campo de "Variantes Fundidas" listando IDs das entradas mescladas
   - Inclua justificativa para resolução de cada conflito significativo
   - Preserve histórico de proveniência dos dados mesclados

Apresente cada registro consolidado em formato CSV completo, acompanhado de resumo das ações tomadas e campos enriquecidos.
```

## 3. Prompts para Classificação e Categorização Temática

### Prompt 3.1: Categorização Multi-dimensional com Ontologia Específica

```markdown
Como especialista em taxonomia e classificação de literatura científica sobre aprendizagem autodirigida, categorize os seguintes trabalhos:

[LISTA DE REFERÊNCIAS COM TÍTULOS, RESUMOS E PALAVRAS-CHAVE]

Aplique uma categorização multi-dimensional utilizando as seguintes ontologias específicas:

1. DIMENSÃO TEÓRICO-CONCEITUAL:

   - Fundamentos cognitivos da SDL
   - Modelos de autorregulação
   - Teorias motivacionais
   - Abordagens andragógicas
   - Epistemologias construtivistas
   - Outras: [especificar se necessário]

2. DIMENSÃO METODOLÓGICA:

   - Aprendizagem baseada em problemas
   - Metodologia de projetos
   - Sala de aula invertida
   - Aprendizagem entre pares
   - Estratégias metacognitivas
   - Avaliação formativa para SDL
   - Outras: [especificar se necessário]

3. DIMENSÃO CONTEXTUAL:

   - Ensino superior
   - Educação profissional
   - Formação de professores
   - Ensino de computação
   - Educação a distância
   - Educação continuada
   - Outras: [especificar se necessário]

4. DIMENSÃO APLICADA:
   - Intervenções pedagógicas
   - Ferramentas de suporte à SDL
   - Métricas e instrumentos de avaliação
   - Estudos de caso
   - Análise de eficácia
   - Desenvolvimento profissional docente
   - Outras: [especificar se necessário]

Para cada referência:

- Atribua categorias primárias e secundárias em cada dimensão
- Indique o grau de relevância para cada categoria (1-5)
- Forneça justificativa breve baseada no conteúdo
- Sugira palavras-chave padronizadas alinhadas com as categorias

Apresente a classificação em formato estruturado que possa ser convertido para um banco de dados relacional, mantendo as relações hierárquicas entre categorias.
```

### Prompt 3.2: Análise de Clusters e Mapeamento Temático

```markdown
Como especialista em bibliometria e análise de corpus científicos, realize um mapeamento temático do seguinte conjunto de referências:

[CONJUNTO DE REFERÊNCIAS COM METADADOS COMPLETOS]

Execute uma análise de clusters temáticos seguindo estas etapas:

1. IDENTIFICAÇÃO DE TEMAS EMERGENTES:

   - Extraia termos de alta frequência dos títulos, resumos e palavras-chave
   - Aplique análise semântica para identificar conceitos relacionados
   - Detecte grupos temáticos naturais sem classificação prévia
   - Nomeie cada cluster emergente com base em seus termos definidores

2. ANÁLISE DE CO-OCORRÊNCIA:

   - Identifique conceitos que frequentemente aparecem juntos
   - Mapeie relações entre diferentes clusters temáticos
   - Quantifique a força das conexões entre temas (0-1)
   - Identifique conceitos-ponte que conectam diferentes áreas

3. EVOLUÇÃO TEMPORAL DE TEMAS:

   - Analise como os temas evoluíram ao longo do tempo
   - Identifique temas em ascensão vs. temas em declínio
   - Detecte mudanças de terminologia para conceitos similares
   - Projete tendências emergentes baseadas em padrões recentes

4. LACUNAS E OPORTUNIDADES:
   - Identifique áreas subexploradas na intersecção de temas
   - Detecte desconexões entre clusters que poderiam ser integrados
   - Sugira temas potencialmente relevantes ausentes do corpus
   - Indique oportunidades para trabalhos integradores entre clusters

Apresente os resultados como:

- Um mapa visual de clusters com suas interconexões
- Uma tabela de atribuição de referências a clusters (com scores de pertinência)
- Uma análise temporal mostrando a evolução dos principais temas
- Recomendações para organização da base de conhecimento baseada na estrutura temática natural
```

## 4. Prompts para Complementação e Enriquecimento da Base

### Prompt 4.1: Identificação de Lacunas Críticas

```markdown
Como consultor estratégico para desenvolvimento de bases de conhecimento acadêmico, realize uma análise de lacunas críticas na seguinte coleção:

[VISÃO GERAL DA BASE DE CONHECIMENTO ATUAL]

Identifique sistematicamente:

1. LACUNAS FUNDAMENTAIS:

   - Trabalhos seminais ausentes na área de SDL (verifique citações frequentes não presentes na base)
   - Autores influentes com representação insuficiente
   - Períodos históricos com cobertura inadequada
   - Correntes teóricas subrepresentadas

2. LACUNAS CONTEXTUAIS:

   - Ausência de estudos específicos sobre licenciatura em computação
   - Carência de pesquisas no contexto brasileiro/latino-americano
   - Insuficiência de trabalhos sobre temas emergentes relevantes
   - Falta de estudos comparativos entre contextos diversos

3. LACUNAS METODOLÓGICAS:

   - Desequilíbrio entre estudos qualitativos e quantitativos
   - Ausência de meta-análises ou revisões sistemáticas recentes
   - Falta de estudos longitudinais sobre desenvolvimento de SDL
   - Escassez de pesquisas com metodologias específicas relevantes

4. PRIORIZAÇÃO ESTRATÉGICA:
   - Classifique cada lacuna identificada por criticidade (Alta/Média/Baixa)
   - Avalie o impacto de cada lacuna na robustez do referencial teórico
   - Estime a dificuldade de preenchimento (facilidade de acesso a fontes)
   - Recomende ordem de prioridade para complementação

Para cada lacuna crítica identificada, forneça:

- Justificativa detalhada baseada na análise da coleção atual
- Recomendações específicas de fontes para preenchimento (quando possível)
- Estratégias de busca sugeridas para localizar materiais relevantes
- Indicação de especialistas ou repositórios especializados para consulta

Apresente a análise em formato estruturado, priorizando as lacunas mais críticas para a construção de um referencial teórico robusto sobre SDL no contexto da licenciatura em computação.
```

### Prompt 4.2: Enriquecimento Contextual de Referências-Chave

```markdown
Como especialista em contextualização de literatura científica, enriqueça as seguintes referências-chave com informações contextuais aprofundadas:

[LISTA DE REFERÊNCIAS PRIORITÁRIAS]

Para cada referência, desenvolva:

1. MAPEAMENTO DE INFLUÊNCIA ACADÊMICA:

   - Identifique trabalhos seminais que influenciaram esta referência
   - Mapeie trabalhos posteriores significativamente influenciados por ela
   - Posicione a referência em sua "árvore genealógica" acadêmica
   - Quantifique impacto via métricas relevantes (citações, altmetrics)

2. CONTEXTUALIZAÇÃO HISTÓRICO-CIENTÍFICA:

   - Descreva o contexto acadêmico quando o trabalho foi publicado
   - Identifique debates ou controvérsias relacionados à época
   - Explique como o trabalho respondeu a questões do seu tempo
   - Avalie como sua recepção evoluiu ao longo do tempo

3. EXTRAÇÃO DE CONTRIBUIÇÕES DISTINTIVAS:

   - Identifique inovações conceituais ou metodológicas introduzidas
   - Extraia definições operacionais de conceitos-chave
   - Destaque evidências empíricas originais apresentadas
   - Identifique limitações reconhecidas pelos próprios autores

4. RELEVÂNCIA ESPECÍFICA PARA SDL EM COMPUTAÇÃO:
   - Analise aplicabilidade ao contexto da licenciatura em computação
   - Identifique elementos transferíveis para o ensino de computação
   - Avalie adaptações necessárias ao contexto brasileiro
   - Articule conexões com outros trabalhos na base de conhecimento

Apresente cada enriquecimento em formato de "cartão de referência avançado" com campos estruturados, incluindo citações relevantes e recomendações de leitura complementar dentro da base.
```

## 5. Prompts para Análise de Qualidade e Manutenção da Base

### Prompt 5.1: Auditoria de Qualidade e Relevância

```markdown
Como auditor de qualidade de bases de conhecimento acadêmico, realize uma avaliação abrangente da seguinte coleção:

[VISÃO GERAL DA BASE DE CONHECIMENTO]

Execute uma auditoria sistemática seguindo estes parâmetros:

1. QUALIDADE DAS FONTES:

   - Avalie o perfil das publicações (classificação Qualis/JCR/Scopus)
   - Verifique credibilidade e reconhecimento dos autores
   - Analise atualidade do material (distribuição temporal)
   - Examine diversidade de fontes (evitando concentração excessiva)

2. RELEVÂNCIA TEMÁTICA:

   - Calcule precisão temática (% de material diretamente relacionado à SDL)
   - Avalie cobertura dos subtemas essenciais (identificar lacunas)
   - Verifique alinhamento com perguntas de pesquisa específicas
   - Identifique materiais periféricos ou tangenciais

3. EQUILÍBRIO E REPRESENTATIVIDADE:

   - Analise distribuição entre perspectivas teóricas diferentes
   - Verifique equilíbrio entre material teórico e evidências empíricas
   - Examine representatividade geográfica e cultural
   - Avalie presença de visões contraditórias ou críticas

4. INTEGRIDADE ESTRUTURAL:
   - Verifique completude dos metadados essenciais
   - Avalie consistência na categorização e indexação
   - Teste integridade dos links e referências cruzadas
   - Examine redundâncias e sobreposições excessivas

Para cada dimensão, gere:

- Pontuação quantitativa (0-100%)
- Identificação específica de problemas
- Recomendações acionáveis para melhoria
- Estimativa de esforço necessário para correção

Apresente um dashboard visual com indicadores de saúde da base, destacando áreas críticas para intervenção e fornecendo um plano de manutenção preventiva.
```

### Prompt 5.2: Recomendações Inteligentes e Relacionamentos Cruzados

```markdown
Como cientista de dados especializado em sistemas de recomendação acadêmica, analise a base de conhecimento para gerar:

[BASE DE CONHECIMENTO COMPLETA EM FORMATO ESTRUTURADO]

Desenvolva um sistema de recomendações inteligentes que:

1. IDENTIFICAÇÃO DE RELACIONAMENTOS IMPLÍCITOS:

   - Detecte trabalhos conceitualmente relacionados mesmo sem citações mútuas
   - Identifique complementaridades metodológicas entre estudos
   - Descubra conexões temáticas não explícitas entre referências
   - Mapeie progressões lógicas para construção de argumentação

2. RECOMENDAÇÕES CONTEXTUAIS:

   - Para cada seção do referencial teórico, sugira as referências mais relevantes
   - Para cada conceito-chave, identifique a sequência ideal de fontes
   - Para cada metodologia ativa, recomende estudos empíricos relacionados
   - Para cada desafio identificado, sugira fontes com propostas de solução

3. CAMINHOS DE NAVEGAÇÃO TEMÁTICA:

   - Construa sequências lógicas de leitura por subtema
   - Identifique pontos de entrada ideais para cada área temática
   - Mapeie rotas de aprofundamento progressivo
   - Sugira conexões interdisciplinares relevantes

4. DETECÇÃO DE LACUNAS DE CONHECIMENTO:
   - Identifique questões frequentemente mencionadas mas não respondidas
   - Detecte premissas implícitas não fundamentadas
   - Mapeie áreas onde evidências empíricas são insuficientes
   - Sugira direções para complementação da base

Apresente os resultados como:

- Grafo de relacionamentos entre referências com pesos de relevância
- Sistema de "Referências relacionadas" para cada entrada
- Trilhas de navegação temática com sequência sugerida
- Mapa de calor destacando áreas de alta/baixa densidade de conhecimento
```

## Implementação Estratégica dos Prompts

Para implementação prática destas estratégias, recomendo:

1. **Implementação Progressiva:**

   - Comece pelas estratégias de normalização e validação (1.1 e 1.2)
   - Avance para deduplicação (2.1 e 2.2)
   - Prossiga com categorização (3.1 e 3.2)
   - Implemente complementação (4.1 e 4.2) após base estabilizada
   - Finalize com análise de qualidade (5.1 e 5.2)

2. **Adaptação por Volume de Dados:**

   - Para conjuntos pequenos (<50 referências): aplique prompts completos
   - Para conjuntos médios (50-200): divida em lotes temáticos
   - Para conjuntos grandes (>200): aplique abordagem amostral seguida de generalização

3. **Estratégia de Modelo por Tarefa:**

   - Tarefas de categorização e análise conceitual: modelos Sonnet (maior capacidade)
   - Tarefas de normalização e verificação: modelos Haiku (mais eficientes)
   - Tarefas de deduplicação: combinar abordagem programática com verificação por LLM

4. **Regime de Manutenção:**
   - Auditoria completa (prompt 5.1): trimestral
   - Normalização de novas entradas (prompt 1.1): imediata na inclusão
   - Deduplicação (prompt 2.1): quinzenal
   - Análise de lacunas (prompt 4.1): mensal
