file1 = open("dane_6_1.txt")
file_wynik1= open("wyniki_6_1.txt","w")

k=107

def szyfr(word,key):
    new_key = key - (key // 26) * 26
    new_word = ""
    for x in word:
        letter = ord(x) + new_key
        if 64 < letter and letter<91:
            new_word+=chr(letter)
        elif letter>90:
            letter=letter-25
            new_word+=chr(letter)
    file_wynik1.write(new_word)

for i in file1:
    line=i[0:len(i)-1]
    print(list(line))
    print(szyfr(line,k))
