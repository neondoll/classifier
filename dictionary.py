def getSinsKeywords(file):
    reader = open(file, 'r', encoding='utf-8')
    expressions = reader.read().split('\n')
    reader.close()
    keys = []
    for expression in expressions:
        keys.append(getExpressionsWithBrackets(expression.split(' ')))
    return keys


def getExpressionsWithBrackets(expression):
    if '(' and ')' in expression:
        time = []
        begin = 0
        c = 0
        for iterationExpression in range(len(expression)):
            if expression[iterationExpression] == '(':
                if c == 0:
                    begin = iterationExpression + 1
                    time.append(expression[iterationExpression])
                c += 1
            elif expression[iterationExpression] == ')':
                c -= 1
                if c == 0:
                    time.append(getExpressionsWithDashes(expression[begin:iterationExpression]))
                    time.append(expression[iterationExpression])
            elif c == 0:
                time.append(expression[iterationExpression])
        expression = time
    return expression


def getExpressionsWithDashes(expression):
    if '|' in expression:
        time = []
        begin = 0
        iterationExpression = 0
        c = 0
        while iterationExpression < len(expression) + 1:
            if iterationExpression == len(expression):
                time.append(getExpressionsWithBrackets(expression[begin:iterationExpression]))
            elif expression[iterationExpression] == '(':
                c += 1
            elif expression[iterationExpression] == ')':
                c -= 1
            elif expression[iterationExpression] == '|':
                if c == 0:
                    time.append(getExpressionsWithBrackets(expression[begin:iterationExpression]))
                    time.append(expression[iterationExpression])
                    begin = iterationExpression + 1
            iterationExpression += 1
        expression = time
    return expression


MARKS = [',', '.', ':', ';', '!', '?', '…', '(', ')', '<', '>', '-', '–', '=', '[', ']']

SINS = ['гордыня', 'алчность', 'зависть', 'гнев', 'похоть', 'чревоугодие', 'лень', 'уныние']
SINS_KEYWORDS = {'гордыня': getSinsKeywords('pride.txt'), 'алчность': getSinsKeywords('stinginess.txt'),
                 'зависть': getSinsKeywords('envy.txt'), 'гнев': getSinsKeywords('anger.txt'),
                 'похоть': getSinsKeywords('lust.txt'), 'чревоугодие': getSinsKeywords('gluttony.txt'),
                 'лень': getSinsKeywords('sloth.txt'), 'уныние': getSinsKeywords('gloom.txt')}
SINS_DEMONS = {'гордыня': 'Люцифер', 'алчность': 'Мамона', 'зависть': 'Левиафан', 'гнев': 'Сатана', 'похоть': 'Асмодей',
               'чревоугодие': 'Вельзевул', 'лень': 'Бельфегор', 'уныние': 'Астарот'}
