# Para criar as listas, podemos utilizar as seguintes variáveis:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Diego', 'Maju', 'Amanda', 'Flok']
ano_nascimento = [1994, 2024]


# Para percorrer todos os itens de uma lista com o loop for, você pode usar essa estrutura:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

print('Lista Percorrida')


# Para fazer calcular a soma dos números impares de 1 a 10, você pode utilizar o seguinte código:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_impares = 0

for numero in numeros:
    if numero % 2 == 1:
        soma_impares += numero

print('Essa eh a soma de numeros impares', soma_impares)



# Para imprimir os números de 1 a 10 de forma decrescente, você pode utilizar a seguinte estrutura:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in reversed(numeros):
    print(numero)



# Para fazer uma tabuada interativa, você pode seguir o seguinte código:
numero = int(input("Digite um número para a tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")



# Uma possível resolução para fazer a soma dos elementos de uma lista com for e usar try except para validar, está no código a seguir:
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")




# Um modo de solucionar essa questão com uma validação de lista vazia é do seguinte modo:
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")