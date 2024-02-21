# 괄호 검사 프로그램
from StackClass import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100) # 공백 상태의 스택 준비
    
    for st in statement:
        if st in ('{', '[', '('):
            stack.push(st)
        
        elif st in ('}', ']', ')'):
            if stack.isEmpty(): # 스택이 공백이면, 비교할 괄호가 없기 때문에 조건 위반
                return False
        
            else:
                left = stack.pop() # 맨 상단 문자를 꺼내서
                # 각기 다른 종류의 괄호 쌍이 서로 같은 유형인지 비교 진행
                if (st == '}' and left != '{') or (st == ']' and left != '[') or (st == ')' and left != '('):
                    return False
                
    return stack.isEmpty() # 남아 있는 요소가 없어야 괄호 검사 성공


str1 = "{ A[(i+1)]=0; }"
str2 = "if ((x<0) && (y<3)"
str3 = "while (n<8)) {n++;}"
str4 = "arr[(i+1])=0;"

print(str1, " ---> ", checkBrackets(str1))
print(str2, " ---> ", checkBrackets(str2))
print(str3, " ---> ", checkBrackets(str3))
print(str4, " ---> ", checkBrackets(str4))