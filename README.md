# Gestão de Dados e Engenharia Financeira

## 📌 Sobre o Projeto
Este repositório faz parte de um sistema em desenvolvimento para a gestão financeira, operacional e de shows do **Bloco Baba de Camelo**. O objetivo principal é consolidar, tratar e visualizar os dados de faturamento, custos logísticos e repasses de comissões da produtora.

## 🔒 O Problema de Negócio (Privacidade de Dados)
Para apresentar a engenharia deste projeto em meu portfólio público de Análise de Dados, surgiu um desafio de segurança da informação: **como demonstrar a estrutura da base de dados e os dashboards gerenciais sem expor o faturamento real e a identidade dos clientes (contratantes) da produtora?**

## 💡 A Solução: Pipeline de Anonimização (Python)
Desenvolvi um script em **Python**, utilizando a biblioteca **Pandas**, para atuar como um pipeline de ofuscação (Data Masking). O script (`anonimizacao.py`) realiza as seguintes operações de forma automatizada:

1. **Ingestão:** Lê a base bruta original (Tabela Fato de shows).
2. **Limpeza e Tipagem:** Remove caracteres especiais de formatação monetária (R$, pontos, espaços) e converte as *strings* para decimais flutuantes.
3. **Ofuscação Financeira:** Identifica dinamicamente todas as colunas financeiras utilizando *List Comprehension* e aplica um fator matemático de redução (0.73). Isso mantém a proporcionalidade perfeita para a construção de gráficos no BI, ocultando os valores reais.
4. **Proteção de Identidade:** Sobrescreve a coluna de Contratantes com identificadores genéricos sequenciais (ex: "Contratante 1", "Contratante 2").
5. **Exportação:** Gera um novo arquivo CSV seguro (`dados_anonimizados_portfolio.csv`) para consumo público.

## 🗄️ Modelagem de Dados (Star Schema)
A tabela bruta gerada nativamente pelo formulário de entrada possui uma estrutura *Wide* (ampla e desnormalizada), ideal para a captação operacional (OLTP), mas ineficiente para processamento em ferramentas de Business Intelligence.

Para solucionar a arquitetura e otimizar o carregamento no BI (OLAP), os dados foram modelados no formato **Star Schema**:
- **Tabela Fato (`Fato_Fluxo_Caixa`):** Centraliza as métricas financeiras. Registra os valores exatos de entradas (parcelas de cachê) e saídas (cachês individuais de músicos, staff técnico e custos logísticos).
- **Tabelas Dimensão:**
  - `Dim_Eventos`: Características qualitativas do show (ID, Contratante, Tipo de Evento).
  - `Dim_Localidade`: Informações geográficas (Cidade/UF) para análises de praça.
  - `Dim_Calendario`: Hierarquia de datas para habilitar análises de inteligência temporal (YTD, YoY).
  - `Dim_Equipe`: Cadastro único de músicos e staff técnico (ID, Nome, Função).

Essa modelagem dimensional elimina a redundância na atualização, garante alta performance no motor de BI e evita problemas de duplicidade de contagem nas agregações financeiras.

## 💼 Regras de Negócio e KPIs
Para garantir a transparência e a correta distribuição financeira entre os membros fundadores e a equipe de apoio do Bloco Baba de Camelo, o banco de dados automatiza as seguintes regras de negócio:
- **Receita Bruta (Cachê):** Valor integral negociado com o contratante para a realização do show.
- **Custos Operacionais (Deduções Diretas):** Pagamento de cachês fixos para músicos de apoio e equipe técnica (roadies, técnicos de som), custos logísticos (transporte, alimentação, hospedagem) e taxas de agenciamento/comissionamento.
- **Lucro Líquido (Faturamento Real):** Calculado dinamicamente pela fórmula: `Receita Bruta - Sum(Custos Operacionais + Taxas + Comissões)`.
- **Distribuição de Sócios:** O Lucro Líquido é o montante final que é efetivamente retido em caixa ou dividido entre os sócios do projeto (Caio, Rafael e Nicholas).

## 🛠️ Tecnologias Utilizadas
* **Python & Pandas:** Limpeza, transformação e anonimização de dados.
* **Git/GitHub:** Controle de versão de código.