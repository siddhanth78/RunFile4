def command(line,sep=" "):
    line_list = line.split(sep)
    list_of_words = list(i for i in line_list if i.strip()!="")
    return list_of_words

def command_args(line,sep=" "):
    arg=[]
    line_list = line.split(sep)
    command = line_list[0].split(" ")
    list_of_words = list(i for i in command if i.strip()!="")
    for i in range(1,len(line_list)):
        arg.append(line_list[i])
    return list_of_words,arg
