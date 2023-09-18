class Node:
    #생성자 구현(초기화)
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
#리스트 출력
def printList(node: Node) :
    tmp = node

    while(tmp is not None) :
        print(tmp.data)
        tmp = tmp.next

#리스트 찾기
def findList(node: Node, data: int) -> Node :
    result: Node = None
    tmp = node
    
    while(tmp is not None) :
        if tmp.data == data :
            result = tmp
            break
        
        tmp = tmp.next
    
    return result

#리스트 제거
def removeList(node: Node, data) :
    global head
    
    tmp = node
    before = None
    
    while(tmp is not None) :
        if tmp.data == data : 
            #헤드 값이라면
            if head == tmp :
                #헤드 다음이 없다면
                if head.next is None :
                    head = None
                #아니라면
                else :
                    head = head.next
            #다음 값이 없을 때
            elif tmp.next == None :
                before.next = None
            #중간 값일 경우
            else :
                before.next = tmp.next
            break
        
        before = tmp
        tmp = tmp.next

#리스트 삽입
def insertList(data) :
    global head
    tmp = Node(data)
    
    #헤드가 없는 경우
    if head is None :
        head = tmp
    
    else :
        node = head
        before = None
        
        #첫 번째 값만 있는 경우
        if node.next is None :
            if node.data >= data :
                tmp.next = node
                head = tmp
            else :
                node.next = tmp
        else :
            while node.next is not None :
                #데이터 비교
                if before is not None :
                    if (node.data >= data) and (before.data < data) :
                        break
                
                before = node
                node = node.next
            
            #중간에 들어가야 하는 값인지, 제일 큰 값인지 비교
            if node.data >= data :
                before.next = tmp
                tmp.next = node
                node.next = None
            else :
                node.next = tmp
        
    
head : Node = None

insertList(1)
insertList(5)
insertList(3)
insertList(9)
insertList(7)

printList(head)

removeList(head, 7)
printList(head)
