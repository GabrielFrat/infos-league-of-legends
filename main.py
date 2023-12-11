import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from time import sleep

key = "RGAPI-1c11c2f4-68d4-4a8d-82db-7bfbf4da8cf2"

url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/ppj7J7EbAUiI_e7W85xZCv7xBUBQNh4bdE3nXmMSd4muQSZRhaZkCYxQV4YwuiWkqOcb8on_Px569g/ids?start=0&count=100&api_key=RGAPI-1c11c2f4-68d4-4a8d-82db-7bfbf4da8cf2"
resp = requests.get(url)
matchIdList = resp.json()
print(matchIdList)

for i in range(0, len(matchIdList)):

    match_id = matchIdList[i]
    url_match = "https://americas.api.riotgames.com/lol/match/v5/matches/{}?api_key=RGAPI-1c11c2f4-68d4-4a8d-82db-7bfbf4da8cf2".format(match_id)

    resp = requests.get(url_match)
    gameMatch = resp.json()
    print(gameMatch)
    with open(r"C:\Users\gabri\OneDrive\Projeto Lolzinho\Plays\{}".format(match_id), 'w') as arq:
        json.dump(gameMatch, arq)

    sleep(10)