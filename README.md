## 🗄️ Modelagem de Dados (Star Schema)

A tabela bruta gerada nativamente pelo formulário de entrada possui uma estrutura *Wide* (ampla e desnormalizada), ideal para a captação operacional (OLTP), mas ineficiente para processamento em ferramentas de Business Intelligence.

Para solucionar a arquitetura e otimizar o carregamento no BI (OLAP), os dados foram modelados no formato **Star Schema**:

*   **Tabela Fato (`Fato_Fluxo_Caixa`):** Centraliza as métricas financeiras. Registra os valores exatos de entradas (parcelas de cachê) e saídas (cachês individuais de músicos, staff técnico e custos logísticos).
*   **Tabelas Dimensão:**
    *   `Dim_Eventos`: Características qualitativas do show (ID, Contratante, Tipo de Evento).
    *   `Dim_Localidade`: Informações geográficas (Cidade/UF) para análises de praça.
    *   `Dim_Calendario`: Hierarquia de datas para habilitar análises de inteligência temporal (YTD, YoY).
    *   `Dim_Equipe`: Cadastro único de músicos e staff técnico (ID, Nome, Função).

Essa modelagem dimensional elimina a redundância na atualização, garante alta performance no motor de BI e evita problemas de duplicidade de contagem nas agregações financeiras.

## 💼 Regras de Negócio e KPIs

Para garantir a transparência e a correta distribuição financeira entre os membros fundadores e a equipe de apoio do Bloco Baba de Camelo, o banco de dados automatiza as seguintes regras de negócio:

* **Receita Bruta (Cachê):** Valor integral negociado com o contratante para a realização do show.
* **Custos Operacionais (Deduções Diretas):** 
  * Pagamento de cachês fixos para músicos de apoio e equipe técnica (roadies, técnicos de som).
  * Custos logísticos (transporte, alimentação, hospedagem) e taxas de agenciamento/comissionamento.
* **Lucro Líquido (Faturamento Real):** Calculado dinamicamente pela fórmula: `Receita Bruta - Sum(Custos Operacionais + Taxas + Comissões)`.
* **Distribuição de Sócios:** O Lucro Líquido é o montante final que é efetivamente retido em caixa ou dividido entre os sócios do projeto (Caio, Rafael e Nicholas).

Essa lógica garante que os dashboards reflitam a saúde financeira real do projeto, isolando o que é faturamento bruto do que é efetivamente margem de lucro.