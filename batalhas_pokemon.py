import os
import time
import random 

os.system("cls")


#Entrada
print("____________________________")
print()
print("“Saudações, jovem treinador! Eu sou o Professor Guilherme, e é uma honra apresentar a você o vasto e vibrante mundo dos Pokémon. Aqui, coragem e estratégia caminham lado a lado, e cada batalha é uma chance de crescer. Muitos treinadores lendários começaram exatamente onde você está agora… e alguns até receberam seu primeiro Pokémon comigo. Agora é sua vez! Levante-se, escolha seu parceiro e avance rumo ao topo!”")
print("____________________________")
time.sleep(8)
print()
nome = input("Digite seu nome:")
print("________________________")
print()
time.sleep(2)
print(f"{nome}...É um belo nome!")
print("__________________________")
while True:
    print()
    pronto = input(f"Muito bem {nome}, já está pronto pra começar?:")
    
    if pronto in ["Sim","sim","s","S","SIM","SIm","sIM","siM"]:
        print()
        print(f"Então vamos começar {nome}!")
        time.sleep(2)
        break
    if pronto in ["Não", "não","n","N","NÂO","NÂo","NãO","nãO","Nao","nAo"]:
        print()
        print("Tudo bem, nem toda jornada se inicia com uma decisão, mas sim com seu tempo. Esteja pronto quando quiser!")
    else:
        print("Escreva as opções Sim ou Não!")
    time.sleep(4)
print()
#_______________
print("_________________________________________")
print()
print("Em sua visão, há três pokebolas com nomes diferentes e cada uma é destacada por uma cor. Na primeira pokebola á esquerda, representada por uma cor mais escura em um tom azulado cinzento, destacado a parte superior em uma parte vermelha, com um nome Gible. Na pokebola ao meio, destaca-se uma pokebola azulada com detalhes negros a parte central da pokebola, que condiz com um nome, Riolu. E por fim, ao lado direito, uma pokebola em tom esverdeado, onde aparenta estar desgastada, mas que atenta os corajosos, um Larvitar.")
print("________________________________________")
print()
time.sleep(15)
print(f"""- E então, qual você escolhe {nome}?
      Perguntava o professor, ansioso por sua resposta.""")
print("_________________________________________")
while True:
    print("Você os observa cada Pokémon sair das Pokebolas, todos felizes em te ver e esperam pacientemente para que você os escolha.")
    print("""Eis suas descrições:
          [1] Gible - Pokémon tipo Dragão e Terrestre
          [2] Riolu - Pokémon tipo Lutador
          [3] Larvitar - Pokémon tipo Pedra e Terrestre""")
    
    pokemon = input("Qual será sua escolha?:")
    
    if pokemon in ["Gible", "Riolu", "Larvitar"]:
        print(f"O pokemon escolhido foi {pokemon}")
        break
    else:
        print("""Opção inválida, selecione:
[1] - Gible
[2] - Riolu
[3] - Larvitar""")
#__________________

print(f"-----Você anda tranquilamente com seu parceiro {pokemon} pela floresta, em busca de se aventurar em um mundo novo onde os limites são sua imaginação..Está na hora de andar agora!---")
rotas = 1
for rotas in range(1,6):
    print(f"Passando pela rota {rotas}..")
    rotas = rotas+1
    time.sleep(1)

print("Parece que a grama acabou de se mexer!")

#Encontro!

criatura_selvagem = ["Ratata" , "Pidgey" , "Caterpie" , "Pikachu"] 
selecionada = random.choice (criatura_selvagem)

print(f"Um Pokémon acaba de sair do gramado! É um {selecionada}!")
print()
time.sleep(5)
print(f"{selecionada}:{selecionada}!")
print()
time.sleep(2)
print(f"{selecionada} então nervoso, começava a se demonstrar em sua forma de ataque..")
print()
time.sleep(3)
print(f"Mas de maneira corajosa, seu parceiro {pokemon} entra em sua frente, pronto para te defender e batalhar!")
print()

#Batalha!

hp = random.choice([15, 30, 20, 50, 70])
jogador = 50

print(f"{selecionada} pronto para combate!")
print()
time.sleep(2)

