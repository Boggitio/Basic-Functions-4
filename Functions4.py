import math
import random
import string

#1 - This functions asks for a number to be checked if it is a perfect square and returns the answer.
def checkperfsqrt(x):
    #x = int(input("What number would you like to find out if they're a perfect square?  "))

    if int(math.sqrt(x) + 0.5) ** 2 == x:
        return(f"{x}  is a perfect square.")
    else:
        return(f"{x}  is NOT a perfect square.")
#checkperfsqrt()


#2 - This function asks for a number and then it will add each digit from that number and then return the result.
def sumdig(x):
    #x = int(input("Write here the number you would like to find out the sum of it's digits:   "))
    digitsum = 0
    while x > 0:
        digit = x % 10
        digitsum += digit
        x //= 10
    return(digitsum)
#sumdig()


#3 - This function asks for a number as input and then checks if it is a palindrome and returns the result.
def isNPali(n):
    #print(n)
    if n == n[::-1]:
        return "It is a palindrome."
    else:
        return "It is not a palindrome."
#NChosen =(str(input("Check which number is a palindrome:   ")))
#print(isNPali(NChosen))

#4 - This function asks for a phrase as an input and checks which word is the most common and how many times and then
# returns the answers.
def findcommonword(phrase):
    words = phrase.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common = max(word_count, key=word_count.get)
    return(f"Most common word is |{most_common}|, and it appears {word_count[most_common]} times.")

#phrase = input("Write a phrase:  ")
#result = findcommonword(phrase)
#print(f"The most common word is '{result[0]}' and it appears {result[1]} times.")

#5 - This function generates a random password including symbols, numbers, lower case letters and uppercase letters.
# The password is between 8 and 16 characters long.

def generate_password():

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols
    password_length = random.randint(8, 16)
    password = ''.join(random.choice(all_chars) for i in range(password_length))

    return password

#print(generate_password())