def is_antipalindrome(n):
    """
    verifica daca un numar n este antipalindrom
    :param n:
    :return: false daca n nu este antipalindrom si true in caz contrar
    """
    for j in range (len(n)//2):
        if n[j] == n[len(n)-1-j]:
            return False
    return True

def test_is_antipalindrome():
    assert is_antipalindrome('2783') is True
    assert is_antipalindrome('2773') is False

def get_base_2(n):
    """
    functia transforma un numar n din baza 10 in baza 2
    :param n:
    :return: numarul in baza 2
    """
    baza2=''
    n = int(n)
    if n==0:
        return "0"
    while n>0:
        baza2=baza2+str(n%2)
        n//=2
    return baza2[::-1]

def test_get_base_2():
    assert get_base_2(26)=="11010"
    assert get_base_2(100) == "1100100"
    assert get_base_2(0)=="0"
    assert get_base_2(1)=="1"

def get_base_16_from_2(n):
    """
    functia transforma un numar n din baza 2 in baza 16
    :param n:
    :return: numarul in baza 16
    """
    nrb16 = ''
    cop = int (n)
    while cop:
        x = cop % 10000
        nr = 0
        p2 = 1
        while x:
            nr = (x % 10) * p2 + nr
            p2 = p2 * 2
            x = x//10
        if nr == 10:
            c = 'A'
        elif nr == 11:
            c = 'B'
        elif nr == 12:
            c = 'C'
        elif nr == 13:
            c = 'D'
        elif nr == 14:
            c = 'E'
        elif nr == 15:
            c = 'F'
        else:
            c = str(nr)
        nrb16 = c + nrb16
        cop = cop//10000
    return nrb16

def test_get_base_16_from_2():
    assert get_base_16_from_2('0111') == '7'
    assert get_base_16_from_2('111000111') == '1C7'
    assert get_base_16_from_2('10011001') == '99'

def main():
    while True:
        print('1. Verifica daca numarul este antipalindrom. ')
        print('2.Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10. ')
        print('3.Transformă un număr dat din baza 2 în baza 16.')
        print('x. Iesire')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            nr = input('Se da numarul: ')
            test_is_antipalindrome()
            if is_antipalindrome(nr) is True:
                print('Numarul este antipalindrom')
            else:
                print('Numarul NU este antipalindrom')
        elif optiune == '2':
            n = input("Alegeti un numar:")
            test_get_base_2()
            print(get_base_2(n))
        elif optiune == '3':
            m = int(input('Se da numarul in baza 2: '))
            test_get_base_16_from_2()
            print(f'Numarul in baza 16 e: ', get_base_16_from_2(m))
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

if __name__=='__main__':
    main()
