class LinkList():

    def __init__(self):
        self.head = None
        self.size=0
        # if x!=None and next!=None:
        #     self.val=x,self.next=next
        # elif x!=None and next==None:
        #     self.val=x


        # self.val = x
        # self.next = None



    def addLink(self,index,val):
        if index==0:
            note=Note(val)
            note.setNext(self.head)
            self.head=note
            self.size+=1
        else:

        # self.head=Note(val).setNext(self.head) 这个不成功不知道为啥不能这么写
            if index>=self.size+1:
                cur=self.head
                for i in range(0,self.size-2):
                 # 这里为什么-2呢，
                 # 首先循环第一遍 到了第二个元素，
                 # 然后到第三个元素，
                 # 用户输入的值则是从第二个元素开始所以这里减去2
                    cur=cur.next
                note = Note(val)
                note.setNext(self.head)
                self.head = note
                self.size += 1
            else:
                cur=self.head
                for i in range(0,index-2):
                    cur=cur.next
            # 先存下一个节点
                nextNote=cur.next
#            创建一个新的节点
                note = Note(val)
                note.setNext(nextNote)
#           把当前节点的next指向新创建的节点
                cur.next=note
                self.size+=1


class Note():
    def __init__(self,x):
        self.val=x
        self.next=None
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next

class PrintLinkList():
    def __init__(self,linkArr):
        self.arr=linkArr
    def toString(self):
        while self.arr!=None:
            print(self.arr.val)
            # print(self.arr.next)
            self.arr=self.arr.next
    
class TurnLink():
    def __init__(self,head):
        self.head=head

    def turnLink(self):
        pre=None;cur=self.head
        next=cur.next
        while cur!=None:
            cur.next=pre
            pre=cur
            cur=next
            if cur==None:
                break
            next=cur.next
        self.head=pre
        return self.head

    def reverseList(self, head):
        pre, cur = None, head
        #这里他把next放在里面第一个位置先负值，就会避免我上面出现的情况多做了一步判断
        #写的好呀！
        #没有多余的操作
        #还有进入while时，直接可以用cur是否为None判断，不用自己写 cur!=Noneyyao
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

if __name__ == '__main__':
   ln=LinkList()
   ln.addLink(0,2)
   ln.addLink(0,1)
   ln.addLink(0,3)
   # ln.addLink(0,"x")
   # ln.addLink(1,3)
   # ln.addLink(2,3)
   # ln.addLink(3,4)

   printArr=PrintLinkList(ln.head)
   printArr.toString()
   print('----------------------')
   turnLink=TurnLink(ln.head)
   printArr2=PrintLinkList(turnLink.turnLink())
   printArr2.toString();
