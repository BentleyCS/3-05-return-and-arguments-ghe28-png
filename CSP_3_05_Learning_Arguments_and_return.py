#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger(num1,num2):
    # n1 = input("give me a number")
    # n2 = input("give me a number")
    # n1 = int(n1)
    # n2 = int(n2)
    # if( n1 > n2):
    #     print (n1)
    # else:
    #     print (n2)
    if( num1 > num2):
        return num1
    else:
        return num2

# n1 = input("give me a number")
# n2 = input("give me a number")
ans=larger(7,12)
print(ans)
#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(g):
    if( g>=90):
        # print ("A")
        return "A"
    elif( g>= 80):
        # print ("B")
        return "B"
    elif(g >= 70):
        # print ("C")
        return "C"
    elif(g >= 60):
        # print ("D")
        return "D"
    else:
        # print ("F")
        return "F"
# g = int(input("Give me your grade"))
# answer9=grade(g)
# print(answer9)
#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz(n):
    if(n%5==0 and n%3==0):

        # print( "FizzBuzz")
        return "FizzBuzz"
    elif(n%3==0):

        # print ("fizz")
        return "fizz"
    elif(n%5==0):

        # print ("buzz")
        return "buzz"
    else:
        return n
# number1=int(input("Give me an number"))
# answer2=fizzBuzz(number1)
# print(answer2)
#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz(n):

    # n = int(n)
    if(n==1):

        return n
        # print (n)
    if(n%2==0):

        return n/2
        # print (n/2)
    else:

        return 3*n+1
        # print (3*n+1)
# number3 = int(input("Give me a number"))
# answer3=collatz(number3)
# print(answer3)

#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature(input):

    if(input[len(input)-1]=="C"):
        input = int(input[0:len(input)-1])
        out = input*(9/5)+32
        ans=(int(out))
        # print (str(int(out))+"F")
        return str(ans)+"F"
    elif(input[len(input)-1]=="F"):
        input = int(input[0:len(input)-1])
        out = (input-32)*5/9
        ans=int(out)
        return str(ans)+"C"
        # print(str(int(out))+"C")
# input1 = input("Give me a temperature")
# answer4=convertTemperature(input1)
# print(answer4)
