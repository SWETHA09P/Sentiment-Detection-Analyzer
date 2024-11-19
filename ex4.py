import json
import matplotlib.pyplot as plt


def citeste_tweeturi(file_path):
    # Funcție pentru citirea tweet-urilor dintr-un fișier JSON
    tweeturi = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            tweeturi.append(tweet)
    return tweeturi


def citeste_sentiment(file_path):
    # Funcție pentru citirea scorurilor de sentiment dintr-un fișier
    scoruri = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            cuvant, scor = line.strip().split('\t')
            scoruri[cuvant] = int(scor)
    return scoruri


def identifica_cuvinte(tweet, scoruri):
    # Funcție pentru identificarea cuvintelor dintr-un tweet care se regăsesc în scorurile de sentiment
    cuvinte_identificate = []
    for cuvant in scoruri:
        if cuvant in tweet.split():
            cuvinte_identificate.append(cuvant)
    return cuvinte_identificate


def calculeaza_scor_tweet(tweet, scoruri):
    # Funcție pentru calcularea scorului total al unui tweet în funcție de cuvintele identificate
    scor_total_tweet = 0
    cuvinte_identificate = identifica_cuvinte(tweet, scoruri)

    for cuvant in cuvinte_identificate:
        scor_total_tweet += scoruri[cuvant]

    return scor_total_tweet


def determina_sentiment(scor):
    # Funcție pentru determinarea sentimentului în funcție de scor
    if scor > 0:
        return 'Pozitiv'
    elif scor < 0:
        return 'Negativ'
    else:
        return 'Neutru'


def main():
    # Citirea scorurilor de sentiment
    scoruri = citeste_sentiment('sentiment_scores.txt')

    # Citirea tweet-urilor
    tweeturi = citeste_tweeturi('twitter_data1.txt')

    # Calcularea scorurilor, cuvintelor, sentimentului și friends_count pentru fiecare tweet
    rezultate_tweeturi = []
    for tweet in tweeturi:
        tweet_text = tweet.get('full_text', tweet.get('text', ''))
        scor_tweet = calculeaza_scor_tweet(tweet_text, scoruri)
        sentiment_tweet = determina_sentiment(scor_tweet)

        # Excludem intrările cu sentiment neutru
        if sentiment_tweet != 'Neutru':
            prieteni = tweet['user']['friends_count']
            rezultate_tweeturi.append((tweet_text, scor_tweet, sentiment_tweet, prieteni))

    # Sortare după friends_count
    rezultate_tweeturi_sortate = sorted(rezultate_tweeturi, key=lambda x: x[3])

    # Scrierea rezultatelor într-un fișier txt
    with open('rezultat_ex4.txt', 'w', encoding='utf-8') as output_file:
        for tweet_text, scor, sentiment, friends_count in rezultate_tweeturi_sortate:
            output_file.write(
                f"Tweet: {tweet_text}\nScor: {scor}\nSentiment: {sentiment}\nFriends Count: {friends_count}\n\n")

    # Crearea graficului
    sentimenete = [item[2] for item in rezultate_tweeturi_sortate]
    prieteni = [item[3] for item in rezultate_tweeturi_sortate]

    plt.figure(figsize=(10, 6))
    plt.scatter(prieteni, sentimenete, alpha=0.5)
    plt.title('Relația dintre Sentiment și Numărul de Prieteni')
    plt.xlabel('Numărul de Prieteni')
    plt.ylabel('Sentiment')
    plt.grid(True)
    plt.show()


main()
