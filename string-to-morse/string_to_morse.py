#text to morse code
dict_letters_morse={"a":"*-","b":"-***","c":"-*-*","d":"-**","e":"*","f":"**-*","g":"--*","h":"****","i":"**","j":"*---","k":"-*-",
                    "l":"*-**","m":"--","n":"-*","o":"---","p":"*--*","q":"--*-","r":"*-*","s":"***","t":"-","u":"**-","v":"***-","w":"*--",
                    "x":"-**-","y":"-*--","z":"--**","1":"*----","2":"**---","3":"***--","4":"****-","5":"*****","6":"-****","7":"--***","8":"---**",
                    "0":"-----","9":"----*"
                   }

def convert(string):
    answer_list=[]
    for i in string:
        if i in dict_letters_morse:
            answer_list.append(dict_letters_morse[i])
    for i in answer_list:
        print(i)


x=input("enter a string : ")
print("morse code is : ")
convert(x)



