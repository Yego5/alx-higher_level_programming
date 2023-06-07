#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sign_numt = {-1: "negative",0: "zero",1: "positive"
}
k = -1 if number < 0 else 1 if number > 0 else 0
print("{} is {}".format(number, sign_num[k]))
