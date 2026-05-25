import random as rd
monstroCheck = bool(False)
mapa = {
    1:"monstro",
    2:"saida",
    3:"tesouro",
    4:"espada",
    5:"cura",
    6:"armadura"
}
inventario = []
portas = [0,0,0]
while True:
    portas.append(inventario)
    portas[1] = rd.randint(1,6)
    portas[2] = rd.randint(1,6)
    escolha = int(input("Escolha 1-???, 2-Monstro ou 3: Saída!"))
    if (escolha == 1):
        print("Você entra em uma sala cheia de portas!")
        escolhaPorta = int(input("1-?? 2-?? 3-?? \nEscolha uma: "))
        escolhaPorta =+3
        if escolhaPorta == 4:
            inventario.append("espada")
            print("Voce acha uma espada e volta ao centro.")
        elif escolhaPorta == 5:
            inventario.append("cura")
            print("Voce acha uma cura e volta ao centro.")
        elif escolhaPorta == 6:
            inventario.append("armadura")
            print("Voce acha uma armadura e volta ao centro.")
        continue
    elif (escolha == 2):
        if ("espada" in inventario or "cura" in inventario or "armadura" in inventario):
            print("Você sobreviveu!")
            inventario.append("tesouro")
            monstroCheck = True
            continue
        else:
            print("GAME OVER")
            break
    elif (escolha == 3):
        if (monstroCheck == False):
            print("Por que veio à dungeon? Faça alguma coisa antes de sair!")
            continue
        else:
            print("Você venceu com ", end="")
            print(inventario.count["tesouro"])
            break