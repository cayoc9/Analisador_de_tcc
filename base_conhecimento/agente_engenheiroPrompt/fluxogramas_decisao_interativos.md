# Fluxogramas de Decisão Interativos para Engenharia de Prompts

Este documento apresenta fluxogramas de decisão estruturados para orientar a seleção e aplicação de técnicas de engenharia de prompts em contextos de pesquisa científica, com foco especial na aprendizagem autodirigida.

## 1. Fluxograma Mestre de Seleção de Técnicas

### 1.1 Diagrama Principal

```
┌─────────────────┐
│  INÍCIO         │
└────────┬────────┘
         │
         ▼
┌────────────────┐      ┌──────────────────┐
│Qual o objetivo │ Sim  │Use técnicas      │
│principal é     ├─────►│Zero-Shot ou      │
│exploração      │      │Few-Shot básicas  │
│inicial?        │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│A tarefa requer │ Sim  │Use Chain-of-     │
│raciocínio      ├─────►│Thought ou        │
│estruturado     │      │Self-Consistency  │
│passo a passo?  │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│É necessário    │ Sim  │Use Tree of       │
│explorar        ├─────►│Thoughts ou       │
│múltiplas       │      │Active Prompting  │
│perspectivas?   │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Há necessidade  │ Sim  │Use RAG ou        │
│de fundamentação├─────►│técnicas de       │
│em conhecimento │      │Retrieval         │
│específico?     │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│A tarefa é      │ Sim  │Combine técnicas: │
│complexa,       ├─────►│RAG+CoT,          │
│requerendo      │      │ToT+Self-Consist. │
│múltiplas       │      │ou Role+Few-Shot  │
│habilidades?    │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐
│Retorne ao      │
│início e        │
│reavalie os     │
│requisitos      │
└────────────────┘
```

### 1.2 Tabela de Decisão Complementar

| Condição                                 | Técnica Recomendada | Quando Evitar                                     |
| ---------------------------------------- | ------------------- | ------------------------------------------------- |
| Instruções simples e diretas             | Zero-Shot           | Tarefas complexas ou ambíguas                     |
| Necessidade de exemplificar padrões      | Few-Shot            | Quando exemplos podem limitar a criatividade      |
| Problemas que requerem passos explícitos | Chain-of-Thought    | Quando o processo é intuitivo ou não decomponível |
| Comparação entre alternativas            | Tree of Thoughts    | Quando há restrições significativas de token      |
| Incorporação de conhecimento específico  | RAG                 | Quando o conhecimento já está no modelo           |
| Verificação de consistência              | Self-Consistency    | Quando a variabilidade de respostas é desejável   |

## 2. Fluxograma para Seleção por Fase de Pesquisa

### 2.1 Fase de Revisão de Literatura

```
┌─────────────────┐
│  REVISÃO DE     │
│  LITERATURA     │
└────────┬────────┘
         │
         ▼
┌────────────────┐      ┌──────────────────┐
│Está iniciando  │ Sim  │Few-Shot + RAG    │
│a pesquisa      ├─────►│para fichamento   │
│bibliográfica?  │      │estruturado       │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está analisando │ Sim  │CoT + Role para   │
│metodologias    ├─────►│análise crítica   │
│de estudos?     │      │de design         │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está comparando │ Sim  │ToT + Self-       │
│diferentes      ├─────►│Consistency       │
│perspectivas    │      │para triangulação │
│teóricas?       │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está realizando │ Sim  │RAG + CoT para    │
│síntese         ├─────►│integração        │
│integrativa     │      │conceitual        │
│da literatura?  │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐
│Consulte o      │
│fluxograma      │
│específico para │
│sua fase atual  │
└────────────────┘
```

### 2.2 Fase de Contextualização para SDL

```
┌─────────────────┐
│CONTEXTUALIZAÇÃO │
│PARA SDL         │
└────────┬────────┘
         │
         ▼
┌────────────────┐      ┌──────────────────┐
│Está mapeando   │ Sim  │Zero-Shot + RAG   │
│elementos       ├─────►│com conhecimento  │
│fundamentais    │      │contextual de SDL │
│de SDL?         │      └──────────────────┘
└────────┬───────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está adaptando  │ Sim  │RAG + Role com    │
│conceitos ao    ├─────►│perspectiva de    │
│contexto        │      │educador          │
│brasileiro?     │      │brasileiro        │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está analisando │ Sim  │ToT + Role com    │
│aplicações em   ├─────►│múltiplas         │
│computação?     │      │perspectivas      │
└────────┬───────┘      │disciplinares     │
         │              └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está            │ Sim  │CoT + Self-       │
│desenvolvendo   ├─────►│Consistency para  │
│framework       │      │validação         │
│contextualizado?│      │metodológica      │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐
│Consulte o      │
│especialista em │
│engenharia de   │
│prompts para SDL│
└────────────────┘
```

## 3. Fluxograma para Seleção por Tipo de Material

### 3.1 Análise de Artigos Científicos

