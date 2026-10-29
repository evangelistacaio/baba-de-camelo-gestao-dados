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