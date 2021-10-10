# Pergunta: É um porco?
# Classificação das Features ( 0 = não, 1 = sim )
# Pêlos longos?
# Pernas curtas?
# Late?

print("Pergunta: É um porco?\n- Classificação das Features ( 0 = não, 1 = sim )\n- Pêlos longos?\n- Pernas curtas?\n- Late?\n")

# Declaração de um grupo
# de indivíduos da classe porcos
porco1 = [ 0, 1, 0 ]
porco2 = [ 0, 1, 1 ]
porco3 = [ 1, 1, 0 ]

# Declaração de um grupo
# de indivíduos da classe cachorros
cachorro1 = [ 0, 1, 1 ]
cachorro2 = [ 1, 0, 1 ]
cachorro3 = [ 1, 1, 1 ]

train_x = [ porco1, porco2, porco3, cachorro1, cachorro2, cachorro3 ]
train_y = [ 1, 1, 1, 0, 0, 0, ]

# Importando o algoritmo de classificação LinearSVC
# a partir da biblioteca SKlearn - scikit-learn
# Linear Support Vector Classification
from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit(train_x, train_y)

# Testando o modelo com um novo objeto
animal_misterioso = [ 1, 1, 1 ]

print("Aqui foi informado um animal não-classificado com os parâmetros [ 1, 1, 1]")

# Estrutura condicional para imprimir o resultado em texto
if (model.predict([animal_misterioso]) == 0):
    print("O objeto da análise não é um porco\n")
else:
    print("O objeto da análise é um porco\n")

# Novo teste com mais elementos
animal1 = [ 1, 1, 1 ]
animal2 = [ 1, 1, 0 ]
animal3 = [ 0, 1, 1 ]

teste_x = [ animal1, animal2, animal3 ]
teste_y = [ 0, 1, 1 ]
previsoes = model.predict(teste_x)

# Calculando a taxa de acerto
acertos = ( previsoes == teste_y ).sum()
total = len(teste_x)
tx_acerto = ( acertos/total )
print("Cálculo ""manual"" da Taxa de acerto:",round(tx_acerto*100,2),"%")

from sklearn.metrics import accuracy_score
tx_acerto = accuracy_score(teste_y, previsoes)
print("Cálculo da taxa de acerto com ""accuracy_score"":",round(tx_acerto*100,2),"%")