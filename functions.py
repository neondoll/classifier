from dictionary import *
from pymorphy2 import MorphAnalyzer


def carryover(lenth):
    if lenth % 9 == 0:
        return "\n"
    return " "


def countMatches(sentence):
    sins = {sin: 0 for sin in SINS}
    for sin in SINS:
        i = 0
        while i < len(sentence):
            for keyword in SINS_KEYWORDS[sin]:
                t, check = searchMatches(sentence, i, keyword)
                if check:
                    s = ''
                    for j in range(i, t):
                        s += sentence[j] + ' '
                    sins[sin] += 1
                    i = t
                    #print(s + '- ' + sin)
            i += 1
    return sins


def isLetter(ch):
    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я'):
        return True
    return False


def isSeparator(s): return s in MARKS


def getNormalForm(token):
    morph = MorphAnalyzer()
    #print(morph.parse(token))
    return morph.parse(token)[0].normal_form


def getSentences(text):
    sentences = []
    j = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!' or i == len(text) - 1:
            sentences.append(text[j:i + 1])
            j = i + 2
    return sentences


def getText(my_sins):
    if len(my_sins) == 0:
        str = 'Вы безгрешны...'
    elif len(my_sins) == 1:
        str = 'Ваш грех - ' + my_sins[0] + '. Продолжайте в том же духе и вас заберет ' + SINS_DEMONS[my_sins[0]] + '.'
    else:
        str = 'Ваши грехи -'
        lenth_str = 2
        for sin in my_sins:
            str += carryover(lenth_str) + sin
            lenth_str += 1
            if sin == my_sins[-1]:
                str += '.'
            elif sin == my_sins[-2]:
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
            else:
                str += ','
        str += carryover(lenth_str) + 'Вас'
        lenth_str += 1
        str += carryover(lenth_str) + 'заберет'
        lenth_str += 1
        for sin in my_sins:
            str += carryover(lenth_str) + SINS_DEMONS[sin]
            lenth_str += 1
            if sin == my_sins[-1]:
                str += '.'
            elif sin == my_sins[-2]:
                str += carryover(lenth_str) + 'или'
                lenth_str += 1
            else:
                str += ','
        for sin in my_sins:
            str += carryover(lenth_str) + 'Если'
            lenth_str += 1
            str += carryover(lenth_str) + 'хотите,'
            lenth_str += 1
            str += carryover(lenth_str) + 'чтобы'
            lenth_str += 1
            str += carryover(lenth_str) + 'вас'
            lenth_str += 1
            str += carryover(lenth_str) + 'забрал'
            lenth_str += 1
            str += carryover(lenth_str) + SINS_DEMONS[sin] + ','
            lenth_str += 1
            if sin == 'pride':
                str += carryover(lenth_str) + 'ходите'
                lenth_str += 1
                str += carryover(lenth_str) + 'с'
                lenth_str += 1
                str += carryover(lenth_str) + 'высоко'
                lenth_str += 1
                str += carryover(lenth_str) + 'задранным'
                lenth_str += 1
                str += carryover(lenth_str) + 'носом'
                lenth_str += 1
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
                str += carryover(lenth_str) + 'гордитесь'
                lenth_str += 1
                str += carryover(lenth_str) + 'собой.'
                lenth_str += 1
            elif sin == 'stinginess':
                str += carryover(lenth_str) + 'храните'
                lenth_str += 1
                str += carryover(lenth_str) + 'маленький'
                lenth_str += 1
                str += carryover(lenth_str) + 'сундучок'
                lenth_str += 1
                str += carryover(lenth_str) + 'со'
                lenth_str += 1
                str += carryover(lenth_str) + 'златом'
                lenth_str += 1
                str += carryover(lenth_str) + 'под'
                lenth_str += 1
                str += carryover(lenth_str) + 'кроватью'
                lenth_str += 1
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
                str += carryover(lenth_str) + 'пополняйте'
                lenth_str += 1
                str += carryover(lenth_str) + 'его'
                lenth_str += 1
                str += carryover(lenth_str) + 'каждый'
                lenth_str += 1
                str += carryover(lenth_str) + 'день.'
            elif sin == 'envy':
                str += carryover(lenth_str) + 'сильнее'
                lenth_str += 1
                str += carryover(lenth_str) + 'наблюдайте'
                lenth_str += 1
                str += carryover(lenth_str) + 'за'
                lenth_str += 1
                str += carryover(lenth_str) + 'другими'
                lenth_str += 1
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
                str += carryover(lenth_str) + 'сравнивайте'
                lenth_str += 1
                str += carryover(lenth_str) + 'с'
                lenth_str += 1
                str += carryover(lenth_str) + 'собой.'
                lenth_str += 1
            elif sin == 'anger':
                str += carryover(lenth_str) + 'злитесь'
                lenth_str += 1
                str += carryover(lenth_str) + 'как'
                lenth_str += 1
                str += carryover(lenth_str) + 'можно'
                lenth_str += 1
                str += carryover(lenth_str) + 'чаще,'
                lenth_str += 1
                str += carryover(lenth_str) + 'сопровождая'
                lenth_str += 1
                str += carryover(lenth_str) + 'это'
                lenth_str += 1
                str += carryover(lenth_str) + 'разбитой'
                lenth_str += 1
                str += carryover(lenth_str) + 'посудой'
                lenth_str += 1
                str += carryover(lenth_str) + 'или'
                lenth_str += 1
                str += carryover(lenth_str) + 'чьей-то'
                lenth_str += 1
                str += carryover(lenth_str) + 'моськой.'
                lenth_str += 1
            elif sin == 'lust':
                str += carryover(lenth_str) + 'измение'
                lenth_str += 1
                str += carryover(lenth_str) + 'жене/мужу,'
                lenth_str += 1
                str += carryover(lenth_str) + 'а'
                lenth_str += 1
                str += carryover(lenth_str) + 'лучше'
                lenth_str += 1
                str += carryover(lenth_str) + 'несколько'
                lenth_str += 1
                str += carryover(lenth_str) + 'раз.'
                lenth_str += 1
            elif sin == 'gluttony':
                str += carryover(lenth_str) + 'очень'
                lenth_str += 1
                str += carryover(lenth_str) + 'плотно'
                lenth_str += 1
                str += carryover(lenth_str) + 'кушайте,'
                lenth_str += 1
                str += carryover(lenth_str) + 'лучше'
                lenth_str += 1
                str += carryover(lenth_str) + '5 раз'
                lenth_str += 1
                str += carryover(lenth_str) + 'в'
                lenth_str += 1
                str += carryover(lenth_str) + 'день.'
                lenth_str += 1
            elif sin == 'sloth':
                str += carryover(lenth_str) + 'лягте'
                lenth_str += 1
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
                str += carryover(lenth_str) + 'поплюйте'
                lenth_str += 1
                str += carryover(lenth_str) + 'в'
                lenth_str += 1
                str += carryover(lenth_str) + 'потолок.'
                lenth_str += 1
            elif sin == 'gloom':
                str += carryover(lenth_str) + 'закройтесь'
                lenth_str += 1
                str += carryover(lenth_str) + 'в'
                lenth_str += 1
                str += carryover(lenth_str) + 'ванной'
                lenth_str += 1
                str += carryover(lenth_str) + 'и'
                lenth_str += 1
                str += carryover(lenth_str) + 'поплачьте.'
                lenth_str += 1
    return str


