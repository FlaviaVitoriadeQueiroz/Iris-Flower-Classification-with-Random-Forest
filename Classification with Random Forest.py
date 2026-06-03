# ATIVIDADE - COMBINAÇÃO DE CLASSIFICADORES
# Técnica utilizada: Random Forest
# Biblioteca: scikit-learn

# Importação das bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns

# CARREGAMENTO DO DATASET
iris = load_iris()

# Variáveis de entrada
X = iris.data

# Variável alvo
y = iris.target

# DIVISÃO DOS DADOS
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# CRIAÇÃO DO MODELO
modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Treinamento
modelo.fit(X_train, y_train)

# Previsões
y_pred = modelo.predict(X_test)

# AVALIAÇÃO DO MODELO

# Acurácia
acuracia = accuracy_score(y_test, y_pred)

print("Acurácia do modelo:", acuracia)

# Relatório de classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)

print("\nMatriz de Confusão:")
print(cm)

# MATRIZ DE CONFUSÃO VISUAL
plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.title('Confusion Matrix - Random Forest')
plt.xlabel('Predicted Class')
plt.ylabel('Actual Class')

plt.show()