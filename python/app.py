def fizz_buzz (number):
    if (number % 3 == 0) and (number % 5 == 0):
        print ("fizzBuzz")
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0:
        print ("buzz")
    else:
        print (number)
    

fizz_buzz(3)
