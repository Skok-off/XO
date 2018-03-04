#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import random

print("This is console module")

def sravnilka(s):
    p = ''
    da = 'xxx'
    net = 'ooo'
    d = [s[0:3],
        s[3:6],
        s[6:9],
        s[0]+s[3]+s[6],
        s[1]+s[4]+s[7],
        s[2]+s[5]+s[8],
        s[0]+s[4]+s[8],
        s[2]+s[4]+s[6]]
    if da in d: 
        p = 'win'
    if net in d: 
        p = 'loss'
    return(p)

def proverka(m, n):
    pobeda = False
    if sravnilka(m) == 'win':
        pobeda = True
        print('Вы победили!')
    elif sravnilka(m) == 'loss':
        pobeda = True
        print('Вы проиграли!')
    elif not n:
        pobeda = True
        print('Ничья!')
    return pobeda

def hod(s, pos, val):
    s = s[:pos] + val + s[pos+1:]
    pole = [s[0:3], s[3:6], s[6:9]]
    for i in pole:
        st = ''
        for j in i:
            st = st + j + '|'
        print('|' + st)
    return s
    
def main():
    ss = '123456789'
    komp = 0
    v = 0
    history = list(range(1, 10))
    pobeda = False
    print('Используйте числа, чтобы сделать ход')
    hod(ss, 0, '1')
    print('Ваш ход')
    ss = '_________'
    hod(ss, 0, '_')
    while not pobeda:
        if komp == 0:
            print('Введите позицию')
            v = int(input())
            a = v - 1
            ss = hod(ss, a, 'x')
            history.remove(v)
            komp = 1
            pobeda = proverka(ss, history)
        else:
            print('Ход компьютера')
            a = random.choice(history)
            history.remove(a)
            ss = hod(ss, a - 1, 'o')
            komp = 0
            pobeda = proverka(ss, history)
        

if __name__ == '__main__':
    main()
