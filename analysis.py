import json
import hazm

import os
import os.path
from pathlib import Path


sentimentJSON = json.loads(open('./dictionaries/dict.json', 'r', encoding='utf-8-sig').read())
sentimentDICT = sentimentJSON['emotions']

def getWordSentiment(word):
    for key in sentimentDICT:
        if word == key:
            return sentimentDICT[key]
    return 0 # not important/not in dictionary

def getListSentiment(words):
    sentiment = 0
    for word in words:
        sentiment += getWordSentiment(word)
    return sentiment

def prepareText(text):
    normalizer = hazm.Normalizer()
    text = normalizer.normalize(text)
    tokens = hazm.word_tokenize(text)
    stemmer = hazm.Stemmer()
    words = [stemmer.stem(token) for token in tokens]
    return words

def countTextWords(text):
    normalizer = hazm.Normalizer()
    text = normalizer.normalize(text)
    tokens = hazm.word_tokenize(text)
    stemmer = hazm.Stemmer()
    words = [stemmer.stem(token) for token in tokens]
    return len(words)

def analyseText(text):
    words = prepareText(text)
    return getListSentiment(words)

def analyseTextDetailed(text):
    words = prepareText(text)
    result = []
    for word in words:
        s = getWordSentiment(word)
        if not s == 0:
            result.append((word, s))
    if len(result) > 0:
        print(result)

if __name__ == '__main__':
    dir_files = os.listdir()
    output_files = [file for file in dir_files if file.startswith(
        'merged') and file.endswith('.txt')]

    weekNumber = 16

    for file_name in output_files:
        with open(file_name, 'r') as file:
            with open('sentiments' + str(weekNumber) + '-' + file_name, 'w') as output_file:
                output_file.close()
            
            with open('sentiments' + str(weekNumber) + '-' + file_name, 'a') as output_file:
                for tweet in file:
                    sentiment = analyseText(tweet)
                    output_file.write(tweet)
                    output_file.write(str(sentiment) + '\n\n')

                output_file.close()

        file.close()