import pandas as pd

arquivo_entrada = "Baba de Camelo - Gestão Financeira e Balanço - Visão Cronológica.csv"
df = pd.read_csv(arquivo_entrada)

fator_ofuscacao = 0.73

# Encontra automaticamente todas as colunas que envolvem dinheiro
colunas_financeiras = [col for col in df.columns if '(R$)' in col or col in ['Custo Total', 'Lucro Líquido', 'Impostos / Taxas (NF, Ecad)']]

for coluna in colunas_financeiras:
    # Preenche células vazias (como parcelas não utilizadas) com '0'
    df[coluna] = df[coluna].fillna('0')
    
    # Remove formatações de moeda e converte para decimal
    df[coluna] = df[coluna].astype(str).replace(r'[R\$\.\s]', '', regex=True).replace(',', '.', regex=True).astype(float)
    
    # Multiplica pelo fator de segurança
    df[coluna] = (df[coluna] * fator_ofuscacao).round(2)

# Anonimiza o nome do contratante
if 'Nome do Evento / Contratante' in df.columns:
    df['Nome do Evento / Contratante'] = ['Contratante ' + str(i+1) for i in range(len(df))]

arquivo_saida = "dados_anonimizados_portfolio.csv"
df.to_csv(arquivo_saida, index=False)

print("Sucesso! Todas as colunas financeiras foram ajustadas proporcionalmente.")