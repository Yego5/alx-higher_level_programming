#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Michael", "Jordan")
say_my_name("Kobe", "Bryant")
say_my_name("LeBron")
try:
    say_my_name(23, "James")
except Exception as e:
    print(e)
