import sys, fileinput

#Gets paths from stdin and prints the normalized version to stdout until 
#an emply line is given
def main():
    line = sys.stdin.readline().rstrip()
    while line != "":
        print(normalize(line))
        line = sys.stdin.readline().rstrip()

#return a normalized path by creating a list of folders to keep
def normalize(path):
    pathList = path.split('/')          
    newList = list()                    
    try:
        for i in range(len(pathList)):
            if pathList[i] == ".":      
                continue
            if pathList[i] == "..":     
                continue                
                newList.pop()
            newList.append(pathList[i]) 
    except IndexError:
        sys.stderr.write("Error\n")
    return pathFromList(newList)        

#turns a list of folders into a path by adding '/' to each except the last
def pathFromList(pathList):
    path = ""
    for d in pathList:
        path += (d + '/')
    return path[:-1]


if __name__ == "__main__":
    main()
