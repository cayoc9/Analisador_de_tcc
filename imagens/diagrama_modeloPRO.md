# Diagrama do Modelo de Orientação de Responsabilidade Pessoal (PRO) de Brockett e Hiemstra

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#f5f5f5',
    'primaryTextColor': '#333',
    'primaryBorderColor': '#aaa',
    'lineColor': '#666',
    'fontSize': '16px'
  }
}}%%

flowchart TB
    subgraph CS["Contexto Social (Socio-político, Educacional e Cultural)" class="contexto"]
        subgraph PRO["Modelo PRO - Orientação de Responsabilidade Pessoal" class="pro-model"]
            RP["Responsabilidade<br/>Pessoal" class="responsabilidade"]

            subgraph Componentes["Dimensões da Autodireção" class="componentes"]
                SDL["Aprendizagem<br/>Autodirigida<br/>(Método instrucional)" class="processo"]
                LS["Autodireção<br/>do Aprendiz<br/>(Característica pessoal)" class="caracteristica"]
            end
        end
    end

    %% Conexões
    RP <--> SDL
    RP <--> LS
    SDL <--> LS

    %% Classificação para estilização
    classDef contexto fill:#E8F4F8,stroke:#5DADE2,stroke-width:2px
    classDef pro-model fill:#FBEEE6,stroke:#DC7633,stroke-width:2px
    classDef responsabilidade fill:#FADBD8,stroke:#EC7063,stroke-width:3px,color:#943126,font-weight:bold
    classDef processo fill:#D4EFDF,stroke:#27AE60,stroke-width:2px
    classDef caracteristica fill:#E8DAEF,stroke:#8E44AD,stroke-width:2px
    classDef componentes fill:#F9F9F9,stroke:#AAB7B8,stroke-width:1px,stroke-dasharray:5
```

## Legenda e Descrição dos Componentes

### 1. Responsabilidade Pessoal

<div style="background-color:#FADBD8; border:2px solid #EC7063; padding:10px; border-radius:5px; margin-bottom:15px;">
<strong>Definição:</strong> O conceito central que representa a capacidade e disposição do indivíduo para assumir controle e propriedade sobre seus pensamentos e ações no processo de aprendizagem.
</div>

### 2. Aprendizagem Autodirigida (Método Instrucional)

<div style="background-color:#D4EFDF; border:2px solid #27AE60; padding:10px; border-radius:5px; margin-bottom:15px;">
<strong>Definição:</strong> O processo externo ao indivíduo, onde o aprendiz assume responsabilidade primária pelo planejamento, implementação e avaliação do processo de aprendizagem, frequentemente com o apoio de um facilitador.
</div>

### 3. Autodireção do Aprendiz (Característica Pessoal)

<div style="background-color:#E8DAEF; border:2px solid #8E44AD; padding:10px; border-radius:5px; margin-bottom:15px;">
<strong>Definição:</strong> As características internas do indivíduo que o predispõem a assumir responsabilidade por sua aprendizagem, incluindo autoconceito, motivação intrínseca, e percepção de si como aprendiz autônomo.
</div>

### 4. Contexto Social

<div style="background-color:#E8F4F8; border:2px solid #5DADE2; padding:10px; border-radius:5px; margin-bottom:15px;">
<strong>Definição:</strong> O ambiente social, político, cultural e educacional mais amplo no qual a autodireção ocorre, reconhecendo que o indivíduo não aprende em um vácuo, mas dentro de um contexto que pode facilitar ou limitar as oportunidades para autodireção.
</div>

## Características-chave do Modelo PRO

- **Natureza integrativa**: Combina aspectos metodológicos e de personalidade da autodireção
- **Responsabilidade pessoal como conceito unificador**: Conecta os componentes do modelo
- **Reconhecimento da importância do contexto**: Situa a autodireção em um ambiente social mais amplo
- **Visão humanística**: Valoriza a capacidade do indivíduo para autodirigir seu desenvolvimento
- **Equilíbrio entre fatores internos e externos**: Considera tanto características do aprendiz quanto aspectos do ambiente de aprendizagem

## Evolução do Modelo PRO

O Modelo PRO, originalmente desenvolvido em 1991, foi posteriormente revisado pelos mesmos autores em 2012, resultando no Modelo PPC (Person-Process-Context). A revisão mantém os elementos essenciais do original, mas reorganiza-os para enfatizar ainda mais a importância do contexto e as interações dinâmicas entre todos os componentes.

Este diagrama representa a versão original do modelo PRO, destacando a centralidade da responsabilidade pessoal e a distinção entre aprendizagem autodirigida como processo instrucional e autodireção do aprendiz como característica pessoal, tudo situado dentro de um contexto social mais amplo.