def getTokens(text):
    length = len(text)
    str = text.lower().replace('ё', 'е')
    lexemes = []
    if length > 0:
        i = 0
        while i < length:
            if i < length and (str[i] == ' ' or str[i] == '\n' or str[i] == '\t'):
                while i < length and (str[i] == ' ' or str[i] == '\n' or str[i] == '\t'):
                    i += 1
            begin = i
            if i < length and isSeparator(str[i]):
                while i < length and isSeparator(str[i]):
                    i += 1
            elif i < length and str[i].isdigit():
                while i < length and str[i].isdigit():
                    i += 1
            elif i < length and (str[i] == '"' or str[i] == '«'):
                end = '"' if str[i] == '"' else '»'
                i += 1
                while i < length and str[i] != end:
                    i += 1
                i += 1
            elif i < length and isLetter(str[i]):
                while i < length and (isLetter(str[i]) or str[i] == '-' or str[i] == "'"):
                    i += 1
            lexemes.append(str[begin:i])
    return lexemes


def searchMatches(tokens, iterationTokens, keyword):
    check = True
    iterationKeyword = 0
    while check and iterationKeyword < len(keyword):
        if type(keyword[iterationKeyword]) == str:
            if keyword[iterationKeyword] == tokens[iterationTokens]:
                iterationKeyword += 1
                iterationTokens += 1
            elif keyword[iterationKeyword] == '...':
                iterationKeyword += 1
                while iterationTokens < len(tokens) - 1 and iterationKeyword < len(keyword) \
                        and tokens[iterationTokens] != keyword[iterationKeyword]:
                    iterationTokens += 1
                if iterationTokens == len(tokens) - 1:
                    iterationTokens -= 1
                check = check and not (tokens[iterationTokens] in MARKS)
            elif keyword[iterationKeyword] == '(' or keyword[iterationKeyword] == ')':
                iterationKeyword += 1
            else:
                check = check and False
        elif type(keyword[iterationKeyword]) == list:
            if '|' in keyword[iterationKeyword]:
                checkList = False
                iterationListKeyword = 0
                while not checkList and iterationListKeyword < len(keyword[iterationKeyword]):
                    iterationTokens, checkList = searchMatches(tokens, iterationTokens,
                                                               keyword[iterationKeyword][iterationListKeyword])
                    iterationListKeyword += 2
            else:
                iterationTokens, checkList = searchMatches(tokens, iterationTokens, keyword[iterationKeyword])
            check = check and checkList
            if check:
                iterationKeyword += 1
            else:
                return iterationTokens, check
    return iterationTokens, check
