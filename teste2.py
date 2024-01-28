# 1 - Para verificar se um número é impar ou par, você pode fazer essa estrutura condicional
numero_inserido = int(input('Insira um numero '))

if numero_inserido % 2 == 0:
        print('O numero eh par')
else:
        print('O numero eh impar')



# 2 - Para fazer as condicionais que informará a idade em categorias, você pode usar essa estrutura:
insira_idade = int(input('Insira a sua idade '))

if 0 < insira_idade <= 12:
        print('Criança')
elif 13 <= insira_idade <= 18:
        print('Adolescente')
elif insira_idade > 18:
        print('Adulto')
else:
        print('Numerop invalido')



# 3 - Para fazer uma condicional que poderá verificar os valores de usuário e senha, você pode utilizar o seguinte código:
insira_usuario = input('Insira um nome de usuario ')
insira_senha = input('Insira a senha ')

if insira_usuario == 'Diego' and insira_senha == 'Diego@2024':
    print('Usuario logado')
else:
    print('Usuario negado')


# 4 - Para verificar onde o ponto está localizado no plano cartesiano, você pode utilizar a seguinte estrutura:
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")





