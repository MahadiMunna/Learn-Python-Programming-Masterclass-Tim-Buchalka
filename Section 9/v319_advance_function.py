def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width-len(text))//2
    print(" " * left_margin, text)

def centre_text(*args, sep= " "):
    text=""
    for arg in args:
        text+=str(arg) + sep
    left_margin = (80-len(text))//2
    return " " * left_margin + text
menu = ".\\Section 9\\menu.txt"
with open(menu,'w') as menu:
    print(centre_text("spam and eggs"), file=menu)
    print(centre_text("spam, spam and eggs"), file=menu)
    print(centre_text("spam,spam,spam and eggs"), file=menu)
    print(centre_text("first","second",3,4, "spam",sep=":"), file=menu)