import os
from time import sleep
from string import ascii_lowercase as abc
from shutil import rmtree as rmdir

fp=lambda *x:os.path.join(".",*x)
j=lambda *x:os.path.join(*x)

def touch(f,*,dat=""):
    f=open(f,"w")
    f.write(dat)
    f.close()

def main(*,exts=[f".{x}" for x in "gba,gb,gbc,nds,3ds".split(",")],outdir=fp("games")):
    l=list(abc)
    tmp=[]
    for i in l:
        tmp.append(i)
        os.mkdir(fp(*tmp))
        for e in exts:
            touch(fp(*[*tmp,"".join([i,e])]))
    if not os.path.exists(outdir):
        os.mkdir(outdir)

def init(*,cooldown=1):
    try:
        main()
    except FileExistsError:
        rmdir(fp("a"))
        sleep(cooldown)
        main()

if __name__=="__main__":
    init()