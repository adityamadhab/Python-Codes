#Higher order function 

def shout(text) :
    return text.upper()
def whisper(text) :
    return text.lower()

def greet(func) :
    greetings=func("Hi everyone")
    print(greetings)

greet(shout)
greet(whisper)