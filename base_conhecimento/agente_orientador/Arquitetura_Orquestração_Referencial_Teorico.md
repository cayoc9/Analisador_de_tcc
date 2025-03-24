## Arquitetura de Orquestração para Construção do Referencial Teórico

Focando agora na tarefa em questão – construir um referencial teórico conceitual-descritivo a partir de referências já coletadas (e parcialmente fichadas) – vamos delinear como os agentes colaboram. A arquitetura proposta combina um fluxo sequencial principal com interações pontuais, garantindo aprofundamento da análise e coesão narrativa:

_Exemplo de orquestração de agentes especializados em um fluxo de trabalho. Aqui, um agente "Researcher" e um "Chart Generator" cooperam mediado por um componente roteador central, ilustrando como diferentes agentes podem ser encadeados para cumprir uma tarefa complexa._

1. \*\*Início e Validação do Escopo:

   - O **Pesquisador** inicia revisando as referências disponíveis (e quaisquer fichamentos prévios) para se familiarizar com o material bruto.
   - Em seguida, elabora um **plano preliminar** do referencial teórico – tópicos principais a serem abordados, teorias centrais e possíveis lacunas.
   - Ele então consulta o **Orientador**: apresenta esse plano e discute se o escopo e direção estão adequados.
   - O Orientador avalia, por exemplo, se algum conceito fundamental foi esquecido ou se alguma parte está fora do foco.
   - Essa interação (Pesquisador ↔ Orientador) alinha a visão macro **antes** de aprofundar no trabalho.
   - Se o Orientador aprovar, passamos adiante; se não, o Pesquisador ajusta o plano conforme o feedback e submete novamente.

2. **Organização da Base de Referências:**

   - Em paralelo ou logo após, o **Curador de Base de Conhecimento** (se disponível) organiza as referências coletadas.
   - Ele verifica as fichas parciais existentes, padroniza formatos de citações e agrupa referências por relevância aos tópicos do plano.
   - Por exemplo, identifica quais fontes tratam do conceito A, quais do conceito B, criando “pastas virtuais” ou listas anotadas.
   - Essa curadoria garante que o próximo agente (Revisor) receba um pacote de fontes bem estruturado, poupando tempo ao não ter que ordenar relevâncias.
   - (Se não houver Curador explícito, o Pesquisador deve fazer parte disso manualmente).

3. **Mapeamento Conceitual:**

   - O **Cartógrafo de Conceitos** entra em cena para transformar o plano do Pesquisador em um **esquema conceitual detalhado**.
   - Ele analisa os tópicos e as referências e produz, por exemplo, um mapa mental ou uma lista hierárquica: “1. Definição de Aprendizagem Autodirigida (refs: X, Y); 2. Teorias Relacionadas: 2.1 Andragogia (ref Z), 2.2 Autorregulação (refs: X, W) ...; 3. Estudos Empíricos sobre Aprendizagem Autodirigida em Computação (refs: Y, Z)...”.
   - Esse mapeamento é compartilhado com o Escritor como um **esqueleto** do capítulo e com o Revisor para orientá-lo sobre onde cada fonte se encaixa.
   - O Orientador também pode revisar esse mapa para ver se está conceitualmente completo e coerente.

4. **Análise Profunda das Referências:**

   - Agora o **Revisor/Analista** assume a tarefa central de dissecar as fontes.
   - Ele pode trabalhar uma subseção por vez (conforme o mapa conceitual): por exemplo, primeiro analisa todas as referências ligadas à Definição do conceito principal, depois as de Teorias relacionadas, etc.
   - Para cada referência, ele produz um **fichamento estruturado**, contendo: resumo do conteúdo, pontos-chave, definição de conceitos nas palavras do autor, e eventuais críticas (tipo “Autor X define assim, mas não aborda Y”).
   - Sempre que conclui uma parte (por exemplo, todas as fontes do tópico 1), ele compartilha um _mini-relatório_ daquele tópico com o Escritor e Orientador.
   - Isso permite detecção precoce de problemas – ex.: o Orientador percebe que nenhum autor trouxe a perspectiva histórica do conceito, e pede ao Pesquisador (via Engenheiro de Prompt) para buscar uma referência adicional específica antes de prosseguir.
   - O Revisor então incorporaria essa nova fonte e atualizaria o fichamento. Essa etapa pode ser iterativa: o Revisor avança, Orientador valida segmentadamente. Ao final, temos um conjunto de análises aprofundadas para cada segmento do referencial.

