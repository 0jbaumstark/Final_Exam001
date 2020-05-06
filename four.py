def questionOne():
    inputF = open("four.txt", 'r')
    outputF = open("solution4.txt", 'w')

    for line in inputF:
        outputString = ""
        for i in line:
            if i.isupper():
                outputString = outputString + i
            else:
                pass
        outputF.write(outputString)

    inputF.close()
    outputF.close()


def questionTwo():
    inputF = open("four.txt", 'r')

    numbers = '0123456789'

    finalNum3 = 0

    for fileLines in inputF:
        for text in fileLines:
            if text in numbers:
                # print(i)
                finalNum3 = finalNum3 + int(text)
    outputString = ""

    with open("four.txt") as fp:
        for i, line in enumerate(fp):
            if i >= 10:

                for aLine in line:
                    outputString = outputString + aLine.replace("|", " ")
                break

    counter = 0

    if "|" not in outputString:
        for i in outputString:
            counter = counter + 1
            if counter >= finalNum3:
                print("test")
                print(i)
                break

    inputF.close()


if __name__ == "__main__":
    questionOne()
    questionTwo()