import tweepy
from time import sleep
from keyssearch import *

# Keys para conexão com tt
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Palavra pesquisada / Quantidade de retweets por execução
search = 'Santa Zuera'
numberOfTweets = 50

while True:
    print('-' * 40)
    print('Começando rodada de buscas.'.center(40))
    print('-' * 40)
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            print("\nTweet encontrado")
            if not tweet.retweeted: # Se ainda não foi retweetado e respondido, retweetar e responder.
                print('Tweet por: @' + tweet.user.screen_name)
                tweet.retweet()
                print('Retweet feito com sucesso.')
                resposta = "Olá @" + tweet.user.screen_name + ", te pegamos no flagra haha. Você caiu no nosso pente fino e tweetou algo com nosso nome, obrigado por lembrar de nós, ou não hehe."
                resp = api.update_status(status=resposta, in_reply_to_status_id=tweet.id)
                print('Resposta ao tweet feito com sucesso.')

            if not tweet.user.following:
                tweet.user.follow()
                print(f'Usuário ' + tweet.user.screen_name + ' seguido com sucesso.')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    print('-' * 40)
    print('Rodada Completa.'.center(40))
    print('-' * 40)
    print(f'Começando outra rodada em: ')
    for c in range(600, -1, -1):
        print(c)
        sleep(1)
