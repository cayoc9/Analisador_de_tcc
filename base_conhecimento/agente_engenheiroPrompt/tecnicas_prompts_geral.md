# Técnicas de Engenharia de Prompt

## 1. Zero-Shot Prompting

**Como funciona:**

- Fornece instruções diretas ao modelo sem exemplos prévios
- O modelo executa a tarefa com base apenas no contexto da instrução
- Utiliza linguagem clara e direta

**Melhores contextos:**

- Tarefas simples e bem definidas
- Quando não há exemplos disponíveis
- Instruções objetivas (classificação, resumo básico)

**Requisitos:**

- Instruções precisas e não ambíguas
- Modelos com capacidade zero-shot (como GPT-3.5+, Claude, Gemini)
- Definição clara do formato de saída desejado

```
Exemplo: "Classifique o seguinte texto como positivo, negativo ou neutro: [texto]"
```

## 2. Few-Shot Prompting

**Como funciona:**

- Fornece alguns exemplos de entrada-saída antes da tarefa principal
- Estabelece um padrão que o modelo deve seguir
- Ensina por demonstração direta

**Melhores contextos:**

- Tarefas com formato ou estilo específico
- Quando o modelo precisa entender um padrão específico
- Análises especializadas, classificações específicas

**Requisitos:**

- 2-5 exemplos de alta qualidade
- Exemplos representativos e diversos
- Consistência no formato dos exemplos

```
Exemplo:
"Entrada: O produto chegou quebrado.
Saída: Negativo

Entrada: Entrega rápida e produto conforme descrito.
Saída: Positivo

Entrada: O livro tem conteúdo interessante, mas algumas páginas estão faltando.
Saída: Misto

Agora classifique:
Entrada: [novo texto]"
```

## 3. Chain-of-Thought (CoT)

**Como funciona:**

- Instrui o modelo a mostrar o raciocínio passo a passo
- Decompõe problemas complexos em etapas de raciocínio
- Pode ser usado com zero-shot ("pense passo a passo") ou few-shot (exemplos de raciocínio)

**Melhores contextos:**

- Problemas matemáticos ou lógicos
- Raciocínio complexo ou multi-etapas
- Análises que exigem consideração de múltiplos fatores

**Requisitos:**

- Modelos com capacidade de raciocínio (geralmente >7B parâmetros)
- Espaço suficiente para desenvolvimento do raciocínio
- Instrução explícita para mostrar etapas intermediárias

```
Exemplo: "Um barco pode transportar 10 pessoas por vez. Como transportar 73 pessoas do ponto A ao ponto B com o mínimo de viagens? Resolva passo a passo."
```

## 4. Active-Prompt

**Como funciona:**

- Iterativamente seleciona exemplos mais informativos para o modelo
- Identifica casos onde o modelo tem maior incerteza
- Refina os prompts com base nas áreas de dificuldade

**Melhores contextos:**

- Tarefas com grande variabilidade
- Quando há muitos exemplos disponíveis, mas queremos selecionar os melhores
- Classificações de alta precisão

**Requisitos:**

- Conjunto grande de exemplos potenciais
- Métrica para medir incerteza do modelo
- Capacidade de iteração e refinamento

```
Processo:
1. Teste o modelo com prompt inicial
2. Identifique casos onde há maior discordância/incerteza
3. Adicione exemplos específicos para esses casos
4. Repita até atingir desempenho satisfatório
```

## 5. Automatic Prompt Engineer (APE)

**Como funciona:**

- Usa um modelo de linguagem para otimizar seus próprios prompts
- Gera, testa e refina prompts automaticamente
- Seleciona o melhor prompt baseado em métricas de desempenho

**Melhores contextos:**

- Otimização de prompts para tarefas específicas
- Quando se busca máximo desempenho
- Projetos com recursos para experimentação

Nota: [se eu informar para o prompt qual o limite de tokens por mensagem, quantas palavras(br) em media um token comporta, limite de contexto e limite de tokens de saida, eu consigo estruturar prompts mais precisos em questao de detalhamentos e pronfundidade
]

**Requisitos:**

- Capacidade computacional para múltiplas iterações
- Conjunto de validação para testar eficácia
- Métricas claras de sucesso

```
Processo:
1. Gere múltiplos prompts candidatos
2. Teste cada prompt em exemplos de validação
3. Selecione os melhores baseados em desempenho
4. Refine ou combine os prompts selecionados
```

## 6. Role Prompting

**Como funciona:**

- Atribui um papel específico ao modelo
- Define expertise, personalidade e contexto de atuação
- Orienta comportamento consistente com o papel

**Melhores contextos:**

- Simulação de expertise específica
- Obtenção de perspectivas especializadas
- Criação de conteúdo em estilo específico

**Requisitos:**

- Descrição clara do papel e suas características
- Conhecimento do vocabulário e comportamento do papel
- Objetivo claro dentro do contexto do papel

