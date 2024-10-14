def geet(fx):
    def mfx(*args,**kwargs):
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@geet
def add (a,b):
    print(a+b)

add(1,2)
