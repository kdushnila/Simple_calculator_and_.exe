import eel
import operator


allowed_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}


@eel.expose
def get_cal(text: str):
    t = ""
    a = text
    for i in text:
        if i.isdigit():
            pass
        else:
            t = i
    a = a.split(t)
    return allowed_operators[t](int(a[0]), int(a[1]))


eel.init("web")

eel.start("main.html", size=(800, 340))