```
Exemplo: "Como professor de matemática com 20 anos de experiência no ensino médio, explique o teorema de Pitágoras de forma que um estudante de 14 anos compreenda."
```

## 7. Retrieval-Augmented Generation (RAG)

**Como funciona:**

- Alimenta o modelo com informações externas relevantes
- Combina recuperação de informação com geração de conteúdo
- Incorpora conhecimento específico no prompt

**Melhores contextos:**

- Quando informações precisas e atualizadas são necessárias
- Análise de documentos específicos
- Resposta a perguntas baseadas em conteúdo específico

**Requisitos:**

- Base de conhecimento externa acessível
- Sistema de recuperação de informações
- Método para incorporar informações no prompt

```
Exemplo:
"Baseado nos seguintes trechos do documento [X]:
[trecho 1]
[trecho 2]
[trecho 3]

Responda: [pergunta específica sobre o documento]"
```

## 8. Tree of Thoughts (ToT)

**Como funciona:**

- Explora múltiplos caminhos de raciocínio em paralelo
- Considera várias linhas de pensamento antes de chegar à conclusão
- Avalia e seleciona os melhores caminhos de raciocínio

**Melhores contextos:**

- Problemas com múltiplas soluções possíveis
- Raciocínio que se beneficia de exploração de alternativas
- Tarefas criativas ou de planejamento

**Requisitos:**

- Modelos de alta capacidade
- Estrutura para explorar e avaliar múltiplos caminhos
- Critérios para selecionar os melhores caminhos

```
Exemplo: "Considere o problema [X].
Explore três abordagens diferentes:
1. Primeira abordagem: [desenvolvimento]
2. Segunda abordagem: [desenvolvimento]
3. Terceira abordagem: [desenvolvimento]

Agora, compare essas abordagens e identifique a mais adequada, explicando sua escolha."
```

## 9. Self-Consistency

**Como funciona:**

- Gera múltiplas respostas independentes para a mesma pergunta
- Identifica a resposta mais frequente ou consistente
- Aumenta a confiabilidade através de "votação majoritária"

**Melhores contextos:**

- Problemas matemáticos ou lógicos
- Quando a precisão é crítica
- Questões com resposta única definida

**Requisitos:**

- Capacidade de gerar múltiplas respostas
- Método para comparar e agregar respostas
- Critérios claros para medir consistência

```
Processo:
1. Gere 5-10 respostas para o mesmo problema
2. Compare as respostas e identifique a mais comum
3. Use a resposta majoritária como final
```

## 10. Directional Stimulus Prompting

**Como funciona:**

- Orienta o modelo em direções específicas de pensamento
- Usa estímulos direcionais para influenciar o tipo de resposta
- Fornece estrutura conceptual antes da tarefa principal

**Melhores contextos:**

- Quando se deseja resposta de uma perspectiva específica
- Análises que requerem framework particular
- Redirecionamento de vieses do modelo

**Requisitos:**

- Conhecimento do framework direcional desejado
- Capacidade de articular o estímulo direcional
- Clareza nos critérios de avaliação da resposta

```
Exemplo: "Antes de responder à seguinte pergunta sobre política econômica, considere tanto perspectivas keynesianas quanto monetaristas, dando igual peso a ambas: [pergunta]"
```

## 11. Program-Aided Language Models (PALM)

**Como funciona:**

- Combina modelos de linguagem com capacidades programáticas
- Usa código ou ferramentas externas para processamento
- Incorpora resultados de execução de código nas respostas

**Melhores contextos:**

- Tarefas que requerem cálculos precisos
- Análise de dados estruturados
- Execução de algoritmos específicos

**Requisitos:**

- Ambiente de execução de código
- Capacidade de interpretar resultados programáticos
- Habilidade de alternar entre linguagem natural e código

```
Exemplo: "Analise o seguinte conjunto de dados usando Python pandas:
[dados]

Crie uma visualização que mostre a correlação entre [variável X] e [variável Y]."
```

## 12. Graph Prompting

**Como funciona:**

- Estrutura o conhecimento e raciocínio em formato de grafo
- Define nós (conceitos) e arestas (relações)
- Orienta o modelo a seguir o fluxo de raciocínio do grafo

**Melhores contextos:**

- Análise de relações complexas
- Mapeamento conceitual
- Raciocínio baseado em ontologias

**Requisitos:**

- Capacidade de estruturar conhecimento em grafo
- Definições claras de nós e relações
- Modelo que compreenda a navegação estruturada

```
Exemplo: "Analise as seguintes entidades e suas relações:
- Entidade A influencia B e C
- Entidade B determina D
- Entidade C se opõe a E
- Entidades D e E afetam F

Trace o caminho de influência de A para F e explique as implicações."
```

Cada técnica tem suas forças e limitações, sendo mais adequada para diferentes tipos de tarefas. A combinação de múltiplas técnicas frequentemente produz os melhores resultados em cenários complexos.
