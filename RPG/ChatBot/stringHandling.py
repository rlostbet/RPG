import re


def IsOneOfThePhrases(words, phrases):
    """find out if words contains one of the phrases"""
    IsOneOfThePhrases = False

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    IsOneOfThePhrases = True

    return IsOneOfThePhrases


def FindMatchingPhrases():
    """find out if words contains one of the phrases"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    matchingPhrase = candidateWords

    return matchingPhrase


def FindStartingPoint():
    """find out if words contains one of the phrases"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    return j


def FindEndingPoint():
    """find out if words contains one of the phrases"""
    matchingPhrase = None

    # all the words in small cap
    for i in range(len(words)):
        words[i] = words[i].lower()

    # split phrases word by word & small cap
    for i in range(len(phrases)):
        phrases[i] = [phraseWord.lower() for phraseWord in phrases[i].split()]

    # compare
    for phrase in phrases:
        for j, word in enumerate(words):

            if word == phrase[0]:
                candidateWords = words[j: j + len(phrase)]

                if candidateWords == phrase:
                    return j + len(phrase)
