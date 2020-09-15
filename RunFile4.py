import os
import webbrowser
import subprocess
import sys

origin = os.getcwd()
path = origin
print("RunFile 4.0.2. Enter 'help' for more info.\n")
print("HomePath:{}".format(path))
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
            '_lines_','_lines_reset_','storelines','_fromlines_','RunFile','clearcontent','clr','clear','help',
               'enablebrowser','disablebrowser','enablenhp','disablenhp','quit','history','clearhistory','searchhistory']

arg0 = ['homepath','showpath','delpath','enablenhp','disablenhp','enablebrowser','disablebrowser','quit',
        'clear','clr','help','_file_','_file_reset_','_lines_','_lines_reset_','history','clearhistory']

arg1 = ['newhomepath','delfile','createfile','addcontent','store','runfile','funclist','content',
        'storelines','browse','_lines_','_fromlines_','RunFile','clearcontent','findpath','addpath',
        'searchhistory']

arg2 = ['runfunc','findfunc']
            

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

def command_args(line):
    line_list = line.split(" ")
    list_of_words = list(i for i in line_list if i.strip()!="")
    return list_of_words

while True:
    user = input("rf4>>")
    if user.strip()=="":
        continue

    command = command_args(user)

    if command[0] not in ['history','clearhistory','searchhistory']:
        filee = open(historydir,'a')
        filee.write(user.strip()+'\n')
        filee.close()
    
    if command[0] not in commandlist:
        print("rf4>>Command '{}' doesn't exist. Enter 'help' for more info.".format(command[0]))
        continue

    arglen = len(command)
    
    if arglen>3:
        print(f"rf4>>Max args : 2  Got args : {arglen-1}")
        continue
    else:
        pass


    if arglen==1:

        if command[0] not in arg0:
            if command[0] in arg1:
                print("rf4>>Command '{}' takes 1 argument. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf4>>Command '{}' takes 2 arguments. Enter 'help' for more info.".format(command[0]))
            continue

        if command[0]=="history":
            if os.path.exists(historydir)==False:
                print("rf4>>No history found.")
                continue
            filee = open(historydir,'r')
            histdata = filee.read()
            print("\n"+histdata)
            filee.close()
            continue

        if command[0]=="clearhistory":
            if os.path.exists(historydir)==False:
                print("rf4>>No history found.")
                continue
            filee = open(historydir,'w')
            filee.write("")
            filee.close()
            print("rf4>>History has been cleared.")
            continue
            
        
        if command[0]=="help":
            print()
            print("RunFile v4.0.2")
            print("RunFile is used mainly for file manipulation. It is optimised for python files as RunFile can")
            print("explore deep into your code, access the code's functions and classes, run functions seperately,")
            print("search for desired function or class in the code and run the code itself.")
            print("Commands:\n")
            print("showpath                            : List all the available directories and files in your current path.")
            print("addpath <dir/subdir>                : Add a dir to your original path.")
            print("findpath <dir/subdir>               : Check and display all dirs or files which match.")
            print("delpath                             : Remove last added dir or subdir from path.")
            print("homepath                            : Go back to original path.")
            print("delfile <filename>                  : Delete the specified file.")
            print("createfile <filename>               : Create file of specified name.")
            print("content <filename>                  : Display content of a file.")
            print("clearcontent <filename>             : Clear content of a file.")
            print("store <filename>                    : Store content of a file and extract with key '_file_'.")
            print("storelines <filename>               : Store lines of a file and extract with key '_lines_'.")
            print("_file_                              : Use to get stored file data.")
            print("_lines_                             : Use to get stored file lines.")
            print("_lines_ <linenumber>                : Use to get specified line from _lines_.")
            print("_fromlines_ <linenumber>            : Store a line from _lines_ into _file_.")
            print("_file_reset_                        : Clear data stored in _file_.")
            print("_lines_reset_                       : Clear data stored in _lines_.")
            print("runfile <filename>                  : Run or open specified file. Output of code will be displayed on a different teminal.")
            print("runfunc <filename> <func(<args>)>   : Access and run a function in a '.py' file.")
            print("findfunc <filename> <func(<args>)>  : Find a function or functions in a '.py' file>")
            print("funclist <filename>                 : List all the classes and functions in a '.py' file.")
            print("RunFile <filename>                  : Mark a '.py' file to display output of the code on the runfile terminal.")
            print("clear/clr                           : Clear runfile terminal.")
            print("history                             : Display command history.")
            print("searchhistory                       : Search command history.")
            print("clearhistory                        : Clear command history.")
            print("quit                                : Exit runfile.")
            print()
            continue
        
        if command[0]=="enablebrowser":
            try:
                from googlesearch import *
            except:
                print("rf4>>Installing module google.")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install','google'])
                print()
                from googlesearch import *
            else:
                enableb=1
                print("rf4>>Browser:Enabled")
                print("rf4>>May or may not give desired output. Can be disabled with 'disablebrowser' command.")
            continue

        if command[0]=='disablebrowser':
            enableb=0
            print("rf4>>Browser:Disabled")
            continue

        if command[0]=='enablenhp':
            enable=1
            print("rf4>>NewHomePath:Enabled")
            print("rf4>>May or may not give desired output. Can be disabled with 'disablenhp' command.")
            continue

        if command[0]=='disablenhp':
            enable=0
            func=""
            origin = os.getcwd()
            path=origin
            print("rf4>>NewHomePath:Disabled")
            print("\nHomePath:{}".format(path))
            continue

        if command[0]=='clear' or command[0]=='clr':
            os.system('cls')
            print("RunFile 4.0.2. Enter 'help' for more info.\n")
            print("HomePath:{}".format(path))
            continue

        if command[0]=="quit":
            quit()

        if command[0]=='homepath':
            path=origin
            func=""
            print("\nHomePath:{}".format(path))
            continue

        if command[0]=='_file_':
            print(contentkey.get('_file_'))
            continue

        if command[0]=='_file_reset_':
            contentkey['_file_'] = ''
            print("rf4>>Contents of _file_ has been deleted.")
            continue

        if command[0]=='_lines_':
            print(contentkey.get('_lines_'))
            continue

        if command[0]=='_lines_reset_':
            contentkey['_lines_'] = ''
            print("rf4>>Contents of _file_ has been deleted.")
            continue

        if command[0]=='showpath':
            print()
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    print("File:"+os.path.join(root, name))
                for name in dirs:
                    print("Directory:"+os.path.join(root, name))
            print()
            continue

        if command[0]=='delpath':
            if path==origin:
                print("rf4>>Cannot delete from original path.")
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
            print("\nNewPath:{}".format(path))
            continue

    elif arglen==2:

        if command[0] not in arg1:
            if command[0] in arg0:
                print("rf4>>Command '{}' doesn't take arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf4>>Command '{}' takes 2 arguments. Enter 'help' for more info.".format(command[0]))
            continue

        if command[0]=="searchhistory":
            if os.path.exists(historydir)==False:
                print("rf4>>No history found.")
                continue
            filee = open(historydir,'r')
            histdata = filee.readlines()
            filee.close()
            if histdata==[]:
                print("rf4>>No history found.")
                continue
            print()
            for x in histdata:
                x = x.strip()
                x = x.strip("\n")
                if command[1] in x:
                    print(x)
            print()
            continue

        if command[0]=='_lines_':
            if command[1].isnumeric()==False:
                print("rf4>>Line number required.")
            elif command[1].isnumeric()==True:
                try:
                    command[1] = int(command[1])
                except:
                    print("rf4>>_lines_ accepts numbers only.")
                else:
                    try:
                        print("Line {0}:{1}".format(command[1],contentkey.get('_lines_')[command[1]-1].strip("\n")))
                    except:
                        print("rf4>>Line number out of range.")
                    else:
                        pass
            continue

        if command[0]=='_fromlines_':
            if command[1].isnumeric()==False:
                print("rf4>>Line number required.")
            elif command[1].isnumeric()==True:
                try:
                    command[1] = int(command[1])
                except:
                    print("rf4>>_lines_ accepts numbers only.")
                else:
                    try:
                        contentkey['_file_'] = contentkey.get('_lines_')[command[1]-1].strip("\n")
                        print("rf4>>Specified _lines_ content has been stored in _file_. Use key '_file_' to access the content.")
                    except:
                        print("rf4>>Line number out of range.")
                    else:
                        pass
            continue

        if command[1]=='_file_':
            command[1] = contentkey.get('_file_')

        if command[1]=='_lines_':
            command[1] = contentkey.get('_lines_')

        if command[0]=='browse':
            if enableb==1:
                print("\nSearch:{}\n".format(command[1]))
                browse_path = browserPath
                for url in search(command[1], tld="co.in", num=1, stop = 1, pause = 2):
                    webbrowser.open("https://google.com/search?q=%s" % command[1])
            elif enableb==0:
                print("rf4>>Command '{}' doesn't exist. Enter 'help' for more info.".format(command[0]))
            continue

        try:
            lif = command[1].split('.')
            ext=""
            file = lif[0]
            file = file.strip()
            if len(lif)>=2:
                ext = lif[1]
                ext = ext.strip()
            file = file.replace("/",".")
            file = file.replace("\\",".")
        except:
            print("rf4>>An error occured. Check your input and try again.")
            continue
        else:
            pass
        
        if ext!="py" and command[0]=='funclist':
            print("rf4>>Command '{}' works with '.py' files only.".format(command[0]))
            continue
        else:
            pass

        if command[0]=='addpath':
            if "." in command[1]:
                print("rf4>>Cannot add file to path.")
                continue
            if os.path.exists(pt:=(path+"\\"+command[1]))==False:
                print(f"rf4>>Path '{pt}' doesn't exist.")
                continue
            path = path+"\\"+command[1]
            command[1] = command[1].replace("/",".")
            command[1] = command[1].replace("\\",".")
            if func.strip()=="":
                func=command[1]
            else:
                func = func+"."+command[1]
            func=func.strip()
            if "-" in func:
                print("rf4>>Invalid character '-' found. Files may or may not open and 'runfunc' will not work.")
            print("\nNewPath:{}".format(path))
            if command[1][0]=='.' or command[1][0]=='.':
                print("rf4>>Dir/subdir request beginning with '/' or '\\' may result in wrong path.")
            continue

        if command[0]=='createfile':
            if os.path.exists(path+"\\"+command[1])==True:
                print("rf4>>File '{}' already exists.".format(command[1]))
            else:
                try:
                    filee = open(path+"\\"+command[1],'x')
                    filee.close()
                except:
                    print("rf4>>An error occured. Check your input and try again.")
                else:
                    print("rf4>>File '{}' has been created.".format(command[1]))
            continue

        if command[0]=='delfile':
            try:
                os.remove(path+"\\"+command[1])
            except:
                print("rf4>>File '{}' doesn't exist.".format(command[1]))
            else:
                print("rf4>>File '{}' has been deleted.".format(command[1]))
            continue

        
        if command[0]=='findpath':
            print()
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    if command[1].lower() in name.lower():
                        print(os.path.join(root, name))
                for name in dirs:
                    if command[1].lower() in name.lower():
                        print(os.path.join(root, name))
            print()
            continue

        if command[0]=='newhomepath':
            if enable==1:
                origin=command[1].replace("/","\\")
                if os.path.exists(pt:=origin)==False:
                    print(f"rf4>>Path '{pt}' doesn't exist.")
                    origin = os.getcwd()
                    path=origin
                    func=""
                    print("\nHomePath:{}".format(origin))
                else:
                    path=origin
                    func=""
                    print("\nNewHomePath:{}".format(origin))
            elif enable==0:
                print("rf4>>Command '{}' doesn't exist. Enter 'help' for more info.".format(command[0]))
            continue

        if os.path.exists(path+"\\"+command[1])==False:
            print("rf4>>File '{}' doesn't exist.".format(command[1]))
            continue
        else:
            pass

        if command[0]=='RunFile':
            filee = open(path+"\\"+command[1],'a')
            filee.write("#RunFile\n")
            filee.close()
            if ext=="py":
                print("rf4>>The output of this file will now be displayed on the terminal.")
            continue

        if command[0]=='storelines':
            filee = open(path+"\\"+command[1],'r')
            data = filee.readlines()
            filee.close()
            contentkey["_lines_"] = data
            print("rf4>>File content has been stored. Use key '_lines_' to access the content.")
            continue
        elif command[0]=='content':
            try:
                filee = open(path+"\\"+command[1],'r')
                data = filee.read()
                print("\n{}\n".format(data.strip("\n")))
            except:
                print("rf4>>Couldn't read file.")
            finally:
                filee.close()
            continue
        elif command[0]=='clearcontent':
            filee = open(path+"\\"+command[1],'w')
            filee.write("")
            filee.close()
            print("rf4>>File content has been deleted.")
            continue
        elif command[0]=='store':
            filee = open(path+"\\"+command[1],'r')
            data = filee.read()
            filee.close()
            contentkey["_file_"] = data.strip()
            print("rf4>>File content has been stored. Use key '_file_' to access the content.")
            continue

        if command[0]=='addcontent':
            sub=0
            print("\nFile:{}\n".format(command[1]))
            while True:
                try:
                    file = open(path+"\\"+command[1],'a')
                    con = input(" "*sub+"Line:")
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
                                    print("\nrf4>>Line number out of range.\n")
                                    continue
                                else:
                                    pass
                    if '_lines_' in con:
                        con = con.replace("_lines_",contentkey.get('_lines_'))
                    if con=='[endfile]':
                        file.close()
                        print("\nrf4>>New content has been added.")
                        break
                    file.write(" "*sub+con+"\n")
                except:
                    print("\nrf4>>An unexpected error occured. File will be closed.")
                    file.close()
                    break
                else:
                    pass
            file.close()
            continue

        if ext=='py':
            filee = open(path+"\\"+command[1],'r')
            datar = filee.read()
            filee.close()
            if command[0]=='runfile':
                print("\nStart:{}".format(command[1]))
                if "#RunFile" in datar:
                    os.system(r'{}'.format(path+"\\"+command[1]))
                else:
                    webbrowser.open(r'{}'.format(path+"\\"+command[1]))
                print("Stop:{}\n".format(command[1]))
            elif command[0]=='funclist':
                filee = open(path+"\\"+command[1],'r')
                data = filee.readlines()
                filee.close()
                print()
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
                            print("Function:"+funcname)
                        elif 'class ' in lines:
                            print("Class:"+funcname)
                print()
        else:
            if command[0] == 'runfile':
                print("\nStart:{}".format(command[1]))
                webbrowser.open(r"{}".format(path+"\\"+command[1]))
                print("Stop:{}\n".format(command[1]))
        continue


    elif arglen==3:

        if command[0] not in arg2:
            if command[0] in arg0:
                print("rf4>>Command '{}' doesn't take arguments. Enter 'help' for more info.".format(command[0]))
            elif command[0] in arg2:
                print("rf4>>Command '{}' takes 1 argument. Enter 'help' for more info.".format(command[0]))
            continue

        if command[0] in ['runfunc','findfunc']:
            try:
                lif = command[1].split('.')
                file = lif[0]
                file = file.strip()
                ext = lif[1]
                ext = ext.strip()
                file = file.replace("/",".")
                file = file.replace("\\",".")
            except:
                print("rf4>>An error occured. Check your input and try again.")
                continue
            else:
                pass
            if ext!="py":
                print("rf4>>Command '{}' works with '.py' files only.".format(command[0]))
                continue
            else:
                pass

        if command[0]=='runfunc':
            filee = open(path+"\\"+command[1],'r')
            datar = filee.read()
            filee.close()
            arg = command[2]
            arg = arg.strip()
            if arg=='':
                pass
            elif '(' not in arg or ')' not in arg:
                print("rf4>>Function not completely defined.")
                continue
            else:
                if func.strip()=="":
                    runfunc = file+'.'+arg
                else:
                    runfunc = func+'.'+file+'.'+arg
            print("\nStart:{}".format(command[1]))

            try:
                print("Execute:{}".format(runfunc))
                if func=="":
                    exec("import {}".format(file))
                else:
                    exec("import {}".format(func+'.'+file))
                exec(runfunc)
            except:
                print("rf4>>An error occured. Check your input and try again.")
                continue
            else:
                pass
            print("Stop:{}\n".format(command[1]))
        elif command[0]=='findfunc':
                funct = command[2]
                filee = open(path+"\\"+command[1],'r')
                data = filee.readlines()
                filee.close()
                print()
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
                                print("Function:"+funcname)
                            elif 'class ' in lines:
                                print("Class:"+funcname)
                print()
        continue  

