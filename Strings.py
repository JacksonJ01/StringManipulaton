# Jackson J.
# 2/5/20
# This the the manipulation class for strings


class Strings:
    def __init__(self, strings):
        self.str = strings
        return


def length(self):
    return f"\nThe length of this string is " + str(len(self.str)) + " units long."


def first_letter(self):
    return "\nThe first letter of this strings is: " + self.str[:1] + "."


def last_name(self):
    return "\nThe last letter of this string is: " + self.str[-1] + "."


def del_third_char(self):
    return "\nOkay, now let's delete the third character in " + self.str + ":" \
           "\n" + self.str[:2] + self.str[3:] + "."


def upper(self):
    return "\nLook at this!" \
           f"\n{self.str}".upper() + \
           "\nCaps lock.".upper()


def title(self):
    return "\nAnd this too!" \
           f"\n{self.str}".title() + \
           "\nthis on is called title case".title()


def contents_check(self):
    allowed = "abcdefghijklmnopqrstuvwxyz "
    return set(self.str).issubset(allowed)


def splitting(self):
    data = self.str.split(", ")
    for commas in data:
        print(commas)
    return


def choice(self):
    return "\nI will add something special to your string" \
           f"\n{self.str}".__add__(f"\n\nThanks for playing with me. I had a lot of fun"
                                   f"See you around")
