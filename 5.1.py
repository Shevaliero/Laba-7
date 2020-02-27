'''Дан текст з цифр і малих латинських літер, за яким слідує крапка. Визначити яких
букв - голосних або приголосних більше в цьому тексті. Результат вивести на екран.'''
while True:
    s=input('Write text:')
    vowels='a','e','y','o','u','i'
    cons='q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
    if s.count('.')>1:
        print('Only 1 point in the end of text!')
        continue
    elif s.count('.')<1:
        print('Write point in the end of text!')
        continue
    vow=0
    con=0
    sym=0
    for i in range(len(s)):
        for j in range(len(s[i])):
                if s[i][j] in vowels:
                    vow+=1
                elif s[i][j] in cons:
                    con+=1
                else:
                    sym+=1
    if vow>con:
        print('Vowels value is more than consonants')
    elif con>vow:
        print('Consonants value is more than vowels')
    else:
        print('Value of vowels and consonants is equally')
    print(f'Vowels:{vow} \nConsonants:{con}\nSymbols:{sym}')
    c=input('Press 1 to rerun or anything else to close program')
    if c=='1':
        continue
    else:
        break
    
                       
