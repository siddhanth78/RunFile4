import os
import webbrowser
import subprocess
import sys

try:
    import keyboard
except:
    print("[PythonModuleNotFound]:Installing module keyboard.\n")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','keyboard'])
    print()
    import keyboard
else:
    pass
    

origin = os.getcwd()
path = origin
print("RunFile 3.4.5")
print("[HomePath]:{}\n".format(path))
browserPath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
func=""
enable=0
enableb=0
contentkey = {"_file_" : '', "_lines_" : ""}
user=''
historydir = path+'\\.runfile_history'
licommand=[]

commandlist = ['homepath','delpath','showpath','quit','newhomepath','delfile','createfile','addcontent','store',
            'runfile','runfunc','funclist','findfunc','content','addpath','findpath','browse','_file_','_file_reset_',
            '_lines_','_lines_reset_','storelines','_fromlines_','RunFile','clearcontent','clr','clear']

if os.path.exists(historydir)==True:
    filehist = open(historydir,'r')
    histdata = filehist.readlines()
    filehist.close()
    for i in range(0,len(histdata)):
        histdata[i] = histdata[i].strip()
        histdata[i] = histdata[i].strip('\n')

if os.path.exists(historydir)==False:
    filee = open(historydir,'x')
    filee.close()
    filehist = open(historydir,'r')
    histdata = filehist.readlines()
    filehist.close()
    for i in range(0,len(histdata)):
        histdata[i] = histdata[i].strip()
        histdata[i] = histdata[i].strip('\n')

counthist=-1
countrevhist=len(histdata)+counthist
hc=0
rhc=0
beg=0

def history_list():
    global histdata,counthist,countrevhist,hc,rhc,beg
    keyboard.press_and_release('shift+end')
    keyboard.press_and_release('backspace')
    try:
        if beg==0:
            beg=1
        elif hc==0 and beg!=0:
            counthist-=1
        countrevhist=len(histdata)+counthist
        keyboard.write(histdata[counthist])
        counthist-=1
        if counthist==-len(histdata)-1:
            counthist+=1
            countrevhist=len(histdata)+counthist
    except:
        keyboard.write('')
    finally:
        hc=1
        rhc=0

def rev_history_list():
    global histdata,counthist,countrevhist,hc,rhc,beg
    keyboard.press_and_release('shift+end')
    keyboard.press_and_release('backspace')
    try:
        if beg==0:
            beg=1
        elif rhc==0 and beg!=0:
            countrevhist+=1
        counthist=-len(histdata)+countrevhist
        keyboard.write(histdata[countrevhist])
        countrevhist+=1
        if countrevhist==len(histdata):
            countrevhist-=1
            counthist=-len(histdata)+countrevhist
    except:
        keyboard.write('')
    finally:
        hc=0
        rhc=1
    
keyboard.add_hotkey('up arrow',history_list)
keyboard.add_hotkey('down arrow',rev_history_list)

