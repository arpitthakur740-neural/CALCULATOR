num1=int(input("enter first number::"))
num2=int(input("enter second number::"))
operator = input("enter the operators----(+,-,*,/)")

if operator == "+":
    print("the sum of the numbers is:: ",num1+num2)
elif operator == "-":
    print("the difference is::",num1-num2)
elif operator == "*":
    print("the product of numbers is::",num1*num2)
elif operator == "/":
    if num2 == 0:
      print("invalid syntax")
    else:
        print("num1/num2 ::",num1/num2)
