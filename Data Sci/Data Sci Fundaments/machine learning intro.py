from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregando o dataset de exemplo
iris = load_iris()
X, y = iris.data, iris.target

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando um modelo simples
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Fazendo previsões
predictions = model.predict(X_test)

# Avaliando o modelo
accuracy = accuracy_score(y_test, predictions)
print(f"Acurácia: {accuracy * 100:.2f}%")
