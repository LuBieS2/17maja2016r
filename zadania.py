from string import ascii_uppercase
#6.1
file=open("dane_6_1.txt", "r")
words=list(map(str.strip, file.readlines()))
alphabet=list(ascii_uppercase)
k=1718
word_coded=""
n=0
for word in words:
    for i in word:
        while k>len(alphabet):
            k-=len(alphabet)
        if alphabet.index(i)<len(alphabet)-k:
            word_coded+=alphabet[alphabet.index(i)+k]
        else:
            word_coded+=alphabet[alphabet.index(i)+k-len(alphabet)]
    print(word_coded)
    word_coded=""
#6.2
file=open("dane_6_2.txt", "r")
codes=list(map(str.strip, file.readlines()))
codes=[item.split(" ") for item in codes]
n=0
for code in codes:
    n+=1
    if len(code)>1:
        k=int(code[1])
    else:
        k=0

    for i in code[0]:
        while k>=len(alphabet):
            k-=len(alphabet)
        if alphabet.index(i)<len(alphabet)+k:
            word_coded+=alphabet[alphabet.index(i)-k]
        else:
            print(alphabet.index(i)-k-len(alphabet))
            word_coded+=alphabet[alphabet.index(i)-k-len(alphabet)]
    print(n, word_coded)
    word_coded=""
    #6.3
file=open("dane_6_3.txt", "r")
pairs=list(map(str.strip, file.readlines()))
pairs=[l.split(" ") for l in pairs]
bledne=[]
for pair in pairs:
    if alphabet.index(pair[1][0])-alphabet.index(pair[0][0])>=0:
        p=alphabet.index(pair[1][0])-alphabet.index(pair[0][0])
    else:
        p=alphabet.index(pair[1][0]) - alphabet.index(pair[0][0])+len(alphabet)
    for i in range(len(pair[1])):
        if alphabet.index(pair[1][i])-alphabet.index(pair[0][i])>=0:
            k=alphabet.index(pair[1][i])-alphabet.index(pair[0][i])
            if p!=k:
                bledne.append(pair)
                break
        else:
            k=alphabet.index(pair[1][i])-alphabet.index(pair[0][i])+len(alphabet)
            if p!=k and k!=0:
                bledne.append(pair)
                break
print(bledne)