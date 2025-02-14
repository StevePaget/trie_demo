f = open("sherlock.txt","r")

class Node():
    def __init__(self, contents):
        self.contents = contents
        self.leftPointer = None
        self.rightPointer = None

class Tree():
    def __init__(self, firstNode):
        self.root = firstNode

    def addItem(self,item):
        current = self.root
        while True:
            if item < current.contents:
                if current.leftPointer is None:
                    current.leftPointer = Node(item)
                    #print(f"adding {item} to left of {current.contents}")
                    return 1
                else:
                    current = current.leftPointer
            elif item > current.contents:
                if current.rightPointer is None:
                    current.rightPointer = Node(item)
                    #print(f"adding {item} to right of {current.contents}")
                    return 1
                else:
                    current = current.rightPointer
            else:
                return 0

    def findItem(self, item):
        current = self.root
        checkCount = 0
        while current.contents != item:
            checkCount +=1
            if item < current.contents:
                if current.leftPointer is None:
                    return False
                else:
                    current = current.leftPointer
            if item > current.contents:
                if current.rightPointer is None:
                    return False
                else:
                    current = current.rightPointer
        return True, checkCount

words = []
alltext = f.readlines()
for line in alltext:
    line = line.strip().split()
    for word in line:
        words.append(word.lower())

wordcount = 0
sherlockTree = Tree( Node(words[0]))
for word in words:
    wordcount += sherlockTree.addItem(word)
print(f"{wordcount} unique words found")

wordtoFind = ""
while wordtoFind != "quit":
    target = input("Enter a word to find (enter quit to exit)")
    print( sherlockTree.findItem(target.lower()))
