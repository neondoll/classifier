from classifier import classifier


def test():
    for i in range(3):
        if i != 0:
            print('-------------')
        file = open('test\\testtext' + str(i + 1) + '.txt', 'r', encoding='utf-8')
        test = file.read().split(
            '\n----------------------------------------------------------------------------------------\n')
        testText = test[0]
        testAnswer = test[1]
        file.close()
        print(testAnswer == classifier(testText))


test()