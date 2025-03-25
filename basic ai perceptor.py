#basic ai perceptor
# Perceptron je jednoduchý model umělé neuronové sítě, který se používá pro klasifikaci binárních dat.
# Tento model má vstupy, které jsou váženy a sečteny, a na základě výsledku se rozhodne, zda je vstupní data klasifikována jako 0 nebo 1.
# V tomto příkladu implementujeme Perceptron pro AND logickou funkci, která má dva binární vstupy a vrací 1 pouze tehdy, když jsou oba vstupy 1.
# Výstup Perceptronu je porovnán s očekávanými výstupy a váhy jsou upraveny pomocí učení s učitelem.
# Nakonec jsou testována nová vstupní data, aby se ověřilo, zda Perceptron správně klasifikuje AND funkci.

import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=1000):
        self.weights = np.zeros(input_size + 1)  # +1 pro bias
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        x = np.insert(x, 0, 1)  # Přidání biasu
        return self.activation(np.dot(self.weights, x))
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                self.weights += self.learning_rate * (label - prediction) * np.insert(inputs, 0, 1)

# Testovací data (AND logická funkce)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_size=2)
perceptron.train(X, y)

# Testování predikce
for x in X:
    print(f'Input: {x}, Output: {perceptron.predict(x)}')
