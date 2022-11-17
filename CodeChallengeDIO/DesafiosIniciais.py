# As Duas Torres
def desafio_inicial_um():
    entrada = input('Informe a Distância, Diametro da Primera e Segunda Torre: ').split()

    calculo = int(entrada[0]) / (int(entrada[1]) + int(entrada[2]))
    print(format(calculo, '.2f'))


# Cachorros-Quentes
def desafio_inicial_dois():
    valores = input('Informe a quantidade de participantes e o número de cachorros-quentes: ').split()

    calculo = int(valores[0]) / int(valores[1])
    print(format(calculo, '.2f'))


# Cálculo de viagem
def desafio_inicial_tres():
    valores = input('Informe o tempo da viagem e a velocidade média: ').split()

    litros_km = 12
    velocidade = int(valores[1])
    tempo_viagem = int(valores[0])

    calculo = tempo_viagem * velocidade / litros_km
    print(format(calculo, '.3f'))


# Executa desafios
desafio_inicial_um()
desafio_inicial_dois()
desafio_inicial_tres()