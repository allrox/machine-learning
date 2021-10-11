import pandas as pd
uri = "https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv"
dados = pd.read_csv(uri)

# Tornando nomes de coluna mais amigáveis
rename = {
    "unfinished" : "nao_concluido",
    "expected_hours" : "tempo_estimado",
    "price" : "preco"
}

# Aplicação da função rename()
dados = dados.rename(columns = rename)

# Definindo dados x e y
x = dados[["nao_concluido", "tempo_estimado"]]
y = dados["preco"]

# Realizando swap dos valores da coluna nao_concluido para
# criar a coluna finalizado
swap = {
    0 : 1,
    1 : 0
}

# Incluindo a coluna finalizado,
# mais objetiva para análise em comparação à nao_concluido
dados["finalizado"] = dados.nao_concluido.map(swap)

print(dados)

# Importando a bilbioteca de visualização de dados Python baseada em matplotlib
import seaborn as sns
sns.scatterplot(x = "tempo_estimado", y = "preco", hue = "finalizado", data = dados)
sns.relplot(x = "tempo_estimado", y = "preco", hue = "finalizado", col = "finalizado", data = dados)

# Importando a biblioteca matplotlib para exibir o gráfico
import matplotlib.pyplot as plt
plt.show()