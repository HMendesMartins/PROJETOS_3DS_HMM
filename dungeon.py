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
    portas[1] = rd.randint(1,3)
    portas[2] = rd.randint(4,6)
    escolha = int(input("Escolha 1-???, 2-Monstro ou 3: Saída!\n"))
    if (escolha == 1):
        print("Você entra em uma sala com algo no chão!")
        ch = mapa[portas[2]]
        inventario.append(ch)
        print("Você achou um(a)", ch)
        continue
    elif (escolha == 2):
        if ("espada" in inventario or "cura" in inventario or "armadura" in inventario):
            print("Você sobreviveu!")
            if ("espada" in inventario):
                print("Você derrotou o monstro, mas saiu ferido!\n Gastou uma parte do tesouro para se curar!")    
                inventario.append("tesouro")
            monstroCheck = True
            if ("armadura" in ):

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
            print(inventario.count("tesouro"), "tesouro(s)")
            break