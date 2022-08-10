num1 = 20
num2 = 30.5

num1 = num1+num2

print(type(num1), type(num2))


num3 = 5.8
print(num3)
num4 = int(num3)
print(num4)

edad = input("tu edad")
print(type(edad))
edad = int(edad)
nueva_edad = edad + 1
print(type(edad))

print("tu edad el proximo año sera de: " + str(nueva_edad))
print("tu edad actual es {} y el otro año sera de {}".format(edad, nueva_edad))
print(f"tu edad actual es de {edad} y el proximo año sera de {nueva_edad}")