print(f"{nome} solta {pokemon} para a jogada!")
print()
time.sleep(2)
print(f"{selecionada} HP:{hp}")
print()
time.sleep(2)
print(f"{pokemon} HP:{jogador}")
print()

#__________ SISTEMA DE COMBATE __________

# Tipos de cada Pokémon
tipos_pokemon = {
    "Gible": ["Dragão", "Terrestre"],
    "Riolu": ["Lutador"],
    "Larvitar": ["Pedra", "Terrestre"],
    "Ratata": ["Normal"],
    "Pidgey": ["Normal", "Voador"],
    "Caterpie": ["Inseto"],
    "Pikachu": ["Elétrico"],
}

# Tabela de tipos: atacante -> {defensor: multiplicador}
tabela_tipos = {
    "Normal":    {"Pedra": 0.5},
    "Lutador":   {"Normal": 2, "Pedra": 2, "Voador": 0.5, "Inseto": 0.5},
    "Dragão":    {"Dragão": 2},
    "Terrestre": {"Elétrico": 2, "Pedra": 2, "Voador": 0, "Inseto": 0.5},
    "Pedra":     {"Voador": 2, "Inseto": 2, "Lutador": 0.5, "Terrestre": 0.5},
    "Elétrico":  {"Voador": 2, "Terrestre": 0, "Dragão": 0.5, "Elétrico": 0.5},
    "Voador":    {"Lutador": 2, "Inseto": 2, "Pedra": 0.5, "Elétrico": 0.5},
    "Inseto":    {"Lutador": 0.5, "Voador": 0.5},
}

# Golpes: (nome, tipo, poder, nível necessário)
golpes_pokemon = {
    "Gible":    [("Investida", "Normal", 10, 1), ("Garra de Dragão", "Dragão", 14, 1), ("Tremor", "Terrestre", 16, 3)],
    "Riolu":    [("Investida", "Normal", 10, 1), ("Soco Focado", "Lutador", 15, 1), ("Palma Aérea", "Voador", 17, 3)],
    "Larvitar": [("Investida", "Normal", 10, 1), ("Pedrada", "Pedra", 14, 1), ("Tremor", "Terrestre", 16, 3)],
}
golpes_selvagem = {
    "Ratata":   ("Mordida", "Normal", 9),
    "Pidgey":   ("Ataque de Asa", "Voador", 10),
    "Caterpie": ("Investida", "Normal", 8),
    "Pikachu":  ("Choque do Trovão", "Elétrico", 12),
}

# Status do jogador e do selvagem
hp_max = hp
jogador_max = jogador
nivel = 1
xp = 0
pocoes = 3
pokebolas = 3
nivel_selvagem = 1

def multiplicador(tipo_golpe, tipos_defensor):
    mult = 1
    for t in tipos_defensor:
        mult = mult * tabela_tipos[tipo_golpe].get(t, 1)
    return mult

def calcular_dano(poder, tipo_golpe, nivel_atacante, tipos_defensor):
    mult = multiplicador(tipo_golpe, tipos_defensor)
    dano = int((poder + nivel_atacante * 2) * mult * random.uniform(0.85, 1.15))
    if mult > 0:
        dano = max(1, dano)
    return dano, mult

def efetividade(mult):
    if mult == 0:
        return "Não afeta o alvo..."
    if mult > 1:
        return "É super efetivo!"
    if mult < 1:
        return "Não é muito efetivo..."
    return ""

def escolher_golpe():
    # Retorna o golpe escolhido, ou None para VOLTAR à ação
    disponiveis = [g for g in golpes_pokemon[pokemon] if g[3] <= nivel]
    print()
    for i, g in enumerate(disponiveis, start=1):
        print(f"[{i}] {g[0]} ({g[1]}, poder {g[2]})")
    print("[0] Voltar")
    while True:
        escolha = input("Qual golpe?:")
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            return disponiveis[int(escolha) - 1]
        print("Opção inválida!")

def usar_cura(hp_atual, hp_limite, qtd):
    # Retorna (novo_hp, nova_qtd, usou)
    if qtd <= 0:
        print("Você não tem mais poções!")
        return hp_atual, qtd, False
    if hp_atual >= hp_limite:
        print(f"{pokemon} já está com o HP cheio!")
        return hp_atual, qtd, False
    novo = min(hp_limite, hp_atual + 25)
    print(f"{nome} usou uma poção! {pokemon} recuperou {novo - hp_atual} de HP.")
    return novo, qtd - 1, True

