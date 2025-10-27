# remdon password generator: 

import random

char = "1qaz!QAZ2wsx@WSX3edc#EDC4rfv$RFV5tgb%TGB6yhn^YHN7ujm&UJM8ik,*IK<9ol.(OL>0p;/)P:?-['_{=]+{\|.]"
length = int(input("Enter length: "))
password = ""

for a in range(length):
    password += random.choice(char)
print("Your password is: ",password)