```
┌─────────────────┐
│  ANÁLISE DE     │
│  ARTIGOS        │
└────────┬────────┘
         │
         ▼
┌────────────────┐
│Qual o tipo     │
│de artigo?      │
└┬───────────┬───┘
 │           │
 ▼           ▼
┌────────────┐ ┌────────────┐
│Empírico    │ │Teórico/    │
│            │ │Conceitual  │
└────┬───────┘ └─────┬──────┘
     │               │
     ▼               ▼
┌────────────┐ ┌────────────┐
│CoT + Role  │ │ToT + Self- │
│para análise│ │Consistency │
│metodológica│ │para análise│
│            │ │conceitual  │
└────┬───────┘ └─────┬──────┘
     │               │
     ▼               ▼
┌────────────┐ ┌────────────┐
│Template    │ │Template    │
│A.2.1 com   │ │A.2.2 com   │
│F.1.1 para  │ │F.1.2 para  │
│validação   │ │validação   │
└────────────┘ └────────────┘
```

### 3.2 Análise de Documentos Institucionais

```
┌─────────────────┐
│  ANÁLISE DE     │
│  DOCUMENTOS     │
└────────┬────────┘
         │
         ▼
┌────────────────┐      ┌──────────────────┐
│É um documento  │ Sim  │RAG + Zero-Shot   │
│curricular      ├─────►│com Template A.2.4│
│(PPC, DCN)?     │      │                  │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│É uma política  │ Sim  │RAG + Role com    │
│educacional     ├─────►│perspectiva de    │
│ou normativa?   │      │especialista em   │
└────────┬───────┘      │políticas         │
         │              └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│É um relatório  │ Sim  │CoT + RAG para    │
│técnico ou      ├─────►│análise estruturada│
│institucional?  │      │de dados           │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐
│Use Template    │
│A.2.4 adaptado  │
│ao tipo de      │
│documento       │
└────────────────┘
```

## 4. Fluxograma para Validação Científica

```
┌─────────────────┐
│  VALIDAÇÃO      │
│  CIENTÍFICA     │
└────────┬────────┘
         │
         ▼
┌────────────────┐      ┌──────────────────┐
│Está validando  │ Sim  │Aplicar F.1.1     │
│precisão factual├─────►│(Dimensões de     │
│do conteúdo?    │      │Validação) com    │
└────────┬───────┘      │CoT               │
         │              └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está verificando│ Sim  │Aplicar F.1.2     │
│integridade     ├─────►│(Procedimentos    │
│metodológica?   │      │Preventivos)      │
└────────┬───────┘      │com Self-         │
         │              │Consistency       │
         │              └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está avaliando  │ Sim  │Aplicar F.1.3     │
│objetividade e  ├─────►│(Matrizes de      │
│equilíbrio?     │      │Validação) com    │
└────────┬───────┘      │ToT               │
         │              └──────────────────┘
         │ Não
         ▼
┌────────────────┐      ┌──────────────────┐
│Está verificando│ Sim  │Aplicar Framework │
│relevância      ├─────►│Contextualizado   │
│contextual?     │      │(F.2.1) com RAG   │
└────────┬───────┘      └──────────────────┘
         │ Não
         ▼
┌────────────────┐
│Combine aspectos│
│relevantes dos  │
│frameworks de   │
│validação       │
└────────────────┘
```

## 5. Fluxograma para Desenvolvimento de Prompts Personalizados

```
┌─────────────────┐
│DESENVOLVIMENTO  │
│DE PROMPTS       │
└────────┬────────┘
         │
         ▼
┌────────────────┐
│Defina o        │
│objetivo        │
│principal do    │
│prompt          │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│Selecione os    │
│princípios      │
│estruturais     │
│aplicáveis:     │
└┬──────┬──────┬─┘
 │      │      │
 ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐
│P.1   ││P.2   ││P.3   │
│Clareza││Estrut││Rigor │
│      ││Formal││Cient.│
└──┬───┘└───┬──┘└───┬──┘
   │        │       │
   └────────┼───────┘
            ▼
┌────────────────┐
│Selecione       │
│técnicas        │
│compatíveis     │
│(consulte       │
│fluxograma 1)   │
└────────┬───────┘
         │
         ▼
┌────────────────┐     ┌───────────────┐
│Defina formato  │     │• Contexto     │
│de saída e      │────►│• Instrução    │
│estrutura do    │     │• Formato      │
│prompt          │     │• Validação    │
└────────┬───────┘     └───────────────┘
         │
         ▼
┌────────────────┐
│Incorpore       │
│mecanismo de    │
│validação       │
│(Framework F.1) │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│Teste, refine   │
│e documente o   │
│prompt final    │
└────────────────┘
```

## 6. Sistema de Navegação Interativa

### 6.1 Instruções de Uso do Sistema

Para utilizar estes fluxogramas de forma interativa:

1. **Ponto de Entrada**:

   - Inicie pelo Fluxograma Mestre (Seção 1) se não tiver certeza por onde começar
   - Vá diretamente ao fluxograma específico se já souber sua fase ou tipo de material

