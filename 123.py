m=""
s=""
b=""
n=""
while 1==1:
    print("Что вы хотите узнать?")
    print("1 - Успех")
    print("2 - Здоровье")
    enter=int(input())
    if enter == 1:
        age=float(input("Введите свой возраст: "))
        if age<22:
            print("Вы молодой чоловек")
            m="молодой"
        else:
            print("Вы стары чоловек")
            s="старый"

        salary=float(input("Ваш доход в $: "))
        if salary<500:
            print("Вы нищий чоловек")
            n=" нищий"
        else:
            print("Вы богатый чоловек")
            b=" богатый"

        print("Вы",m+s+n+b, "чоловек", sep=' ')
        print("украдено goga group")
        a=str(input("press Enter to continue or press q to exit "))
        if a == "q":
            break
        else:
            continue
    elif enter == 2:
                age=float(input("Введите свой возраст: "))
                if age<22:
                    print("Вы молодой чоловек")
                    m="молодой"
                else:
                    print("Вы стары чоловек")
                    s="старый"
        
                buterbrody=float(input("Сколько бутербродов вы употребляете в день: "))
                if buterbrody>5:
                    print("Вы жырный чоловек")
                    n=" жырны"
                else:
                    print("Вы худои чоловек")
                    b=" худои"
                print("Вы",m+s+n+b, "чоловек", sep=' ')
                print("украдено goga group")
                a=str(input("press Enter to continue or press q to exit "))
                if a == "q":
                    break
                else:
                                 continue