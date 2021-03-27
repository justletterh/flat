import os
from string import ascii_lowercase as abc

fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(*x)

outdir=fp("games")
indir=fp("a")

def main():
    print("Hello, World!!!")

def init():
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    
    #remove later
    if not os.path.exists(fp(*list(abc))):
        from gen import init as gen
        gen()
        del gen

    main()
    print("Done!!!")

if __name__=="__main__":
    init()