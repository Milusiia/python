file1 = open("dane_6_1.txt")
file_wynik1= open("wyniki_6_1.txt","w")

file2 = open("dane_6_2.txt")
file_wynik2= open("wyniki_6_2.txt","w")

file3 = open("dane_6_3.txt")
file_wynik3= open("wyniki_6_3.txt","w")


def szyfr(word,key):
    new_key = key - (key // 26) * 26
    new_word = ""
    for x in word:
        letter = ord(x) + new_key
        if letter > 64 and letter < 91:
            new_word+=chr(letter)

        elif letter>90:
            letter=letter-25
            new_word+=chr(letter)
    new_word+="\n"
    return new_word

def deszyfr(word,key):
    new_key = key - (key // 26) * 26
    new_word = ""
    for x in word:
        letter = ord(x) - new_key
        if letter > 64 and letter < 91:
            new_word += chr(letter)

        elif letter < 65:
            letter = letter + (90-64)
            new_word += chr(letter)
    new_word += "\n"
    return new_word

def klucz(w1,w2):
    first_key = 0
    key = 0
    for i in range (len(w1)):
        word1 = ord(w1[i])
        word2 = ord(w2[i])
        while word1 != word2:
            word1+=1
            key+=1
            if word1>90:
                word1=word1-26
        if first_key == 0:
            first_key = key
        if first_key != key:
            return False
        key=0
    return True

def zad1():
    k1=107
    for i in file1:
        new = (szyfr(i,k1))
        file_wynik1.write(new)

def zad2():
    for i in file2:
        line = i.split()
        word = line[0]
        key = line[1]
        new = (deszyfr(word,int(key)))
        file_wynik2.write(new)

def zad3():
    for i in file3:
        line = i.split()
        word = line[0]
        word2 = line[1]
        if (klucz(word,word2)) is False:
            bad = word + "\n"
            file_wynik3.write(bad)

zad1()
zad2()
zad3()


