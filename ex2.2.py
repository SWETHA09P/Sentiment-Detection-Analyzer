import re
from collections import Counter
from nltk.tokenize import word_tokenize  # Asigurați-vă că aveți nltk instalat

def identifica_top_cuvinte(fisier_rezultate, fisier_rezultate_top, fisier_sentiment_scores):
    # Citirea rezultatelor din fisierul rezultate_ex1.txt
    with open(fisier_rezultate, 'r', encoding='utf-8') as file:
        rezultate = file.read()

    # Citirea scorurilor de sentiment din fisierul sentiment_scores.txt
    with open(fisier_sentiment_scores, 'r', encoding='utf-8') as sentiment_file:
        sentiment_scores = set(line.split('\t')[0].strip().lower() for line in sentiment_file)
        sentiment_scores_upper = set(line.split('\t')[0].strip() for line in sentiment_file)

    sentiment_scores.update(sentiment_scores_upper)  # Adăugăm cuvintele cu litere mari în setul cu litere mici

    # Divizarea rezultatelor în blocuri separate pentru fiecare "Tweet:"
    blocuri_tweet = rezultate.split('Tweet: ')[1:]

    # Lista în care vom colecta toate cuvintele
    cuvinte = []

    for bloc in blocuri_tweet:
        # Extragem conținutul fiecărui tweet (între "Tweet: " și "Scor:")
        tweet_content = bloc.split('Scor:')[0].strip()

        # Utilizăm tokenizer-ul pentru a obține cuvintele
        cuvinte_tweet = word_tokenize(tweet_content)

        # Filtrăm cuvintele care conțin doar litere și nu sunt în setul de cuvinte valide
        cuvinte.extend(cuvant.lower() for cuvant in cuvinte_tweet if cuvant.isalpha() and cuvant.lower() not in sentiment_scores)

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

# Exemplu de utilizare a funcției modificate
identifica_top_cuvinte('rezultat_ex1.txt', 'rezultat_ex2.2.txt', 'sentiment_scores.txt')
