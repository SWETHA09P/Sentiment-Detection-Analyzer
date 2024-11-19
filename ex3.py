import re


def extract_scores(tweet):
    # Extract scores from the "Scor:" lines in the tweet
    score_matches = re.findall(r'Scor: ([\d-]+)', tweet)
    return list(map(int, score_matches))


def calculate_term_score(term, tweets):
    term_scores = []
    total_positive = 0
    total_negative = 0

    for tweet in tweets:
        if term.lower() in tweet.lower():
            scores = extract_scores(tweet)

            # Calculate the score for the current term in this tweet
            term_score = sum(scores)
            term_scores.append(term_score)

            # Count positive and negative tweets
            if any(score > 0 for score in scores):
                total_positive += 1
            elif any(score < 0 for score in scores):
                total_negative += 1

    # Calculate the final score for the term
    if total_positive + total_negative == 0:
        return 0  # Avoid division by zero
    return round(sum(term_scores) / (total_positive + total_negative))


def write_results_to_file(terms, results):
    with open('rezultat_ex3.txt', 'w', encoding='utf-8') as output_file:
        for term, score in zip(terms, results):
            output_file.write(f"Term: {term}\t Score: {score}\n")


def main():
    # Read terms from rezultat_ex2.txt
    with open('rezultat_ex2.txt', 'r', encoding='utf-8') as terms_file:
        terms = [line.split()[0] for line in terms_file]

    # Read tweets from rezultat_ex1.txt
    with open('rezultat_ex1.txt', 'r', encoding='utf-8') as tweets_file:
        tweets = tweets_file.read().split('Tweet: ')[1:]

    # Calculate scores for each term
    term_scores = [calculate_term_score(term, tweets) for term in terms]

    # Write results to rezultat_ex3.txt
    write_results_to_file(terms, term_scores)


main()
