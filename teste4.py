# 1 - Para criar um dicionário com informações de uma pessoa, você pode utilizar a seguinte solução:
pessoa = {'nome':'Diego', 'idade':'29', 'cidade':'osasco'}

# 2 - Para fazer a atualização de um valor, adicionar um item e remover uma informação, você pode usar o seguinte raciocínio:
pessoa['idade'] = 31
pessoa['profissao'] = 'Engenheiro'
del pessoa['cidade']




# 3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)



#4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")
    
    
    
    
 
 
   
# 5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:  
# Definindo a frase
frase = "O rato roeu a roupa do rei de Roma"

# Dividindo a frase em palavras
palavras = frase.split()

# Inicializando o dicionário para armazenar as frequências
frequencia = {}

# Contando a frequência de cada palavra
for palavra in palavras:
    # Se a palavra já estiver no dicionário, incrementa a contagem
    if palavra in frequencia:
        frequencia[palavra] += 1
    # Se não, adiciona a palavra ao dicionário com contagem inicial 1
    else:
        frequencia[palavra] = 1

# Exibindo a frequência de cada palavra
for palavra, freq in frequencia.items():
    print(f"A palavra '{palavra}' aparece {freq} vez(es) na frase.")