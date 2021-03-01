from dictionary import SINS
from functions import getSentences, getTokens, countMatches, getNormalForm, getText


def classifier(text):
    text = getSentences(text)
    for iterationSentence, sentence in enumerate(text):
        text[iterationSentence] = getTokens(sentence)
    for sentence in text:
        for iterationToken, token in enumerate(sentence):
            sentence[iterationToken] = getNormalForm(token)
    sins = {sin: 0 for sin in SINS}
    for sentence in text:
        receivedSins = countMatches(sentence)
        for sin in SINS:
            sins[sin] += receivedSins[sin]
    max = 0
    for sin in SINS:
        if sins[sin] > max:
            max = sins[sin]
    mySins = []
    if max != 0:
        for sin in SINS:
            if sins[sin] == max:
                mySins.append(sin)
    return getText(mySins)
