import re, sys

#Gets paths from stdin and prints the normalized version to stdout until 
#an emply line is given
def main():
    line = sys.stdin.readline().rstrip()
    while line != "":
        print(normalize(line))
        line = sys.stdin.readline().rstrip()

#return a normalized path by removing parts of the path with regex
def normalize(path):
    return re.sub('(/|^)[^/]*/\.\.(/|$)', '/', re.sub('(/|^)\.(/|$)', '/', path))

if __name__ == '__main__':
    main()