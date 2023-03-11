from random import randrange, seed
import matplotlib.pyplot as plt

seed(10)  # manipula a sequência de números geradas, uma semente = uma seuência

randrange(0, 11, 1)


notas_matematica = []
for notas in range(0, 8, 1):
  # para cada loop uma nota random é adicionada -  total 8 notas
  notas_matematica.append(randrange(0, 11, 1))
print(notas_matematica)
print(len(notas_matematica))


x = list(range(1, 9, 1))
y = notas_matematica


plt.plot(x, y, marker='o')
plt.title('Notas de Matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
