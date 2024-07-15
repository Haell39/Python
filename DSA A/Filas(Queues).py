from collections import deque

# Implementação de uma fila usando deque
fila = deque()

# Adição de elementos (enqueue)
fila.append(1)
fila.append(2)
fila.append(3)
print("Fila após adicionar elementos:", fila)

# Remoção de elementos (dequeue)
print("Elemento removido:", fila.popleft())
print("Fila após remoção:", fila)
