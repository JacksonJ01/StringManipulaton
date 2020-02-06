# Jackson J.
# 2/5/20
# String Manipulation
import time
from Strings import *


def waiting():
    time.sleep(2.5)


input("*click here then press enter*".title()).title()

name = input("Hello user what is your name?"
             "\n>>>").title()

print(f"Ahh, {name}..."
      f"\nThat sounds familiar."
      f"\nI get hundreds of entries a day, in fact, your my 354th user. >_>"
      f"\n\nAnyhow, Welcome.")

# Tell the user what they're going to do overall
print(f"Okay, {name}, what I want you to do is this:"
      f"\nType out a list of words. These words as a whole will be referred to as a string."
      f"\nPut commas in between the words, and witness magic.")

input("\npress enter to continue".title())

Words = Strings(input("Enter your list of words here:"
                      "\n>>>"))

print(length(Words))
waiting()

print(first_letter(Words))
waiting()

print(last_name(Words))
waiting()

print(del_third_char(Words))
waiting()

print(upper(Words))
waiting()

print(title(Words))
waiting()

print("\nLet's see if we have any characters other than alphabetic one; this excludes symbols.")
print(contents_check(Words))
if contents_check(Words):
    print("Cool, looks like we only have strings.")
else:
    print("Looks like there are some other characters, i.e, numbers, colons, etc.")
waiting()

print("\n",
      splitting(Words))
print("Ahh, we got \"None\", which means that's it..")
time.sleep(1.5)

input("\nWasn't that cool?"
      "\n>>>")
input("\nWell guess what, I have one more for you."
      "\nAll you have to do is press enter."
      "\n\npress enter\n".upper())

print(choice(Words))

quit()
