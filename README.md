# Iris Flower Classification with Random Forest

🇧🇷 Português | 🇺🇸 English

---

# 🇧🇷 Português

## Sobre o Projeto

Este projeto aplica técnicas de Machine Learning para classificar flores do conjunto de dados Iris utilizando o algoritmo Random Forest.

O objetivo é prever a espécie da flor com base em medidas morfológicas, demonstrando a aplicação de métodos de classificação supervisionada e técnicas de Ensemble Learning.

---

## Objetivo

Desenvolver um classificador capaz de identificar a espécie de uma flor Iris a partir de características físicas.

As espécies presentes no dataset são:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## Dataset

Foi utilizado o famoso Iris Dataset, amplamente empregado em estudos introdutórios de Machine Learning e classificação supervisionada.

### Variáveis Utilizadas

| Variável     | Descrição             |
| ------------ | --------------------- |
| Sepal Length | Comprimento da sépala |
| Sepal Width  | Largura da sépala     |
| Petal Length | Comprimento da pétala |
| Petal Width  | Largura da pétala     |

### Variável Alvo

| Variável | Descrição       |
| -------- | --------------- |
| Species  | Espécie da flor |

---

## Modelo Utilizado

### Random Forest

O Random Forest é um algoritmo de Ensemble Learning que combina múltiplas Árvores de Decisão para produzir previsões mais robustas e precisas.

Principais vantagens:

* Redução de overfitting;
* Maior capacidade de generalização;
* Melhor desempenho em comparação a uma única árvore de decisão.

---

## Divisão dos Dados

Os dados foram divididos em:

* 70% para treinamento;
* 30% para teste.

A divisão foi realizada utilizando a função `train_test_split()` do Scikit-Learn.

---

## Avaliação do Modelo

Foram utilizadas as seguintes métricas:

### Accuracy

Mede a proporção de previsões corretas realizadas pelo modelo.

### Classification Report

Apresenta métricas como:

* Precision
* Recall
* F1-Score

para cada classe.

### Confusion Matrix

Permite visualizar os acertos e erros de classificação para cada espécie.

---

## Visualização

O projeto inclui uma matriz de confusão visual utilizando:

* Matplotlib
* Seaborn

facilitando a interpretação dos resultados do modelo.

---

## Conclusão

O Random Forest demonstrou excelente desempenho na classificação das espécies de Iris, mostrando a eficácia das técnicas de Ensemble Learning para problemas de classificação supervisionada.

Além de apresentar alta acurácia, o modelo mostrou boa capacidade de generalização nos dados de teste.

---

# 🇺🇸 English

## About the Project

This project applies Machine Learning techniques to classify Iris flowers using the Random Forest algorithm.

The objective is to predict the flower species based on morphological measurements while demonstrating supervised classification and Ensemble Learning concepts.

---

## Objective

Build a classifier capable of identifying Iris flower species using physical measurements.

The dataset contains three classes:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## Dataset

The project uses the famous Iris Dataset, one of the most widely used datasets for introductory Machine Learning and classification tasks.

### Features

| Feature      | Description         |
| ------------ | ------------------- |
| Sepal Length | Length of the sepal |
| Sepal Width  | Width of the sepal  |
| Petal Length | Length of the petal |
| Petal Width  | Width of the petal  |

### Target Variable

| Variable | Description    |
| -------- | -------------- |
| Species  | Flower species |

---

## Model

### Random Forest

Random Forest is an Ensemble Learning algorithm that combines multiple Decision Trees to improve prediction accuracy and robustness.

Main advantages:

* Reduced overfitting;
* Better generalization;
* Higher predictive performance than a single decision tree.

---

## Data Split

The dataset was divided into:

* 70% training data;
* 30% testing data.

The split was performed using Scikit-Learn's `train_test_split()` function.

---

## Model Evaluation

The model was evaluated using:

### Accuracy

Measures the proportion of correct predictions.

### Classification Report

Provides:

* Precision
* Recall
* F1-Score

for each class.

### Confusion Matrix

Displays the classification performance for each species.

---

## Visualization

A confusion matrix heatmap was generated using:

* Matplotlib
* Seaborn

to improve result interpretation.

---

## Conclusion

The Random Forest classifier achieved excellent performance on the Iris dataset, demonstrating the effectiveness of Ensemble Learning techniques for supervised classification problems.

The model achieved high accuracy and strong generalization on unseen data.

---

## 🛠️ Technologies

* Python
* Scikit-Learn
* NumPy
* Matplotlib
* Seaborn

---

## Author

Flávia Vitória de Queiroz

