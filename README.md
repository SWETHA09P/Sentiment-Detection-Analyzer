# 🐦Tweet Sentiment Analyzer📊

In this project, we will use a dataset of tweets as the source of data. Implement the requirements below using one or more Python scripts. Along with these, a short explanatory text will be provided, explaining the solution and how to run the scripts.

**Note:** Due to privacy policies, I am not allowed to post the dataset publicly.

---

## Table of Contents📑
1. [Predominant Sentiment in Each Tweet](#predominant-sentiment-in-each-tweet)
2. [Most Frequent Terms](#most-frequent-terms)
3. [Deriving Sentiment Scores](#deriving-sentiment-scores)
4. [“Do Not Have 100 Rubles, Have 100 Friends”](#do-not-have-100-rubles-have-100-friends)

---

## Predominant Sentiment in Each Tweet🧠

The tweets in the data source contain various texts, and we need to decide if they express a positive or negative sentiment. For each tweet in the input file, calculate the sentiment by summing the sentiment scores of each word in the tweet. For certain more frequent words, the scores are found in the `sentiment_scores.txt` file. For words that do not appear in the given list, the score will be considered 0.

**Hint:**  
To read the tweets from the input file, you can use the [json module](https://docs.python.org/2/library/json.html).

---

## Most Frequent Terms📈

Identify the 500 most frequently used terms in the dataset of tweets, and list them in descending order of frequency.

---

## Deriving Sentiment Scores💡

For the words in the top list identified earlier, if they do not have a sentiment score calculated, associate them with a score.

**Hints:**
- In `sentiment_scores.txt`, words frequently used in tweets expressing a positive sentiment likely express a positive sentiment (and similarly for negative sentiments).
- What can we infer about words that appear in both categories of tweets?

---

## "Do Not Have 100 Rubles, Have 100 Friends"💬

Implement a method to test the hypothesis that people with many friends are happier, based on the provided data. What conclusion did you reach?

---
