a_list=[7,12,88,43,9,0]


def solution(list):
    stack=[]
    counter=0
    for x in list:
        stack.append(x)
        if counter==1:
            stack.pop()
            counter=0
        else:
            counter=1
        print(stack)

print(solution(a_list))