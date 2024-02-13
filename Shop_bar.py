import sys
import time

print("\t\t\t\t\t\t\t\t\t\twelcome to python bar!")

list = ["fanta",100]
list1=["coke",300]
list3 = ["pepsi",500]
drink= []

drink.append(list)
drink.append(list1)
drink.append(list3)

variable1 = []
variable2 = []
variable3 = []

digit1 = []
digit2 = []
digit3 = []

print("click 1 to view")
clicking = input(":")
if clicking == "1":
    for j,i in drink:
        print(j,i)

else:
    print("invalid!\nrestart the program")
    sys.exit()

def menu():
    choice =input("select your choice:")
    for item,value in drink:
        intt = []
        var =[]
        if  choice == item:
            print(item,"amount is",value)
            order = input("how many are you buying?: ")
            total = int(order) * int(value)
            print(" ")
            print("amount is",total)
            intt.append(total)
            digit1.append(total)
            variable1.append(item)
            var.append(item)
            print(item,total)
            print("item:",item,value, "|quantity:", order, "|total price:", total)


            mov = input("cont press 1\nexit(2): ")
            if mov == "1":
                try:
                    for item1, value1 in drink:
                        #print(item1, value1)
                        for i,j in drink:
                            print(i,j)
                        choice1 =input("select your choice:")
                        for item1,value1 in drink:
                            int1 = []
                            var1 =[]
                            if  choice1 == item1:
                                print(item1,"amount is",value1)
                                order1= input("how many are you buying?: ")
                                total1 = int(order1) * int(value1)
                                print("amount is",total1)
                                int1.append(total1)
                                digit2.append(total1)
                                variable2.append(item1)
                                var1.append(item1)
                                print("")
                                print(item1,total1)
                                for dig in intt:
                                    for dig1 in int1:
                                        sum_total = dig + dig1
                                        sum_amount = []
                                        sum_amount.append(sum_total)
                                        print(sum_total)
                                        print("item:",item,value, "|quantity:", order, "|total price:", total)
                                        print("item:",item1,value1, "|quantity:", order1, "|total price:", total1)
                                        break
                                    break
                                break
                            #break
                        break

                except:
                    print("error!")
                    break

                move = input("to cont press 1:")
                if move == "1":
                    for item2, value2 in drink:
                        print(item2,value2)
                    choice2 =input("select your choice:")
                    for item2,value2 in drink:
                        int3 = []
                        var2 =[]
                        if choice2 == item2:
                            print(item2,"amount is",item2)
                            order2= input("how many are you buying?: ")
                            total2 = int(order2) * int(value2)
                            print(" ")
                            print("amount is",total2)
                            int3.append(total2)
                            digit3.append(total2)
                            variable3.append(item2)
                            var2.append(item2)
                            print("")
                            print(item2,total2)
                            for dig3 in sum_amount:
                                for dig4 in int3:
                                    sum_total1 = dig3 + dig4
                                    sum_amount1 = []
                                    sum_amount1.append(sum_total1)
                                    print(sum_amount1)
                                    print("item:",item,value,"|quantity:", order, "|total price:", total)
                                    print("item:",item1,value1,"|quantity:", order1, "|total price:", total1)
                                    print("item:",item2,value2,"|quantity:", order2,"|total price:",total2)
                                    break
                                break
                            break

            deleting = input("to delete press 1\nexit(2): ")
            if deleting == "1":
                erasing = input("enter item to be remove: ")
                if erasing in variable1:
                    variable1.remove(item)
                    digit1.remove(total)
                    print("deleted")

                    for del2 in variable2:
                        for di2 in digit2:
                            while True:
                                print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                break

                    for del3 in variable3:
                        for di3 in digit3:
                            while True:
                                print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                try:
                                    over1 = sum_total1 - total
                                    print(over1)
                                    break
                                except:
                                    pass
                                    break

                elif erasing in variable2:
                    variable2.remove(item1)
                    digit2.remove(total1)
                    print("deleted")

                    for del1 in variable1:
                        for di1 in digit1:
                            while True:
                                print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                break

                    for del3 in variable3:
                        for di3 in digit3:
                            while True:
                                print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                try:
                                    over2 = sum_total1 - total1
                                    print(over2)
                                    break
                                except:
                                    pass

                elif erasing in variable3:
                    variable3.remove(item2)
                    digit3.remove(total2)
                    print("deleted")

                    for del1 in variable1:
                        for di1 in digit1:
                            while True:
                                print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                break

                    for del2 in variable2:
                        for di2 in digit2:
                            while True:
                                print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                try:
                                    over2 = sum_total1 - total2
                                    print(over2)
                                    break
                                except:
                                    pass
                                    break
                                break


                delting = input("delete(1)\nexit(2): ")
                if delting == "1":
                    erasing = input("enter item to be remove: ")
                    if erasing in variable1:
                        variable1.remove(item)
                        digit1.remove(total)
                        print("deleted")

                        for del2 in variable2:
                            for di2 in digit2:
                                while True:
                                    print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                    break

                        for del3 in variable3:
                            for di3 in digit3:
                                while True:
                                    print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                    try:
                                        over4 = sum_total1 - total
                                        # print(over4)
                                        break
                                    except:
                                        pass
                                    break

                    elif erasing in variable2:
                        variable2.remove(item1)
                        digit2.remove(total1)
                        print("deleted")

                        for del1 in variable1:
                            for di1 in digit1:
                                while True:
                                    print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                    break

                        for del3 in variable3:
                            for di3 in digit3:
                                while True:
                                    print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                    try:
                                        over5 = sum_total1 - total1
                                        # print(over5)
                                        break
                                    except:
                                        pass

                    elif erasing in variable3:
                        variable3.remove(item2)
                        digit3.remove(total2)
                        print("deleted")

                        for del1 in variable1:
                            for di1 in digit1:
                                while True:
                                    print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                    break

                        for del2 in variable2:
                            for di2 in digit2:
                                while True:
                                    print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                    try:
                                        over2 = sum_total1 - total2
                                        # print(over2)
                                        break
                                    except:
                                        pass
                                        break

                    continu = input("to delete press 1\nexit(2): ")
                    if continu == "1":
                        rasing = input("enter item to be remove: ")
                        if rasing in variable1:
                            variable1.remove(item)
                            digit1.remove(total)
                            print("deleted")

                            for del2 in variable2:
                                for di2 in digit2:
                                    while True:
                                        print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                        break

                            for del3 in variable3:
                                for di3 in digit3:
                                    while True:
                                        print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                        try:
                                            over4 = sum_total1 - total
                                            # print(over4)
                                            break
                                        except:
                                            pass

                        elif rasing in variable2:
                            variable2.remove(item1)
                            digit2.remove(total1)
                            print("deleted")

                            for del1 in variable1:
                                for di1 in digit1:
                                    while True:
                                        print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                        break

                            for del3 in variable3:
                                for di3 in digit3:
                                    while True:
                                        print("item:", del3, value2, "|quantity:", order2, "|total price:", di3)
                                        try:
                                            over6 = sum_total1 - total1
                                            # print(over6)
                                            break
                                        except:
                                            pass
                                            break

                        elif rasing in variable3:
                            variable3.remove(item2)
                            digit3.remove(total2)
                            print("deleted")

                            for del1 in variable1:
                                for di1 in digit1:
                                    while True:
                                        print("item:", del1, value, "|quantity:", order, "|total price:", di1)
                                        break

                            for del2 in variable2:
                                for di2 in digit2:
                                    while True:
                                        print("item:", del2, value1, "|quantity:", order1, "|total price:", di2)
                                        try:
                                            over7 = sum_total1 - total2
                                            # print(over7)
                                            break
                                        except:
                                            pass
                                            break
                                    break



                    elif continu == "2":
                        print(" thanks for stopping!")
                        sys.exit

                elif delting == "2":
                    print(" thanks for stopping!")
                    sys.exit

            elif deleting == "2":
                print(" thanks for stopping!")
                sys.exit


            elif mov == "2":
                print("thanks or stopping!")
                sys.exit

menu()
