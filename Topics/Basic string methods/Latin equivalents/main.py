the_name = input()


def normalize(name):
    name = name.replace("é", "e")
    name = name.replace("ë", "e")
    name = name.replace("á", "a")
    name = name.replace("å", "a")
    name = name.replace("œ", "oe")
    name = name.replace("æ", "ae")
    return name


print(normalize(the_name))
