import tweepy
import time
from keys import *
import io

# Keys para conexão com tt
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Abrindo arquivo de texto com as frases para twetar e lendo por linha
frase = io.open('frases', mode="r", encoding="utf-8")
linhas = frase.readlines()

# twittar uma frase do arquivo a cada hora
for frases in linhas:
    api.update_status(frases)
    print(f'Frase: {linhas}\ntweetado com sucesso.')
    time.sleep(3600)
