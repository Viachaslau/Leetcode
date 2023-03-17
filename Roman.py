
def rom_num(num):
    rome_num=''
    while True:
        a=len(str(num))
        if num==0:
            break
        else:
            if a==1:
                if 1<=num<4:
                    rome_num+=str(''.join(['I']*num))
                    break
                elif num==4:
                    rome_num+='IV'
                    break
                elif num==5:
                    rome_num+='V'
                    break
                elif 5<num<9:
                    rome_num+='V'+str(''.join(['I']*(num-5)))
                    break
                elif num==9:
                    rome_num+='IX'
                    break
                else:
                    break
            elif a==2:
                if 10<=num<40:
                    rome_num+=str(''.join(['X']*(num//10)))
                    num=num%10
                elif 40<=num<50:
                    rome_num+='XL'
                    num=num%10
                elif 50<=num<90:
                    rome_num+='L'+str(''.join(['X']*((num//10)-5)))
                    num=num%10
                elif num>=90:
                    rome_num+='XC'
                    num=num%10
                else:
                    break
            elif a==3:
                if 100<=num<400:
                    rome_num+=str(''.join(['C']*(num//100)))
                    num=num%100
                elif 400<=num<500:
                    rome_num+='CD'
                    num=num%100
                elif 500<=num<900:
                    rome_num+='D'+str(''.join(['C']*((num//100)-5)))
                    num=num%100
                elif num>=900:
                    rome_num+='CM'
                    num=num%100
                else:
                    break
            elif a==4:
                if 1000<=num<4000:
                    rome_num+=str(''.join(['M']*(num//1000)))
                    num=num%1000
                elif 4000<=num:
                    return("The number out of range!")
                else:
                    break
            
    return(rome_num)
        