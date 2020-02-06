# Jackson J.
# 2/5/20
# This the the manipulation class for strings
import re


class Strings:
    def __init__(self, strings):
        self.str = strings
        return


def length(self):
    return "\nThe length of this string is " + str(len(self.str)) + " units long."


def first_letter(self):
    return "\nThe first letter of the string is " + self.str[:1]


def last_name(self):
    return "\nThe last letter of the string is " + self.str[-1]


def del_third_char(self):
    return "\nOkay, now let's delete the third character:" \
           "\n" + self.str[:2] + self.str[3:]


def upper(self):
    return f"\n{self.str}".upper()


def title(self):
    return f"\n{self.str}".title()


def contents_check(self):
    return "Let's check if there are any characters other than letters",\
           bool(re.match("abcdefghijklmnopqrstuvwxyz", self.str))


def split(self):
    return f"\n{self.str}".split()


def choice(self):
    return "" + self.str


Words = Strings("Strings, Sounds")

print(split(Words))

print(choice(Words))