2. **Navegação entre Fluxogramas**:

   - Cada decisão terminal geralmente aponta para técnicas específicas e templates
   - Use os códigos de referência (ex: T.1.2, A.2.1, F.1.3) para acessar recursos relacionados

3. **Refinamento Iterativo**:
   - Os fluxogramas são pontos de partida, não caminhos rígidos
   - Combine recomendações de diferentes fluxogramas quando necessário
   - Refine iterativamente suas escolhas com base nos resultados

### 6.2 Tabela de Referência Rápida

| Situação                            | Fluxograma Recomendado              | Seção |
| ----------------------------------- | ----------------------------------- | ----- |
| Não sei qual técnica usar           | Fluxograma Mestre                   | 1.1   |
| Estou fazendo revisão de literatura | Fluxograma de Revisão               | 2.1   |
| Estou contextualizando SDL          | Fluxograma de Contextualização      | 2.2   |
| Estou analisando artigos            | Fluxograma de Análise de Artigos    | 3.1   |
| Estou analisando documentos         | Fluxograma de Análise de Documentos | 3.2   |
| Preciso validar conteúdo científico | Fluxograma de Validação             | 4     |
| Quero criar prompts personalizados  | Fluxograma de Desenvolvimento       | 5     |

## 7. Implementação de Interatividade

### 7.1 Funcionalidades Interativas Propostas

Para implementação digital destes fluxogramas, as seguintes funcionalidades são recomendadas:

1. **Navegação Clicável**:

   - Cada nó de decisão serve como hyperlink para a próxima etapa
   - Códigos de referência linkam diretamente ao recurso correspondente

2. **Estado Persistente**:

   - Salvamento de progresso no fluxograma
   - Histórico de decisões tomadas

3. **Recomendações Adaptativas**:

   - Ajuste dinâmico das recomendações com base em escolhas anteriores
   - Sugestões contextuais baseadas no perfil do usuário

4. **Visualização de Recursos**:

   - Prévia de templates e técnicas recomendadas
   - Exemplos contextualmente relevantes

5. **Assistência Inteligente**:
   - Sugestões de caminhos alternativos
   - Detecção de padrões de uso e recomendações personalizadas

### 7.2 Especificação Técnica para Implementação

```json
{
  "fluxograma_id": "master_selection",
  "nós": [
    {
      "id": "start",
      "tipo": "início",
      "texto": "INÍCIO",
      "próximo": "objetivo_exploracao"
    },
    {
      "id": "objetivo_exploracao",
      "tipo": "decisão",
      "pergunta": "Qual o objetivo principal é exploração inicial?",
      "opções": [
        { "texto": "Sim", "destino": "tecnica_zeroshot_fewshot" },
        { "texto": "Não", "destino": "tarefa_raciocinio" }
      ]
    },
    {
      "id": "tecnica_zeroshot_fewshot",
      "tipo": "recomendação",
      "texto": "Use técnicas Zero-Shot ou Few-Shot básicas",
      "recursos": ["T.1.1", "T.1.2"],
      "exemplos": ["exemplo_zeroshot_SDL.md"]
    }
    // ... outros nós
  ],
  "integração": {
    "sistema_indexação": "api/indexacao/busca",
    "interfaces_visuais": "api/visualizacao/mapa"
  }
}
```

## 8. Casos de Uso Demonstrativos

### 8.1 Caso de Uso: Análise de Artigo Empírico sobre SDL

**Contexto**: Pesquisador precisa analisar criticamente um artigo empírico sobre aprendizagem autodirigida em estudantes de computação.

**Caminho no Fluxograma**:

1. Início → Fluxograma para Seleção por Tipo de Material
2. Análise de Artigos → Artigo Empírico
3. Recomendação: CoT + Role para análise metodológica
4. Aplicação do Template A.2.1 com Framework F.1.1 para validação

**Resultado**: Análise estruturada que avalia rigorosamente o design metodológico, amostragem, instrumentos, análise de dados e validade dos resultados, com comentários contextualizados para o cenário brasileiro.

### 8.2 Caso de Uso: Contextualização de Framework de SDL

**Contexto**: Pesquisador precisa adaptar um framework internacional de SDL para o contexto do ensino superior brasileiro em computação.

**Caminho no Fluxograma**:

1. Início → Fluxograma para Contextualização para SDL
2. Adaptando conceitos ao contexto brasileiro → Sim
3. Recomendação: RAG + Role com perspectiva de educador brasileiro
4. Aplicação do Framework Contextualizado (F.2.1)

**Resultado**: Framework adaptado que considera particularidades do sistema educacional brasileiro, infraestrutura tecnológica disponível e aspectos socioculturais relevantes para implementação de SDL em cursos de computação.

## 9. Metadados do Documento

**Versão**: 1.0  
**Data de Criação**: Março/2024  
**Última Atualização**: Março/2024  
**Compatibilidade**: Implementável em ambientes digitais interativos  
**Integração**: Sistema de indexação, interfaces visuais de navegação  
**Próximas Atualizações**: Expansão de casos específicos, integração com sistema de feedback adaptativo
