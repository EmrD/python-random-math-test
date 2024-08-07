import random

dogru_say = 0
yanlis_say = 0

operations = ['+', '-']

def hesapla():
    global dogru_say, yanlis_say
    islem = random.choice(operations)
    
    try:
        say1 = random.randint(1, 50)
        say2 = random.randint(1, say1)
        
        if islem == '+':
            print(f'{say1} + {say2}')
            cevap = int(input('Cevap: '))
            if cevap == say1 + say2:
                print('Tebrikler Doğru Cevap')
                dogru_say += 1
            else:
                print('Yanlış Cevap!')
                yanlis_say += 1
        elif islem == '-':
            print(f'{say1} - {say2}')
            cevap = int(input('Cevap: '))
            if cevap == say1 - say2:
                print('Tebrikler Doğru Cevap')
                dogru_say += 1
            else:
                print('Yanlış Cevap')
                yanlis_say += 1
        
        print("Doğru Sayınız: ", dogru_say)
        print("Yanlış Sayınız: ", yanlis_say)
        
        print("\nYeni bir soru için Enter tuşuna basın veya çıkmak için 'q' tuşuna basın.")
        if input().strip().lower() != 'q':
            hesapla()
        else:
            print("Oyundan çıkılıyor. Sonuçlarınız:")
            print("Doğru Sayınız: ", dogru_say)
            print("Yanlış Sayınız: ", yanlis_say)
            exit()
    
    except ValueError:
        print('Lütfen geçerli bir sayı girin.')
        hesapla()
    except KeyboardInterrupt:
        print('Çıkış Yapılıyor.')
        exit()

hesapla()