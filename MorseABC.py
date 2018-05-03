engToMorse_Dict={'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.',
                 'F' : '..-.' ,'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---',
                 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...',
                 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', '0' : '-----',
                 '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..',
                 '9' : '----.'}

morseToEng_dict={'.-' : 'A', '-...' : 'B', '-.-.' : 'C', '-..' : 'D', '.' : 'E','..-.' : 'F' ,'--.' : 'G', '....' : 'H', '..' : 'I', '.---' : 'J',
                 '-.-' : 'K', '.-..' : 'L', '--' : 'M', '-.' : 'N', '---' : 'O', '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R', '...' : 'S',
                 '-' : 'T', '..-' : 'U', '...-' : 'V', '.--' : 'W', '-..-' : 'X', '-.--' : 'Y', '--..' : 'Z', '-----' : '0',
                 '.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8',
                 '----.' : '9'}
print(engToMorse_Dict.values())

answer=input('EngToMorse(1) or MorseToEng(2): ')

string=input("Give a string: ")
string=string.upper()
#string=string.split(' ')



if answer=='1':
    for i in string:
        if i==' ':
            print('      ',end=' ')
        else:
            print(engToMorse_Dict[i],end='   ')

elif answer=='2':
    wordslist = string.split('       ')
    print(wordslist)
    for j in wordslist:
        if '   ' in j:
            letters=j.split('   ')
            for k in letters:
                print(morseToEng_dict[k],end='')
        else:
            print(' ' + morseToEng_dict[j],end=' ')
