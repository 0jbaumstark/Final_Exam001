import random

def passwordGenerator(personal_list):

    outputList = []
    personal_list = [x for x in personal_list if not isinstance(x, int)]

    # Removes integers from list
    listWithNoInts = []
    for i in personal_list:
        if isinstance(i, str):
            listWithNoInts.append(i)
        if isinstance(i, list):
            listWithNoInts.extend(i)

    rand1 = random.randint(2, 4)

    for i in range(rand1):
        outputList.append(str(random.randint(0, 9)))

    rand2 = random.choice(listWithNoInts)
    rand3 = random.choice(listWithNoInts)
    rand4 = random.choice(listWithNoInts)
    rand5 = random.choice(listWithNoInts)

    outputList.append(rand2)
    outputList.append(rand3)
    outputList.append(rand4)
    outputList.append(rand5)

    specials = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}',
                '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    rand6 = random.choice(specials)
    rand7 = random.choice(specials)
    rand8 = random.choice(specials)

    outputList.append(rand6)
    outputList.append(rand7)
    outputList.append(rand8)

    holder = 0
    for i in outputList:
        char_list = list(i)
        random.shuffle(char_list)
        finalStr = ''.join(char_list)
        outputList[holder] = finalStr
        holder = holder + 1

    # shuffles the strings in the list
    random.shuffle(outputList)

    # shuffles the order of items
    password = ''.join(outputList)

    return password


if __name__ == "__main__":
    mylist = [12, "BOB", -2, "Amy", ["David", "Jona", "Timmothy"], "Burt"]
    print(passwordGenerator(mylist))