import tweepy
import pandas as pd
import os

# Configurar credenciais da API (substitua com suas chaves)
# api_key = "WWiQgWb0C2DolJmdM9AO5Q4yE"
# api_secret = "8ZtBjZIi6ZS4PIQDMEDpRdhRMwAnSYqzOD2QZUQYH2l1cLsmm5"
# access_token = "1122342558179430400-8cjjVIQrVv4W3NI7lND8IOLf4SXGe6"
# access_secret = "mrC3yM6ifOiPIRhz2bjXlixP7fJLOV3pcQ1LzWhXdpGUg"

# Autenticação na API do Twitter
# auth = tweepy.OAuthHandler(api_key, api_secret)
# auth.set_access_token(access_token, access_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True)

bearer_token = "AAAAAAAAAAAAAAAAAAAAAJ60zgEAAAAAE8LxWrznbvUmnS%2FC%2FzbQ5b%2Bk0tc%3D1NdfXElrtacd6qDNtWxxed7SWtBMbHpvDUu54lC009tbZzGR2Z"

# Initialize the Tweepy client
client = tweepy.Client(bearer_token=bearer_token)

# Função para coletar tweets e salvar em um arquivo CSV
def coletar_e_salvar_tweets(termo, qtd=50, arquivo="tweets.csv"):
    # Definir a consulta de pesquisa
    query = f"{termo} -is:retweet lang:pt"
    
    # Coletar os tweets
    tweets = client.search_recent_tweets(query=query, max_results=qtd, tweet_fields=["created_at", "text", "lang"])
    
    # Extrair dados relevantes
    tweet_data = []
    if tweets.data:
        for tweet in tweets.data:
            tweet_data.append([tweet.created_at, tweet.text])
    
    # Criar um DataFrame
    df = pd.DataFrame(tweet_data, columns=["data", "tweet"])
    
    # Garantir que a pasta 'data' exista
    os.makedirs("data", exist_ok=True)
    
    # Caminho completo do arquivo CSV
    caminho_arquivo = os.path.join("data", arquivo)
    
    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(caminho_arquivo, index=False, encoding="utf-8-sig")
    print(f"Arquivo salvo em: {caminho_arquivo}")

# Exemplo de uso
coletar_e_salvar_tweets("Tesla", qtd=40, arquivo="tweets_tesla.csv")