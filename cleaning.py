import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime
from time import sleep
import os

pasta = r'C:\Users\gabri\OneDrive\Projeto Lolzinho\Plays'


arquivos = os.listdir(pasta)
listNome = []

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho_completo):
        print(arquivo)
        listNome.append(arquivo)


print(listNome)
dictDados = {}
for i in range(0, len(listNome)):
    nome_arquivo = r"C:\Users\gabri\OneDrive\Projeto Lolzinho\Plays\{}".format(listNome[i])
    # Abre o arquivo JSON e carrega os dados
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)

    dictDados[listNome[i]] = dados

listGame = []
listPLayer = []
listKills = []
listDeaths = []
listAssistis = []
listChampion = []
listPosition = []
listFirstBlood = []
listFirstBloodAssists = []
listFirstTower = []
listFirstTowerAssists = []
listPenta = []
listQuadra = []
listTriple = []
listDouble = []
listKillingSpree = []
listWin = []
listKDA = []
listKillsParticipation = []
listSoloKills = []
listDamageMinute = []
listGoldMinute = []
listGameMode = []
listTime = []
for i in range(0, len(listNome)):
    filter = dictDados[listNome[i]]['info']['participants']
    play = listNome[i]
    Aux = dictDados[play]['info']
    mode = Aux['gameMode']
    time = Aux['gameStartTimestamp']

    for i in range(0, len(filter)):
        
        listGameMode.append(mode)
        listTime.append(time)
        
        listCampos = dictDados[play]['info']['participants']
        statusPlayer = listCampos[i]
        
        print(statusPlayer)
        listGame.append(play)
        listAssistis.append(statusPlayer['assists'])
        listKills.append(statusPlayer['kills'])
        listDeaths.append(statusPlayer['deaths'])
        listPosition.append(statusPlayer['teamPosition'])
        listChampion.append(statusPlayer['championName'])
        listPLayer.append(statusPlayer['summonerName'])
        listFirstBlood.append(statusPlayer['firstBloodKill'])
        listFirstBloodAssists.append(statusPlayer['firstBloodAssist'])
        listFirstTower.append(statusPlayer['firstTowerKill'])
        listFirstTowerAssists.append(statusPlayer['firstTowerAssist'])
        listWin.append(statusPlayer['nexusLost'])
        listPenta.append(statusPlayer['pentaKills'])
        listQuadra.append(statusPlayer['quadraKills'])
        listTriple.append(statusPlayer['tripleKills'])
        listDouble.append(statusPlayer['doubleKills'])
        listKillingSpree.append(statusPlayer['killingSprees'])
        try:
            challenges = statusPlayer.get('challenges', None)
            kda = challenges['kda']
            listKDA.append(kda)

            damageMinute = challenges['damagePerMinute']
            listDamageMinute.append(damageMinute)

            goldMinute = challenges['goldPerMinute']
            listGoldMinute.append(goldMinute)

            solo = challenges['soloKills']
            listSoloKills.append(solo)
        except:
            listKDA.append('0')
            listDamageMinute.append('0')
            listGoldMinute.append('0')
            listSoloKills.append('0')

        

dados = {'Game_Id': listGame, 'Game Mode': listGameMode, 'Data': listTime, 'Player': listPLayer, 'Campeão': listChampion, 'Posicao': listPosition, 'Abates': listKills, 'Mortes': listDeaths, 'Assistências': listAssistis, 'First Blood': listFirstBlood, 
         'First Blood Assists': listFirstBloodAssists, 'First Tower': listFirstTower, 'First Tower Assists': listFirstTowerAssists, 'Win': listWin, 'Killing Sprees': listKillingSpree, 
         'Double Kills': listDouble, 'Triple Kills': listTriple, 'Quadra Kills': listQuadra, 'Penta Kills': listPenta, 'KDA': listKDA, 'Dano por Minuto': listDamageMinute, 
         'Ouro por Minuto': listGoldMinute, 'Solo Kills': listSoloKills}
dfBase = pd.DataFrame(dados)


print(dfBase)

# print(dfBase.dtypes)
# #dfBase['Data'] = dfBase['Data'].astype(int)
# #print(dfBase)
# dfBase.to_excel(r'C:\Users\gabri\OneDrive\Projeto Lolzinho\visualizacao.xlsx')
# def converter_timestamp(timestamp):
#     try:
#         converted = datetime.fromtimestamp(timestamp)
#         return converted
#     except:
#         return 0

# dfBase['Data'] = dfBase['Data'].apply(converter_timestamp)


listDatasGames = dfBase['Data'].tolist()
listAux = []

for i in range(0, len(listDatasGames)):
    timestamp = listDatasGames[i]
    print(timestamp)
    timestamp = int(timestamp)
    print(timestamp)
    converted = datetime.utcfromtimestamp(timestamp/1000.0)
    converted = converted.strftime('%Y-%m-%d %H:%M:%S')
    listAux.append(converted)


dfBase['Data'] = listAux
print(dfBase)

dfBase.to_excel(r'C:\Users\gabri\OneDrive\Projeto Lolzinho\plays.xlsx')