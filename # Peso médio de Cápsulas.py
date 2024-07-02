# Peso médio de Cápsulas

embalagens_peso = dict([ ("R30", 7.804), ("R60", 14.653), ("R90", 17.293), ("R120", 18.797), ("R180", 23.733),  
                        ("R240", 30.032), ("R300", 34.946), ("R500", 60.282), ("R750", 67.397), ("R1000", 81.034), ("Nenhuma", 0.0)])

capsula_peso = dict([("Cápsula 3", 0.05 ), ("Cápsula 2", 0.06), ("Cápsula 1", 0.075), ("Cápsula 0", 0.1), ("Cápsula 00", 0.12), ("Cápsula Dual", 0.15),
                      ("Env. grande", 1.3), ("Env. pequeno", 0.9)])

for potes in embalagens_peso:
    peso = embalagens_peso [potes]

for capsulas in capsula_peso:
    valor = capsula_peso[capsulas]

chave_embalagem = embalagens_peso.keys()
chave_capsulas = capsula_peso.keys()

tamanho_capsula = input(f"Escolha o tamanho da cápsula ou sachê:\n{chave_capsulas}\n").replace("capsula","Cápsula").replace("env","Env.").capitalize()
resultado_capsula = capsula_peso[tamanho_capsula]

if tamanho_capsula == "Env. grande" or tamanho_capsula == "Env. pequeno":
    quantidade_sache = int(input("Qual é a quantidade de sachês?\n"))
    sache_vazio = resultado_capsula * quantidade_sache

    peso_inteiro = input("Qual é o total de todos os sachês?\n").replace(",",".")
    peso_inteiro_novo = float(peso_inteiro)

    peso_bruto = peso_inteiro_novo - sache_vazio
    peso_medio_sache = peso_bruto / quantidade_sache

    print(f"o peso total de máteria prima é: {peso_bruto:.2f}\nO peso médio dos sachês é: {peso_medio_sache:.3f}")
    quit()

tamanho_embalagem = input(f"Escolha o tamanho da embalagem:\n{chave_embalagem}\n").capitalize()
resultado_embalagem = embalagens_peso[tamanho_embalagem]

quantidade = int(input("Qual é a quantidade de cápsulas?\n"))
cap_vazia = resultado_capsula * quantidade

peso_completo = input("Qual é o peso total com pote e tampa ou sem embalagem?\n").replace(",",".")
peso_completo_novo = float(peso_completo)
peso_total =  peso_completo_novo - resultado_embalagem - cap_vazia

tem_silica = input("Tem sílica dentro do pote?\nSim ou Não\n").replace("nao","Não").capitalize()
if tem_silica == "Sim":
    silica = True
else:
    silica = False

if silica == True:
    peso_total -= 1.086
    peso_medio = peso_total / quantidade
else:
    peso_medio = peso_total / quantidade

print(f"O peso total de máteria prima é: {peso_total:.2f}\nO peso médio das cápsulas é: {peso_medio:.3f}")
