while True:
    while True:
      try:       
         first_number = float(input("enter first number: "))
         break 
      except ValueError:
       print("invalid input, please enter a numeric value") 
                   
    while True:
      try:
         operation = input("enter operation type: ")
         if operation in ("/","+","*","-"):
           break
         else:
           raise ValueError
      except ValueError:
        print("invalid operator , please enter +,*,-,/") 
      
    while True:
      try:
       second_number = float(input("enter second number: "))
       if second_number == 0 and operation == "/":
         raise ZeroDivisionError
       break
      except ValueError:
        print("invalid value, please enter a numeric value")
      except ZeroDivisionError:
           print("cannot divide by zero , please enter another numeric value")
 #print result:
    if operation == "+":
      result = first_number + second_number
    elif operation == "-":
       result = first_number - second_number
    elif operation == "*":
      result = first_number * second_number
    elif operation == "/":
      result = first_number / second_number
    else:
     result = None
    if result != None:
      print("the result is",result)
    else:
      print("unexpected error ")
    repeat =  input("do you want to prefore another operation ?(Yes/No)").strip().lower()
    if repeat == "no":
      break
print("program is closed")