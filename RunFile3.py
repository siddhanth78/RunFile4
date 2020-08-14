try:
    import os
except:
    print("os module rquired.")
else:
    pass


origin = os.getcwd()
path = origin
print("RunFile 3.4.1")
print("[HomePath]:{}\n".format(path))
browserPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
func=""
enable=0
enableb=0
enableac=0
contentkey = {"_data_" : '', "_datalist_" : ""}

while True:
    ok=0
    user = input("[Command]:")
    user = user.strip()
        
    if user=="":
        continue
    
    if user=="quit":
        quit()


    if user=='clear':
        os.system('cls')
        print("RunFile 3.4.1")
        print("[HomePath]:{}\n".format(path))
        continue

    if user=='enablebrowser':
        try:
            import webbrowser
        except:
            print("[PythonModuleNotFound]:webbrowser module rquired.")
            continue
        else:
            pass
        try:
            from googlesearch import *
        except:
            print("[PythonModuleNotFound]:google module required. Enter in your command line : 'pip3 install google'")
            continue
        else:
            enableb=1
            print("[BrowserSearch]:Enabled")
            print("[Warning]:May or may not give desired output. Can be disabled with 'disablebrowser' command.")
            continue


    if user=='disablebrowser':
        enableb=1
        print("[BrowserSearch]:Disabled")
        continue
        

    if user=='enablenhp':
        enable=1
        print("[NewHomePath]:Enabled")
        print("[Warning]:May or may not give desired output. Can be disabled with 'disablenhp' command.")
        continue

    if user=='disablenhp':
        enable=0
        func=""
        origin = os.getcwd()
        path=origin
        print("[NewHomePath]:Disabled")
        print("[HomePath]:{}".format(path))
        continue
    

    if user=='homepath':
        path=origin
        func=""
        print("[NewPath]:{}".format(path))
        continue

    for comms in ['homepath','delpath','showpath','quit','newhomepath','delfile','createfile','addcontent','storecontent',
                    'runfile','runfunc','funclist','findfunc','content','addpath','findpath','browse','_data_','_data_reset_',
                  '_datalist_','_datalist_reset_','storecontentaslines','_fromdatalist_']:
        if comms in user:
            ok=1
            break
    else:
        ok=0
        
    if ok==0:
        print("[InvalidCommand]:Command '{}' doesn't exist. Enter 'help' for more info.".format(user))
        continue
    else:
        pass

    if user=='_data_':
        print(contentkey.get('_data_'))
        continue

    if user=='_data_reset_':
        contentkey['_data_'] = ''
        print("[_data_]:Contents of _data_ has been deleted.")
        continue

    if user=='_datalist_':
        print(contentkey.get('_datalist_'))
        continue

    if user=='_datalist_reset_':
        contentkey['_datalist_'] = ''
        print("[_datalist_]:Contents of _data_ has been deleted.")
        continue

    if user=='showpath':
        print()
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
        print()
        continue

    if user=="help":
        print()
        print("RunFile v3.4.1")
        print("Used to access and run files with ease.")
        print("Commands:\n")
        print("showpath                      : List all the available directories and files in your current path.")
        print("addpath>dir/subdir            : Add a dir to your original path.")
        print("findpath>dir/subdir           : Check and display all dirs or files which match.")
        print("delpath                       : Remove last added dir or subdir from path.")
        print("homepath                      : Go back to original path.")
        print("delfile>filename              : Delete the specified file.")
        print("createfile>filename           : Create file of specified name.")
        print("content>filename              : Display content of a file.")
        print("clearcontent>filename         : Clear content of a file.")
        print("storecontent>filename         : Store content of a file in a variable with name '_data_'.")
        print("storecontentaslines>filename  : Store lines of a file in a list with name '_datalines_'.")
        print("_data_                        : Display stored file data.")
        print("_datalist_                        : Display stored file lines data.")
        print("_datalist_>linenumber         : Display specified line.")
        print("_fromdatalist_>linenumber     : Store a line from _datalist_ into _data_.")
        print("runfile>filename              : Run or open specified file.")
        print("runfunc>filename              : Access and run a function in a '.py' file.")
        print("findfunc>filename             : Find a function or functions in a '.py' file>")
        print("funclist>filename             : List all the classes and functions in a '.py' file.")
        print("quit                          : Exit runfile.")
        print()
        continue

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
        print("[NewPath]:{}".format(path))
        continue

    if ">" not in user:
        print("[Error]:Command and file name must be seperated by '>'.")
        continue
        
    try:
        li = user.split('>')
        comm = li[0]
        comm = comm.strip().lower()
        bfile = li[1]
        bfile = bfile.strip()
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    if comm=='_datalist_':
        if bfile.isnumeric()==False:
            print("[Error]:Line number required.")
            continue
        elif bfile.isnumeric()==True:
            try:
                bfile = int(bfile)
            except:
                print("[Error]:_datalist_ accepts numbers only.")
            else:
                try:
                    print("[Line {0}]:{1}".format(bfile,contentkey.get('_datalist_')[bfile-1].strip("\n")))
                except:
                    print("[Error]:Line number out of range.")
                else:
                    pass
            continue

    if comm=='_fromdatalist_':
        if bfile.isnumeric()==False:
            print("[Error]:Line number required.")
            continue
        elif bfile.isnumeric()==True:
            try:
                bfile = int(bfile)
            except:
                print("[Error]:_datalist_ accepts numbers only.")
            else:
                try:
                    contentkey['_data_'] = contentkey.get('_datalist_')[bfile-1].strip("\n")
                    print("[_fromdatalist_]:Specified _datalist_ content has been stored in _data_. Use key '_data_' to access the content.")
                except:
                    print("[Error]:Line number out of range.")
                else:
                    pass
            continue

    if bfile=='_data_':
        bfile = contentkey.get('_data_')

    if bfile=='_datalist_':
        bfile = contentkey.get('_datalist_')

    if comm=='createfile':
        if os.path.exists(path+"\\"+bfile)==True:
            print("[FileExists]:File '{}' already exists.".format(bfile))
        else:
            try:
                filee = open(path+"\\"+bfile,'x')
                filee.close()
            except:
                print("[Error]:An error occured. Check your input and try again.")
            else:
                print("[FileCreated]:File '{}' has been created.".format(bfile))
        continue


    if comm=='delfile':
        try:
            os.remove(path+"\\"+bfile)
        except:
            print("[FileNotFound]:File '{}' doesn't exist.".format(bfile))
        else:
            print("[FileDeleted]:File '{}' has been deleted.".format(bfile))
        continue
    

    if comm=='browse' and enableb==1:
        print("[BrowserSearch]:{}".format(bfile))
        browse_path = browserPath
        for url in search(bfile, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % bfile)
        continue
    elif comm=='browse' and enableb==0:
        print("[InvalidCommand]:Command '{}' doesn't exist. Enter 'help' for more info.".format(comm))
        continue
        

    if comm=='findpath':
        print()
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                if bfile.lower() in name.lower():
                    print(os.path.join(root, name))
            for name in dirs:
                if bfile.lower() in name.lower():
                    print(os.path.join(root, name))
        print()
        continue


    if comm=='newhomepath' and enable==1:
        origin=bfile.replace("/","\\")
        if os.path.exists(pt:=origin)==False:
            print(f"[InvalidPathOperation]:Path '{pt}' doesn't exist.")
            origin = os.getcwd()
            path=origin
            func=""
            print("[HomePath]:{}".format(origin))
            continue
        else:
            path=origin
            func=""
            print("[NewHomePath]:{}".format(origin))
            continue
    elif comm=='newhomepath' and enable==0:
        print("[InvalidCommand]:Command '{}' doesn't exist. Enter 'help' for more info.".format(comm))
        continue


    if comm=='addpath':
        if "." in bfile:
            print("[InvalidPathOperation]:Cannot add file to path.")
            continue
        if os.path.exists(pt:=(path+"\\"+bfile))==False:
            print(f"[InvalidPathOperation]:Path '{pt}' doesn't exist.")
            continue
        path = path+"\\"+bfile
        bfile = bfile.replace("/",".")
        bfile = bfile.replace("\\",".")
        if func.strip()=="":
            func=bfile
        else:
            func = func+"."+bfile
        func=func.strip()
        print("[NewPath]:{}".format(path))
        if bfile[0]=='.' or bfile[0]=='.':
            print("[Warning]:[Command:addpath]:Dir/subdir beginning with '/' or '\\' may result in wrong path.")
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

    if comm not in ['runfile','runfunc','funclist','findfunc','content','storecontent','storecontentaslines',
                    'newhomepath','addpath','browse','findpath','addcontent','_fromdatalist_']:
        print("[InvalidCommand]:Command '{}' doesn't exist. Enter 'help' for more info.".format(comm))
        continue
    elif comm in ['runfunc','funclist','findfunc'] and ext!='py':
        print("[InvalidCommand]:Command '{}' works with '.py' files only.".format(comm))
        continue
    else:
        pass

    if os.path.exists(path+"\\"+bfile)==False:
        print("[FileNotFound]:File '{}' doesn't exist.".format(bfile))
        continue


    if comm=='storecontentaslines':
        filee = open(path+"\\"+bfile,'r')
        data = filee.readlines()
        filee.close()
        contentkey["_datalist_"] = data
        print("[_datalist_]:File content has been stored. Use key '_datalist_' to access the content.")
    elif comm=='content':
        filee = open(path+"\\"+bfile,'r')
        data = filee.read()
        print("\n{}\n".format(data.strip("\n")))
        filee.close()
    elif comm=='clearcontent':
        filee = open(path+"\\"+bfile,'w')
        file.write("")
        filee.close()
        print("[FileCleared]:File content has been deleted.")
    elif comm=='storecontent':
        filee = open(path+"\\"+bfile,'r')
        data = filee.read()
        filee.close()
        contentkey["_data_"] = data.strip()
        print("[_data_]:File content has been stored. Use key '_data_' to access the content.")
        continue


    if comm=='addcontent':
        enableac=1
        sub=0
        print("[Startfile]:{}".format(bfile))
        while enableac==1:
            try:
                file = open(path+"\\"+bfile,'a')
                con = input(" "*sub+"[Line]:")
                if con=='[sub]':
                    sub+=4
                    continue
                if con=='[endsub]':
                    sub=sub-4
                    if sub<=0:
                        sub=0
                    continue
                if '_data_' in con:
                    con = con.replace("_data_",contentkey.get('_data_').strip("\n"))
                    if con.strip()=='':
                        con='_data_'
                    else:
                        pass
                if '_datalist_>' in con:
                    conn = con
                    liconn = conn.split(">")
                    lineno = liconn[1].strip()
                    lineno = lineno.strip('\n')
                    if lineno.isnumeric()==False:
                        print("[Error]:Line number required.")
                        continue
                    elif lineno.isnumeric()==True:
                        lineno = int(lineno)
                        try:
                            con = conn.replace("_datalist_>"+str(lineno),contentkey.get('_datalist_')[lineno-1].strip("\n"))
                        except:
                            print("[Error]:Line number out of range.")
                            continue
                        else:
                            pass
                if '_datalist_' in con:
                    con = con.replace("_datalist_",contentkey.get('_datalist_'))
                if con=='[endfile]':
                    file.close()
                    enableac=0
                    print("[FileUpdated]:New content has been added.")
                    break
                file.write(" "*sub+con+"\n")
            except:
                print("[Error]:An unexpected error occured. File will be closed.")
                file.close()
                enableac=0
                break
            else:
                pass
        file.close()
            

    if ext=='py':
        if comm=='runfile':
            print("[Start]:{}".format(bfile))
            os.system(r"{}".format(path+"\\"+bfile))
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
            filee.close()
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
            filee.close()
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
        if comm == 'runfile':
            print("[Start]:{}".format(bfile))
            webbrowser.open(r"{}".format(path+"\\"+bfile))
            print("[Stop]:{}".format(bfile))
            
            
            

    
