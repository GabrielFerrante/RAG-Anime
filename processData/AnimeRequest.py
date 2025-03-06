import requests
import json
import string
import time
import pandas as pd

#https://docs.api.jikan.moe
ENDPOINT_BASE = 'https://api.jikan.moe/v4/anime'


def generateDataFrame(jsonName):
    # Carregar dados do JSON
    data = json.load(open(jsonName))

    # Converter para DataFrame (para facilitar o processamento)
    
    colectionDF = []

    for i in range(1, 214):
        df = pd.DataFrame(data[str(i)]['data'])
        colectionDF.append(df)
    
    return colectionDF

def getAnimes():
    endpoint = ENDPOINT_BASE
    dados = {}
    for i in range(0, 214):
        params = {'page':i, 'type':'tv', 'start_date':'1990-01-01', 'end_date':'2025-01-31'}  
        result = requests.get(endpoint, params=params)
        dados[i] = result.json()

   # Grava os dados em formato JSON
    with open('C:/Repositorios/RAG-Anime/dados/animes.json', 'w') as jsonfile:
        json.dump(dados, jsonfile, indent=4)
    

def getPersonagensAnimes():
    df = generateDataFrame('C:/Repositorios/RAG-Anime/dados/animes.json')
    for i in range(0,214): #numero de paginas  

        ids = df[i].filter(items=['mal_id'])
        
        personagens = {}
        for id in ids['mal_id']:
            endpoint = f'{ENDPOINT_BASE}/{id}/characters'
            result = requests.get(endpoint)
            personagens[id] = result.json()
            time.sleep(2) #throttling para evitar bloqueio da API
            with open(f'C:/Repositorios/RAG-Anime/dados/personagensAnimes{i}.json', 'w') as jsonfile:
                json.dump(personagens, jsonfile, indent=4)


def getEpisodiosAnimes():

    # https://api.jikan.moe/v4/anime/{id}/episodes/{episode}

    # Gere o DataFrame usando a função generateDataFrame
    df = generateDataFrame('C:/Repositorios/RAG-Anime/dados/animes.json')
  
    for i in range(0,214):
        dados = df[i].filter(items=['mal_id', 'episodes'])
        for id in dados['mal_id']:
            for numEpi in dados['episodes']:
                episodioAnime = {}
                episodioAnime[id] = {}
                for epi in range(1, numEpi):
                    endpoint = f'{ENDPOINT_BASE}/{id}/episodes/{epi}'
                    result = requests.get(endpoint)
                    episodioAnime[id][epi] = result.json()
                    time.sleep(1) #throttling para evitar bloqueio da API
                    print(episodioAnime)
                with open(f'C:/Repositorios/RAG-Anime/dados/episodios-Anime{id}.json', 'w') as jsonfile:
                    json.dump(episodioAnime, jsonfile, indent=4)
                break
                    

getEpisodiosAnimes()