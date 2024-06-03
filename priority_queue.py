class Node:
    def __init__(self, url, priority):
        self.url = url
        self.priority = priority
        self.next = None

    def __init(self, url):
        self.url = url
        self.priority = 0
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.end = None

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def push(self, url, priority):
        if self.isEmpty() == True:
            self.front = Node(url, priority)
        else:
            if self.front.priority < priority:
                moveNode = Node(url, priority)
                moveNode.next = self.front
                self.front = moveNode
            else:
                temp = self.front
                while temp.next:
                    if priority >= temp.next.priority:
                        break

                    temp = temp.next
                moveNode = Node(url, priority)
                moveNode.next = temp.next
                temp.next = moveNode

    #def pop(self):


