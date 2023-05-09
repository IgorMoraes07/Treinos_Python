import socket as sc
import tweepy as tw

HOST = 'localhost'
PORT = 9009

s = sc.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na Porta: {PORT}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de {address}')

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAM4NnAEAAAAAEKb1I5lSgMOg9KNLqjEcvEnyWyw%3Dxz9uNOBmKY2zWcBqnOQMCTKn4ROHhA6XgWsmWU617iqbLhmE2B'
access_token = '76497618-hPoudvu2UhJIisgm2PZmtUkqNB6pndIj5Z2eoNqsb'
access_token_secret = 'fpkg9adonJpeeyCNEGRsr3qVJ9incSlIg0vLhXHSbsyyR'
keyword = 'nfl'


class GetTweets(tw.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('latin1', 'ignore'))


printer = GetTweets(bearer_token)
printer.add_rules(tw.StreamRule(keyword))
printer.filter()

connection.close()
