# 1. The app shows welcome display
print("selamat datang!")
print("")
print("""1. addition
2.subtraction
3.multiplication
4.division 
      """)


# 2. The app asks for user's option
option = input("choose your option")
print(option)

number1 = input ("insert first number")
number2 = input ("insert second number")
hasil = 0

# 3. if user want addition,do addition
if option == "1":
    hasil = (int (number1) + int (number2))
    print (hasil)
# 4. if user want subtraction,do subtraction
if option == "2":
    hasil = (int (number1) - int (number2))
    print (hasil)
# 5. if user want multiplication,do multiplication
if option == "3":
    hasil = (int (number1) * int (number2))
    print (hasil)
# 6. if user want division,do division
if option == "4":
    hasil = (int (number1) / int (number2))
    print (hasil)
# 7. The user enters option
# 8. The app show the result
# 9. The end