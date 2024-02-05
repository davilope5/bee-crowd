# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# Exemplos de Entrada	Exemplos de Saída

# 2.00

# A=12.5664

# 100.64

# A=31819.3103

# 150.00

# A=70685.7750



import math

# Entrada do raio
raio = input("insira seu raio: ")

# Calcula a área
area = int(3.14159 * raio ** 2)

# Imprime o resultado com 4 casas decimais
print("A={:.4f}".format(area))




