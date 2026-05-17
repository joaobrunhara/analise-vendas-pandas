import pandas as pd
import matplotlib.pyplot as plt

# 1. LEITURA DOS DADOS: O Pandas agora abre o arquivo CSV real
try:
    df = pd.read_csv('dados_vendas.csv')
    print("[SUCESSO] Arquivo 'dados_vendas.csv' carregado com sucesso!\n")
except FileNotFoundError:
    print("[ERRO] O arquivo 'dados_vendas.csv' não foi encontrado.")
    print("Certifique-se de que ele está na mesma pasta que este script.")
    exit()

# 2. ANÁLISE DE DADOS: Calculando o faturamento de cada linha (Qtd x Preço)
df['Faturamento_Total'] = df['Quantidade'] * df['Preco_Unitario']

print("--- VISUALIZAÇÃO DOS DADOS BRUTOS DO CSV ---")
print(df)
print("-" * 40)

# 3. AGRUPAMENTO: Somando o faturamento por tipo de produto
faturamento_por_produto = df.groupby('Produto')['Faturamento_Total'].sum().sort_values(ascending=False)

print("\n--- RELATÓRIO DE FATURAMENTO POR PRODUTO ---")
print(faturamento_por_produto)
print("-" * 40)
print(f"FATURAMENTO TOTAL DA EMPRESA: R$ {df['Faturamento_Total'].sum():,.2f}")

# 4. DATA VISUALIZATION: Gerando o gráfico para a diretoria
plt.figure(figsize=(10, 6))
faturamento_por_produto.plot(kind='bar', color='royalblue', edgecolor='black')

plt.title('Faturamento Total por Produto - Relatório Mensal', fontsize=14, fontweight='bold')
plt.xlabel('Produtos', fontsize=12)
plt.ylabel('Faturamento em R$', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Salva o gráfico automaticamente como uma imagem profissional
plt.savefig('grafico_faturamento.png')
print("\n[SUCESSO] Gráfico 'grafico_faturamento.png' gerado com sucesso!")

# Mostra o gráfico na tela
plt.show()