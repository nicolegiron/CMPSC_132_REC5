# Recitation Activity #5

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

class LinkedList:
    '''
        >>> x=LinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(7)
        >>> x
        Head:Node(7)
        Tail:Node(8.76)
        List:7 -> 8.76
        >>> x.append(5)
        >>> x
        Head:Node(7)
        Tail:Node(5)
        List:7 -> 8.76 -> 5
        >>> x.pop()
        5
        >>> x.pop()
        8.76
        >>> x
        Head:Node(7)
        Tail:Node(7)
        List:7
        >>> x.append(450)
        >>> x
        Head:Node(7)
        Tail:Node(450)
        List:7 -> 450
    '''

    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__

    def isEmpty(self):
        return self.head==None


    def __len__(self):
        current=self.head
        count=0
        while current is not None:
            count += 1
            current = current.next
        return count


    def add(self, value):
        newNode=Node(value)
        if self.isEmpty():
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode


    def __contains__(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return True
            else:
                current=current.next
        return False


    def __delitem__(self,position):
        if self.isEmpty():
            print('List is empty')
            return None
        if len(self)>=position:
            current=self.head
            previous=None
            count=1
            while count<position:
                    previous=current
                    current=current.next
                    count+=1
            if previous is None:
                self.head=current.next
                current.next=None
            elif current.next is None:
                previous.next=None
                self.tail=previous
            else:
                previous.next=current.next
                current.next=None


    def append(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head, self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode



    def pop(self):
        if self.isEmpty():
            return None

        current = self.head
        previous = None
        answer = self.tail.value

        while current.next != None:
            previous = current
            current = current.next
        if previous == None:
            self.head, self.tail = None
        else:
            previous.next = None
            self.tail = previous
        return answer
