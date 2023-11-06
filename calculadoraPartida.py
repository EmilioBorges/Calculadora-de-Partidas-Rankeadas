nome = ""

nivel = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal"]

def classificacao(vitoria, derrota):
    
    return vitoria - derrota

vitoria = int(input("Digite o numero de vitorias: "))
derrota = int(input("Digite o numero de derrotas: "))

saldoVitorias = classificacao(vitoria,derrota)

while True:
    nome = str(input("Digite o nome do Herói: "))
    
    if saldoVitorias <= 10:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[0]}')
        break
    elif saldoVitorias >= 11 and saldoVitorias <= 20:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[1]}')
        break
    elif saldoVitorias >= 21 and saldoVitorias <= 50:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[2]}')
        break
    elif saldoVitorias >= 51 and saldoVitorias <= 80:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[3]}')
        break
    elif saldoVitorias >= 81 and saldoVitorias <= 90:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[4]}')
        break
    elif saldoVitorias >= 91 and saldoVitorias <= 100:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[5]}')
        break
    elif saldoVitorias >= 101:
        print(f'O Herói {nome} de saldo de {saldoVitorias} está no nível de {nivel[6]}')
        break
else:
    print("Jogo Finalizado")