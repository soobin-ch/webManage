global started, friend, count




started = False
friend = 1

count = 1

while count < 5 :
    count = count +1

    def school() :

        B= ""
        C= 12345678
        D= 1234.5678

        if started :
       
            if friend ==1 :
                print('ANSWER : Friend is Male')
                B = 'Male'
            else :
                print('ANSWER : Friend is Female')
                B= 'Female'
        else :
            print('ANSWER : Not defined FRIEND')
            B= 'None'
        return B, C,D, started


    
    numA = input('Key in word : ')
    numB = input ('Key in Number :')

    if numB == '1' : friend =1
    else:  friend = 0

    if numA == 'OK' : started = True
    else : started = False


    ans = school()
    print('ANSWER :' , ans)

  









