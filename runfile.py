import os

path = os.getcwd()
print("RunFile")
print("[Path]:{}\n".format(path))

while True:
    user = input("[Command]:")
    user = user.strip()
        
    if user=="":
        continue
    elif user=="quit":
        quit()
    else:
        pass
        
    try:
        li = user.split('-')
        comm = li[0]
        comm = comm.strip().lower()
        bfile = li[1]
        bfile = bfile.strip()
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    try:
        lif = bfile.split('.')
        file = lif[0]
        file = file.strip()
        ext = lif[1]
        ext = ext.strip()
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    if comm not in ['run','runfunc','funclist','findfunc','content']:
        print("[InvalidCommand]:Command '{}' doesn't exist.".format(comm))
        continue
    elif comm in ['runfunc','funclist','findfunc'] and ext!='py':
        print("[InvalidCommand]:Command '{}' works with '.py' files only.".format(comm))
        continue
    else:
        pass

    if os.path.exists(bfile)==False:
        print("[FileNotFound]:File '{}' doesn't exist.".format(bfile))
        continue

    if ext=='py':
        func=""
        if comm=='content':
            filee = open(bfile,'r')
            data = filee.read()
            print("\n{}\n".format(data))
        elif comm=='run':
            print("[Start]:{}".format(bfile))
            os.system(bfile)
            print("[Stop]:{}".format(bfile))
        elif comm=='runfunc':
            arg = input("[Function]:")
            arg = arg.strip()
            if arg=='':
                func=bfile
            elif '(' not in arg or ')' not in arg:
                print("[Error]:Function not completely defined.")
                continue
            else:
                func = file+'.'+arg
            print("[Start]:{}".format(bfile))
            
            if arg=='':
                os.system(func)
            else:
                try:
                    print("[Execute]:{}".format(func))
                    exec("import {}".format(file))
                    exec(func)
                except:
                    print("[Error]:An error occured. Check your input and try again.")
                    continue
                else:
                    pass
            print("[Stop]:{}".format(bfile))
        elif comm=='funclist':
            print()
            filee = open(bfile,'r')
            data = filee.readlines()
            for lines in data:
                funcname=""
                lines = lines.strip()
                if 'def ' in lines or 'class ' in lines:
                    lines = lines.strip(":")
                    lifunc = lines.split(" ")
                    lifunc[0]=""
                    for x in lifunc:
                        funcname = funcname+x
                        
                    if 'def ' in lines:
                        print("[Function]:"+funcname)
                    elif 'class ' in lines:
                        print("[Class]:"+funcname)
            print()
        elif comm=='findfunc':
            funct = input("[SearchFunction]:")
            print()
            filee = open(bfile,'r')
            data = filee.readlines()
            for lines in data:
                funcname=""
                lines = lines.strip()
                if 'def ' in lines or 'class ' in lines:
                    lines = lines.strip(":")
                    lifunc = lines.split(" ")
                    lifunc[0]=""
                    for x in lifunc:
                        if funct in x:
                            flag=1
                            break
                        else:
                            flag=0
                            
                    if flag==1:
                        for x in lifunc:
                            funcname = funcname+x
                            
                        if 'def ' in lines:
                            print("[Function]:"+funcname)
                        elif 'class ' in lines:
                            print("[Class]:"+funcname)
            print()

    else:
        if comm=='content':
            filee = open(bfile,'r')
            data = filee.read()
            print("\n{}\n".format(data))
        elif comm == 'run':
            print("[Start]:{}".format(bfile))
            os.system(bfile)
            print("[Stop]:{}".format(bfile))
            
            
            

    
