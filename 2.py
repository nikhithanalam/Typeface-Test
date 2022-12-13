def soundex_generator(token):
    token = token.upper()

    soundex = ""
    soundex += token[0]
    dictionary = {"BFPV": "1", "CGJKQSXZ": "2",
                  "DT": "3",
                  "L": "4", "MN": "5", "R": "6",
                  "AEIOUHWY": "."}

    for char in token[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != '.':
                    if code != soundex[-1]:
                        soundex += code

    soundex = soundex[:7].ljust(7, "0")
    return soundex


inputstr = input()
sndx = soundex_generator(inputstr)

file1 = open("2.txt","w")
L = ["Moorthy ", "Moorthi ", "Murthi ","sun ","son "]
file1.writelines(L)
file1.close()

file1 = open("2.txt","r")
for lines in file1.readlines():
    for words in list(lines.split()):
        wordsndx = soundex_generator(words)
        if wordsndx == sndx:
            print(words)
file1.close()