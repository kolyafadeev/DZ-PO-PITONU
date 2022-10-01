a = int(input("Введите число:"))
b = int(input("Введите число:"))
num = input("введите Имя:")

def no_a(a):
     if a%5==0:
         print ("Удачно:", a%5)
     else:
         print ("Falls:", a%5)
     return ''

def no_b(b):
    if a//b==1:
        print ("Вход в систему:", a//b)
    else:
        print ("Не найдено:", a//b)
    return ''

def no_c(num):
    return num



print(no_a(a))
print(no_b(b))
print(no_c(num))