while True:
    counthist=-1
    ok=0
    if user=='':
        pass
    else:
        histdata.append(user)
        filee = open(historydir,'a')
        filee.write(user+'\n')
        filee.close()

    user = input("[Command]:")
    user = user.strip()
        
    if user=="":
        continue

    if user=="help":
        print()
        print("RunFile v3.4.5")
        print("Commands:\n")
        print("showpath               : List all the available directories and files in your current path.")
        print("addpath>dir/subdir     : Add a dir to your original path.")
        print("findpath>dir/subdir    : Check and display all dirs or files which match.")
        print("delpath                : Remove last added dir or subdir from path.")
        print("homepath               : Go back to original path.")
        print("delfile>filename       : Delete the specified file.")
        print("createfile>filename    : Create file of specified name.")
        print("content>filename       : Display content of a file.")
        print("clearcontent>filename  : Clear content of a file.")
        print("store>filename         : Store content of a file and extract with key '_file_'.")
        print("storelines>filename    : Store lines of a file and extract with key '_lines_'.")
        print("_file_                 : Use to get stored file data.")
        print("_lines_                : Use to get stored file lines.")
        print("_lines_>linenumber     : Use to get specified line from _lines_.")
        print("_fromlines_>linenumber : Store a line from _lines_ into _file_.")
        print("_file_reset_           : Clear data stored in _file_.")
        print("_lines_reset_          : Clear data stored in _lines_.")
        print("runfile>filename       : Run or open specified file. Output of code will be displayed on a different teminal.")
        print("runfunc>filename       : Access and run a function in a '.py' file.")
        print("findfunc>filename      : Find a function or functions in a '.py' file>")
        print("funclist>filename      : List all the classes and functions in a '.py' file.")
        print("RunFile>filename       : Mark a '.py' file to display output of the code on the runfile terminal.")
        print("clear/clr              : Clear runfile terminal.")
        print("quit                   : Exit runfile.")
        print()
        continue

    if user=='enablebrowser':
        try:
            from googlesearch import *
        except:
            print("[PythonModuleNotFound]:Installing module google.")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install','google'])
            print()
            from googlesearch import *
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
        print("[Newhomepath]:Enabled")
        print("[Warning]:May or may not give desired output. Can be disabled with 'disablenhp' command.")
        continue

    if user=='disablenhp':
        enable=0
        func=""
        origin = os.getcwd()
        path=origin
        print("[Newhomepath]:Disabled")
        print("[homepath]:{}".format(path))
        continue

    for comms in commandlist:
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

    if user=='clear' or user=='clr':
        os.system('cls')
        print("RunFile 3.4.5")
        print("[HomePath]:{}\n".format(path))
        continue

    if user=="quit":
        quit()

    if user=='homepath':
        path=origin
        func=""
        print("[HomePath]:{}".format(path))
        continue

    if user=='_file_':
        print(contentkey.get('_file_'))
        continue

    if user=='_file_reset_':
        contentkey['_file_'] = ''
        print("[_file_]:Contents of _file_ has been deleted.")
        continue

    if user=='_lines_':
        print(contentkey.get('_lines_'))
        continue

    if user=='_lines_reset_':
        contentkey['_lines_'] = ''
        print("[_lines_]:Contents of _file_ has been deleted.")
        continue

    if user=='showpath':
        print()
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                print("[File]:"+os.path.join(root, name))
            for name in dirs:
                print("[Directory]:"+os.path.join(root, name))
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
        print("[Error]:Command and request must be seperated by '>'.")
        continue
        
    try:
        li = user.split('>')
        comm = li[0]
        comm = comm.strip()
        bfile = li[1]
        bfile = bfile.strip()
    except:
        print("[Error]:An error occured. Check your input and try again.")
        continue
    else:
        pass

    if comm not in commandlist:
        print("[InvalidCommand]:Command '{}' doesn't exist. Enter 'help' for more info.".format(user))
        continue

    if comm=='_lines_':
        if bfile.isnumeric()==False:
            print("[Error]:Line number required.")
            continue
        elif bfile.isnumeric()==True:
            try:
                bfile = int(bfile)
            except:
                print("[Error]:_lines_ accepts numbers only.")
            else:
                try:
                    print("[Line {0}]:{1}".format(bfile,contentkey.get('_lines_')[bfile-1].strip("\n")))
                except:
                    print("[Error]:Line number out of range.")
                else:
                    pass
            continue

    if comm=='_fromlines_':
        if bfile.isnumeric()==False:
            print("[Error]:Line number required.")
            continue
        elif bfile.isnumeric()==True:
            try:
                bfile = int(bfile)
            except:
                print("[Error]:_lines_ accepts numbers only.")
            else:
                try:
                    contentkey['_file_'] = contentkey.get('_lines_')[bfile-1].strip("\n")
                    print("[_fromdatalist_]:Specified _lines_ content has been stored in _file_. Use key '_file_' to access the content.")
                except:
                    print("[Error]:Line number out of range.")
                else:
                    pass
            continue

    if bfile=='_file_':
        bfile = contentkey.get('_file_')

    if bfile=='_lines_':
        bfile = contentkey.get('_lines_')

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
        if "-" in func:
            print("[Warning]:Invalid character '-' found. Files may or may not open and 'runfunc' will not work.")
        print("[NewPath]:{}".format(path))
        if bfile[0]=='.' or bfile[0]=='.':
            print("[Warning]:Dir/subdir request beginning with '/' or '\\' may result in wrong path.")
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

    if comm in ['runfunc','funclist','findfunc'] and ext!='py':
        print("[InvalidCommand]:Command '{}' works with '.py' files only.".format(comm))
        continue
    else:
        pass

    if os.path.exists(path+"\\"+bfile)==False:
        print("[FileNotFound]:File '{}' doesn't exist.".format(bfile))
        continue


    if comm=='storelines':
        filee = open(path+"\\"+bfile,'r')
        data = filee.readlines()
        filee.close()
        contentkey["_lines_"] = data
        print("[_lines_]:File content has been stored. Use key '_lines_' to access the content.")
    elif comm=='content':
        filee = open(path+"\\"+bfile,'r')
        data = filee.read()
        print("\n{}\n".format(data.strip("\n")))
        filee.close()
    elif comm=='clearcontent':
        filee = open(path+"\\"+bfile,'w')
        filee.write("")
        filee.close()
        print("[FileCleared]:File content has been deleted.")
    elif comm=='store':
        filee = open(path+"\\"+bfile,'r')
        data = filee.read()
        filee.close()
        contentkey["_file_"] = data.strip()
        print("[_file_]:File content has been stored. Use key '_file_' to access the content.")
        continue


    if comm=='RunFile':
        filee = open(path+"\\"+bfile,'a')
        filee.write("#RunFile\n")
        filee.close()
        if ext=="py":
            print("[RunFile]:The output of this file will now be displayed on the terminal.")
        continue

    if comm=='addcontent':
        enableac=1
        sub=0
        print("[Startfile]:{}".format(bfile))
        while True:
            try:
                file = open(path+"\\"+bfile,'a')
                con = input(" "*sub+"[Line]:")
                if con=='[sub]':
                    sub+=4
                    continue
                if con=='[RunFile]':
                    con = "#RunFile"
                if con=='[endsub]':
                    sub=sub-4
                    if sub<=0:
                        sub=0
                    continue
                if '_file_' in con:
                    con = con.replace("_file_",contentkey.get('_file_').strip("\n"))
                    if con.strip()=='':
                        con='_file_'
                    else:
                        pass
                if '_lines_>' in con:
                    conn = con
                    liconn = conn.split("_lines_>")
                    for lines in liconn:
                        lines = lines.strip('\n')
                        if lines.strip()=="":
                            continue
                        elif (lineno:=lines[0]).isnumeric()==False:
                            continue
                        elif (lineno:=lines[0]).isnumeric()==True:
                            lineno = int(lineno)
                            try:
                                con = conn.replace("_lines_>"+str(lineno),contentkey.get('_lines_')[lineno-1].strip("\n"))
                            except:
                                print("[Error]:Line number out of range.")
                                continue
                            else:
                                pass
                if '_lines_' in con:
                    con = con.replace("_lines_",contentkey.get('_lines_'))
                if con=='[endfile]':
                    file.close()
                    enableac=0
                    print("[FileUpdated]:New content has been added.")
                    break
                file.write(" "*sub+con+"\n")
            except:
                print("[Error]:An unexpected error occured. File will be closed.")
                file.close()
                break
            else:
                pass
        file.close()
            

    if ext=='py':
        filee = open(path+"\\"+bfile,'r')
        datar = filee.read()
        filee.close()
        if comm=='runfile':
            print("[Start]:{}".format(bfile))
            if "#RunFile" in datar:
                os.system(r'{}'.format(path+"\\"+bfile))
            else:
                webbrowser.open(r'{}'.format(path+"\\"+bfile))
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
                if "#RunFile" in datar:
                    os.system(r'{}'.format(path+"\\"+bfile))
                else:
                    webbrowser.open(r'{}'.format(path+"\\"+bfile))
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
            
            
            

    
