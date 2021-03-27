import os
from string import ascii_lowercase as abc
from shutil import copy2 as cp
from shutil import rmtree as rmdir

fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(*x)
fn=lambda f:f.split(os.path.sep)[-1]
ext=lambda f:f'.{fn(f).split(".")[-1]}'
fix=lambda f:j(*os.path.split(f)[:-1],".".join([x.lower() if x==fn(f).split(".")[-1] else x for x in fn(f).split(".")]))

outdir=fp("games")
indir=fp("a")
exts=[f".{x}" for x in "gba,gb,gbc,nds,3ds".split(",")]

def look(f):
    do=lambda f:[[j(x[0],xx) for xx in x[2]] for x in os.walk(f)]
    l=[]
    for i in do(f):
        for ii in i:
            if ext(ii) in exts:
                l.append(ii)
    return l

def main():
    l=look(indir)
    for i in l:
        cp(i,fix(fp(outdir,fn(i))))

def init():
    if os.path.exists(outdir):
        rmdir(outdir)
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