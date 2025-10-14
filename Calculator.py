while True:
    num1 = float(input("Enter first Number: "))
    operator = input("Enter oprator: ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result = num1*num2
    elif operator == '/':
        if num2 !=0:
            result = num1/num2
        else:
            result = "Earror"

    print("result: ",result)

    count = input("Do you continue this:Yar/No: ").lower()
    if count!='yas':  
        break