def tentar_captura(hp_atual, hp_limite):
    # Retorna True se capturou
    print(f"{nome} jogou uma Pokébola!")
    for i in range(3):
        time.sleep(1)
        print("...balança...")
    chance = 0.15 + 0.75 * (1 - hp_atual / hp_limite)
    if random.random() < chance:
        return True
    print(f"{selecionada} escapou da Pokébola!")
    return False

def ganhar_xp(xp_atual, nivel_atual, jogador_hp, jogador_hp_max):
    ganho = 10 + nivel_selvagem * 8 + hp_max // 5
    xp_atual += ganho
    print(f"{pokemon} ganhou {ganho} de XP!")
    while xp_atual >= nivel_atual * 25:
        xp_atual -= nivel_atual * 25
        nivel_atual += 1
        jogador_hp_max += 8
        jogador_hp = min(jogador_hp_max, jogador_hp + 15)
        print(f"*** {pokemon} subiu para o nível {nivel_atual}! HP máximo: {jogador_hp_max} ***")
        for g in golpes_pokemon[pokemon]:
            if g[3] == nivel_atual:
                print(f"{pokemon} aprendeu {g[0]}!")
    return xp_atual, nivel_atual, jogador_hp, jogador_hp_max

# Loop de combate
while True:
    print()
    print(f"{selecionada} Nv.{nivel_selvagem} HP:{hp}/{hp_max}")
    print(f"{pokemon} Nv.{nivel} HP:{jogador}/{jogador_max}  XP:{xp}/{nivel * 25}  Poções:{pocoes}  Pokébolas:{pokebolas}")
    print()

    acao = input("""Opções:
             [1] Atacar
             [2] Cura
             [3] Capturar
             [4] Fugir
             Qual sua escolha?:""")

    gastou_turno = False

    if acao == "1":
        golpe = escolher_golpe()
        if golpe is None:
            continue  # voltou: retorna para a ação
        dano, mult = calcular_dano(golpe[2], golpe[1], nivel, tipos_pokemon[selecionada])
        hp = max(0, hp - dano)
        print(f"\n{pokemon} usou {golpe[0]}!")
        time.sleep(1)
        if efetividade(mult):
            print(efetividade(mult))
        print(f"{selecionada} sofreu {dano} de dano!")
        gastou_turno = True

    elif acao == "2":
        jogador, pocoes, usou = usar_cura(jogador, jogador_max, pocoes)
        if not usou:
            continue  # não curou: retorna para a ação
        gastou_turno = True

    elif acao == "3":
        if pokebolas <= 0:
            print("Você não tem mais Pokébolas!")
            continue  # retorna para a ação
        pokebolas -= 1
        if tentar_captura(hp, hp_max):
            print(f"\nGotcha! {selecionada} foi capturado!")
            xp, nivel, jogador, jogador_max = ganhar_xp(xp, nivel, jogador, jogador_max)
            break
        gastou_turno = True

    elif acao == "4":
        if random.random() < 0.6:
            print("\nVocê conseguiu fugir em segurança!")
            break
        print("\nNão conseguiu fugir!")
        gastou_turno = True

    else:
        print("Opção inválida, escolha de 1 a 4!")
        continue

    # Selvagem derrotado
    if hp <= 0:
        print(f"\n{selecionada} selvagem desmaiou!")
        xp, nivel, jogador, jogador_max = ganhar_xp(xp, nivel, jogador, jogador_max)
        break

    # Turno do selvagem
    if gastou_turno:
        time.sleep(1)
        golpe_s = golpes_selvagem[selecionada]
        if random.random() < 0.1:
            print(f"\n{selecionada} usou {golpe_s[0]}, mas errou!")
        else:
            dano, mult = calcular_dano(golpe_s[2], golpe_s[1], nivel_selvagem, tipos_pokemon[pokemon])
            jogador = max(0, jogador - dano)
            print(f"\n{selecionada} usou {golpe_s[0]}!")
            time.sleep(1)
            if efetividade(mult):
                print(efetividade(mult))
            print(f"{pokemon} sofreu {dano} de dano!")
        if jogador <= 0:
            print(f"\n{pokemon} desmaiou...")
            break