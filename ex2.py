import re
from collections import Counter


def identifica_top_cuvinte(fisier_rezultate, fisier_rezultate_top, fisier_sentiment_scores):
    # Citirea rezultatelor din fisierul rezultate_ex1.txt
    with open(fisier_rezultate, 'r', encoding='utf-8') as file:
        rezultate = file.read()

    # Citirea scorurilor de sentiment din fisierul sentiment_scores.txt
    with open(fisier_sentiment_scores, 'r', encoding='utf-8') as sentiment_file:
        sentiment_scores = set(line.split('\t')[0].lower().strip() for line in sentiment_file)

    # Divizarea rezultatelor în blocuri separate pentru fiecare "Tweet:"
    blocuri_tweet = rezultate.split('Tweet: ')[1:]

    # Lista în care vom colecta toate cuvintele
    cuvinte = []

    for bloc in blocuri_tweet:
        # Extragem conținutul fiecărui tweet (între "Tweet: " și "Scor:")
        tweet_content = bloc.split('Scor:')[0].strip()

        # Folosim regex pentru a găsi toate cuvintele care conțin doar litere
        cuvinte_tweet = re.findall(r'\b[A-Za-z]+\b', tweet_content)

        # Convertim cuvintele la litere mici înainte de adăugarea lor
        cuvinte.extend(cuvant.lower() for cuvant in cuvinte_tweet if cuvant.lower() not in sentiment_scores)

    # Verificare dacă lista cuvinte are cel puțin 500 de elemente
    if len(cuvinte) >= 500:
        # Calcularea frecvenței cuvintelor
        contor_cuvinte = Counter(cuvinte)

        # Identificarea celor mai folosiți 500 de cuvinte
        top_500 = contor_cuvinte.most_common(500)

        # Scrierea rezultatelor în fisierul rezultate_ex2.txt
        with open(fisier_rezultate_top, 'w', encoding='utf-8') as output_file:
            for cuvant, frecventa in top_500:
                output_file.write(f"{cuvant}\t {frecventa}\n")
    else:
        print("Lista de cuvinte nu are suficiente elemente pentru a identifica 500 de cuvinte.")


# Exemplu de utilizare a noii funcții
identifica_top_cuvinte('rezultat_ex1.txt', 'rezultat_ex2.txt', 'sentiment_scores.txt')
