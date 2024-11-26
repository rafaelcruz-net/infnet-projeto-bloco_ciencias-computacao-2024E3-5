def troco_guloso(valor, moedas):
    moedas.sort(reverse=True)

    troco = []
    for moeda in moedas:
        while valor >= moeda:
            valor -= moeda
            troco.append(moeda)
    
    if (valor != 0):
        return "Troco impossivel"
    
    return troco


moedas = [1, 5, 10, 25, 50]
troco = 100

result = troco_guloso(troco, moedas)

print("Moedas usadas para o troco", result)