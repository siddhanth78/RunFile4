import os

origin = os.getcwd()
path = os.getcwd()
print("RunFile")
print("[OriginalPath]:{}\n".format(path))
func=""

while True:
    user = input("[Command]:")
    user = user.strip()
        
    if user=="":
        continue
    elif user=="quit":
        quit()
    else:
        pass

    if user=='showpath':
        print()
        for root, dirs, files in os.walk(".", topdown=False):
           for name in files:
              print(os.path.join(root, name))
           for name in dirs:
              print(os.path.join(root, name))
        print()
        continue

    if user=="help":
        print()
        print("RunFile v1.3.")
        print("Used to access and run files with ease.")
        print("Commands:\n")
        print("showpath             : Lists all the available directories and sub-directories.")
        print("addpath:<dir/subdir> : Adds a dir or subdir to your original path.")
        print("delpath              : Removes last added dir or subdir from path.")
        print("content:<filename>   : Displays content of the file.")
        print("runfile:<filename>   : Runs or opens specified file.")
        print("runfunc:<filename>   : Access and run a function in a '.py' file.")
        print("findfunc:<filename>  : Find a function in a '.py' file>")
        print("funclist:<filename>  : Lists all the classes and functions in a '.py' file.")
        print("quit                 : Exit runfile.")
        print()

    if user=='delpath':
        if path==origin:
           print("[InvalidPathOperation]:Cannot delete from original path.")
           continue
        count=0
        lipath = path.split("\\")
        lipath.pop(-1)
        path=""
        for l in lipath:
            count+=1
            if count==len(lipath):
                path=path+l
                break
            path = path+l+"\\"
        fucount=0
        if "." not in func:
            func=""
        else:
            lifu = func.split(".")
            lifu.pop(-1)
            func=""
            for fu in lifu:
                fucount+=1
                if fucount==len(lifu):
                    func=func+fu
                    break
                func=func+fu+"."
        func=func.strip()
        print("[NewPath]:{}\n".format(path))
        continue

    if ":" not in user:
        print("[Error]:Command and file name must be seperated by ':'.")
        continue
        
    try:
        li = user.split(':')
        comm = li[0]
        comm = comm.strip().lower()
        bfile = li[1]
        bfile = bfile.strip()
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    if comm=='addpath':
        if "." in bfile:
            print("[InvalidPathOperation]:Cannot add file to path.")
            continue
        if os.path.exists(path+"\\"+bfile)==False:
            print("[InvalidPathOperation]:Such directory doesn't exist.")
            continue
        path = path+"\\"+bfile
        if func.strip()=="":
            func=bfile
        else:
            func = func+"."+bfile
        func=func.strip()
        print("[NewPath]:{}\n".format(path))
        continue

    try:
        lif = bfile.split('.')
        file = lif[0]
        file = file.strip()
        ext = lif[1]
        ext = ext.strip()
        file = file.replace("/",".")
        file = file.replace("\\",".")
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    if comm not in ['runfile','runfunc','funclist','findfunc','content']:
        print("[InvalidCommand]:Command '{}' doesn't exist.".format(comm))
        continue
    elif comm in ['runfunc','funclist','findfunc'] and ext!='py':
        print("[InvalidCommand]:Command '{}' works with '.py' files only.".format(comm))
        continue
    else:
        pass

    if os.path.exists(path+"\\"+bfile)==False:
        print("[FileNotFound]:File '{}' doesn't exist.".format(bfile))
        continue

    if ext=='py':
        if comm=='content':
            filee = open(path+"\\"+bfile,'r')
            data = filee.read()
            print("\n{}\n".format(data))
        elif comm=='runfile':
            print("[Start]:{}".format(bfile))
            os.system(path+"\\"+bfile)
            print("[Stop]:{}".format(bfile))
        elif comm=='runfunc':
            arg = input("[Function]:")
            arg = arg.strip()
            if arg=='':
                pass
            elif '(' not in arg or ')' not in arg:
                print("[Error]:Function not completely defined.")
                continue
            else:
                if func.strip()=="":
                    runfunc = file+'.'+arg
                else:
                    runfunc = func+'.'+file+'.'+arg
            print("[Start]:{}".format(bfile))
            
            if arg=='':
                os.system(path+"\\"+bfile)
            else:
                try:
                    print("[Execute]:{}".format(runfunc))
                    if func=="":
                        exec("import {}".format(file))
                    else:
                        exec("import {}".format(func+'.'+file))
                    exec(runfunc)
                except:
                    print("[Error]:An error occured. Check your input and try again.")
                    continue
                else:
                    pass
            print("[Stop]:{}".format(bfile))
        elif comm=='funclist':
            print()
            filee = open(path+"\\"+bfile,'r')
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
            filee = open(path+"\\"+bfile,'r')
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
            filee = open(path+"\\"+bfile,'r')
            data = filee.read()
            print("\n{}\n".format(data))
        elif comm == 'runfile':
            print("[Start]:{}".format(bfile))
            os.system(path+"\\"+bfile)
            print("[Stop]:{}".format(bfile))
            
            
            

    
