import json
import hazm

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
    datafile = open('sample_output.json', 'r', encoding='utf-8-sig')
    outputfile = open('sample_output.txt', 'w', encoding='utf-8-sig')

    for line in datafile:
        text = json.loads(line)['text']
        outputfile.write(text + '\n' + str(analyseText(text)) + '\n\n\n')
        analyseTextDetailed(text)

    datafile.close()
    outputfile.close()