5. **Síntese e Redação pelo Escritor:**

   - Munido do mapa conceitual (estrutura) e dos fichamentos (conteúdo analisado), o **Escritor** começa a redigir o capítulo do referencial teórico.
   - Ele segue a estrutura sugerida, transformando os fichamentos em narrativa coesa.
   - Em cada seção, sintetiza os diversos autores: por exemplo, no parágrafo inicial de “Definição”, ele integra 2-3 definições dos autores X, Y, Z, compara diferenças se houver, e cita todos.
   - Se o **Crítico de Argumentos** for parte do sistema, ele pode previamente alertar o Escritor sobre pontos polêmicos (“Note que Autor X contradiz Autor Y nisso, não deixe de mencionar”).
   - O Escritor presta atenção a manter um **tom descritivo e acadêmico**, cobrindo o que cada conceito significa e como é tratado na literatura, mas também adicionando pitadas críticas conforme insumos do Revisor e do possível Crítico.
   - Durante a escrita, podem surgir dúvidas – o Escritor pode perguntar ao Revisor por mais detalhes de um estudo (“aquele experimento de Autor Y tinha quais resultados mesmo?”) ou pedir ao Pesquisador alguma referência complementar para um ponto que ficou fraco. Tais interações são mediadas pelo Engenheiro de Prompt para que sejam claras e focadas.
   - O resultado desta etapa é um **rascunho completo** do referencial teórico.

6. **Revisão Crítica e Orientação:**

   - O **Orientador** recebe o rascunho do referencial teórico e realiza uma leitura crítica abrangente.
   - Aqui ele verifica: fluxo lógico entre seções, se todas as partes do plano inicial foram cobridas, se há excesso de descrição sem análise (podendo pedir para incluir mais discussão crítica), se as transições estão boas, e se o texto dialoga bem com os objetivos do projeto.
   - O Orientador também confere se as recomendações anteriores foram seguidas (por ex., se pediu para incluir autor W, verifica se de fato está no texto).
   - Frequentemente, o Orientador fará uma **lista de correções ou sugestões**: por exemplo, “Reorganizar os parágrafos na seção 2.2 para primeiro apresentar a teoria A antes da B”, “Explorar implicações práticas mencionadas por Autor Z no final, para concluir a seção”, “Rever citação de Autor Y, parece destoar do ponto”. Essa lista é passada ao Escritor para retrabalho.
   - Caso exista o agente **Crítico de Argumentos**, ele também passa seu relatório ao Orientador e Escritor – muitas de suas observações podem coincidir com as do Orientador (ex.: sinalizar afirmações sem referência), reforçando tais pontos a corrigir.

7. **Refinamento e Iteração:**

   - O **Engenheiro de Prompt** agora entra ativamente para garantir que a rodada de revisões seja eficiente.
   - Ele pega cada item de feedback do Orientador e traduz em instruções acionáveis para os agentes competentes.
   - Por exemplo: se o Orientador disse para incluir um autor faltante, o Engenheiro formula uma nova tarefa para o Pesquisador (“Buscar referência sobre X, possivelmente do Autor W mencionado”) e para o Revisor (“Analisar rapidamente a nova fonte W e fornecer resumo”).
   - Em seguida, ajusta o prompt do Escritor para “Adicionar no texto da seção tal: comparação entre as definições de X e W, conforme análise fornecida”.
   - Assim, a segunda rodada é conduzida. O Escritor implementa as mudanças e devolve o texto atualizado.
   - O Orientador reavalia apenas os pontos ajustados (ou o todo, se necessário). Pode-se repetir esse ciclo até que o Orientador esteja satisfeito com a qualidade e aderência do referencial teórico.

8. **Finalização:**

   - Uma vez validadas todas as partes, o capítulo de referencial teórico conceitual-descritivo é dado como pronto.
   - O Curador de Base (ou Pesquisador) então pode gerar a lista final de referências formatadas para anexar ao trabalho.
   - Eventualmente, o Editor de Estilo (se houver) faz uma última passada para padronizar termos, conferir ortografia/gramática, mas idealmente o Escritor já cuidou disso.
   - O resultado final é uma narrativa teórica coesa, profundamente embasada nas fontes analisadas e com tratamento crítico na medida adequada, construída de forma colaborativa pelos agentes.

Esse fluxo arquitetural mostra a **orquestração faseada**: primeiro alinhar escopo, depois analisar, depois escrever, depois revisar e iterar. Note que embora apresentemos linearmente, houve pontos de interação (passos 1-2, 4-5, 5-6-7) que tornaram o processo dinâmico. A chave foi usar o Orientador e o Engenheiro de Prompt para sincronizar essas interações sem perder o controle. Cada agente desempenhou seu papel especializado no momento certo, comprovando a eficácia do design multiagente para compor um referencial teórico sólido.
