# Jackson J.
# 2/5/20
# String Manipulation
from Strings import *

input("*click here then press enter*".title()).title()

name = input("Hello user what is your name?"
             "\n>>>").title()

print(f"Ahh, {name}..."
      f"\n That sounds familiar"
      f"\nI get hundreds of entries a day, in fact, your my 354th user >_>"
      f"\n\nAnyhow, Welcome")

# Tell the user what they're going to do overall
print(f"Okay, {name}, what I want you to do is this:"
      f"\nType out a list of words. These words will be referred to as strings"
      f"\nPut commas in between these strings and witness magic")

input("press enter to continue".title())

Words = Strings(input("Enter your list of words here"
                      "\n>>>"))

print(length(Words))

print(first_letter(Words))

print(last_name(Words))

print(del_third_char(Words))

print(upper(Words))

print(title(Words))

print(contents_check(Words))
if contents_check(Words):
    print("")
else:
    print("")
