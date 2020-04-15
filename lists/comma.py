spam = ['apples', 'pizza', 'tofu', 'cats']

def comma(items):
    """Takes a list and prints it as an Oxford comma denoted sentence."""
    for i in range(len(items)-2):
        print(items[i], end=", ")
    print(items[-2] + ', and ' + items[-1])

comma(spam)
