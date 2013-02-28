import sys, fileinput

def main():
    line = sys.stdin.readline().rstrip()
    while line != "":
        print(normalize(line))
        line = sys.stdin.readline().rstrip()

def normalize(path):
    pathList = path.split('/')
    newList = list()
    try:
        for i in range(len(pathList)):
            if pathList[i] == ".":
                continue
            if pathList[i] == "..":
                newList.pop()
                continue
            newList.append(pathList[i])
    except IndexError:
        sys.stderr.write("Error\n")
    return pathFromList(newList)

def pathFromList(pathList):
    path = ""
    for d in pathList:
        path += (d + '/')
    return path[:-1]


if __name__ == "__main__":
    main()