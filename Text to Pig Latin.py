
FromTo=input('NormalToPigLatin(1) or PigLatinTiNormal(2): ')
sentence=str(input('Give a sentence: '))

splitSentence=sentence.split(' ')

if FromTo=='1':
    for i in splitSentence:
        print(i[1:] + i[0] + 'ay', end=' ')


if FromTo=='2':
    for j in splitSentence:
        print (j[-3] + j[:-3], end=' ')

