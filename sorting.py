from pymorphy2 import *

morph = MorphAnalyzer()


def sort(words):
    c = False
    while not c:
        for i in range(len(words) - 1):
            print(words[i] + ' ? ' + words[i + 1])
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] > words[i + 1][j]:
                    words[i], words[i + 1] = words[i + 1], words[i]
                    break
                elif words[i][j] < words[i + 1][j]:
                    break
        c = True
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] > words[i + 1][j]:
                    c = False
                    break
                elif words[i][j] < words[i + 1][j]:
                    break
    return words


file = open('anger.txt', 'r', encoding='utf-8')
words = file.read().split('\n')
file.close()

print(words)
words = sort(words)
print(words)

s = ''
for word in words:
    s += word + '\n'

file = open('anger.txt', 'w', encoding='utf-8')
file.write(s)
file.close()
