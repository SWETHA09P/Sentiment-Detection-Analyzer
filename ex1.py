import json


# Citirea scorurilor din sentiment_scores.txt
def citire_scoruri(file_path):
    scoruri = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            cuvant, scor = line.strip().split('\t')
            scoruri[cuvant] = int(scor)
    return scoruri


# Identificarea tweeturilor care au cuvinte din dictionarul de scoruri
def identifica_cuvinte(tweet, scoruri):
    cuvinte_identificate = {}
    for cuvant in scoruri:
        if cuvant.lower() in tweet.lower().split():
            cuvinte_identificate[cuvant] = tweet.lower().split().count(cuvant.lower())
    return cuvinte_identificate


# Determinarea scorului per tweet in functie de cuvintele prezente in tweet si scorul lor
def calculeaza_scor_tweet(tweet, scoruri):
    scor_total_tweet = 0
    cuvinte_identificate = identifica_cuvinte(tweet, scoruri)

    for cuvant, frecventa in cuvinte_identificate.items():
        scor_total_tweet += frecventa * scoruri[cuvant]

    return scor_total_tweet, cuvinte_identificate


# Determinarea sentimentului in functie de scorul cuvintelor prezente in tweet
def determina_sentiment(scor):
    if scor > 0:
        return 'Pozitiv'
    elif scor < 0:
        return 'Negativ'
    else:
        return 'Neutru'


def citire_tweets(fisier_tweeturi, fisier_scoruri, fisier_rezultat):
    # Citirea scorurilor
    scoruri = citire_scoruri(fisier_scoruri)

    # Citirea tweet-urilor din twitter_data1.txt
    with open(fisier_tweeturi, 'r', encoding='utf-8') as file:
        tweeturi = []
        for line in file:
            tweet = json.loads(line)
            tweet_text = tweet.get('full_text', tweet.get('text', ''))
            tweeturi.append((tweet_text, tweet))

    # Calcularea scorurilor, cuvintelor și sentimentului pentru fiecare tweet
    rezultate_tweeturi = []
    for tweet_text, tweet in tweeturi:
        scor_tweet, cuvinte_tweet = calculeaza_scor_tweet(tweet_text, scoruri)
        sentiment_tweet = determina_sentiment(scor_tweet)
        rezultate_tweeturi.append((tweet_text, scor_tweet, cuvinte_tweet, sentiment_tweet))

    # Scrierea rezultatelor într-un fișier txt
    with open(fisier_rezultat, 'w', encoding='utf-8') as output_file:
        for tweet_text, scor, cuvinte, sentiment in rezultate_tweeturi:
            cuvinte_formatate = ', '.join([f"{cuvant} ({frecventa} ori)" for cuvant, frecventa in cuvinte.items()]) if cuvinte else 'Niciun cuvânt identificat'
            output_file.write(
                f"Tweet: {tweet_text}\nScor: {scor} ,Cuvinte: {cuvinte_formatate}\nSentiment: {sentiment}\n\n")


citire_tweets('twitter_data1.txt', 'sentiment_scores.txt', 'rezultat_ex1.txt')
