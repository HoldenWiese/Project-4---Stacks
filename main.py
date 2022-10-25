from stack import *
import re

def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Argument must be of type string")
    
    op_sym = Stack()
    expr = expr.replace(" ", "")
    output = ''

    for char in expr:
        char = str(char)
        if char == '(':
            op_sym.push(char)
        elif char.isnumeric():
            output += char
        elif is_op(char):
            while (
                op_sym.size() != 0 and
                op_sym.top() != '(' and
                precedence(op_sym.top(), char)
            ):
                output += str(op_sym.top())
                op_sym.pop()
            op_sym.push(char)
        else:
            if op_sym.size() != 0:
                output += op_sym.top()
                op_sym.pop()
            if op_sym.size() != 0:
                while(op_sym.top() != '('):
                    if op_sym.size() != 0:
                        output += op_sym.top()
                        op_sym.pop()
                    if op_sym.size() == 0:
                        break
            if op_sym.size() != 0:
                op_sym.pop()
    
    while op_sym.size() != 0:
        output += str(op_sym.top())
        op_sym.pop()
        if op_sym.size() == 0:
            break

    return output


def precedence(top, char):
    if (
        (top == '+' and char == '*') or
        (top == '+' and char == '/') or
        (top == '-' and char == '*') or
        (top == '-' and char == '/')
       ):
           return False
    return True

def is_op(char):
    if (
        (char == '+') or
        (char == '-') or
        (char == '*') or
        (char == '/')
    ):
        return True
    else:
        return False

def eval_postfix(postfix):
    a_stack = Stack()
    
    for char in postfix:
        if char.isnumeric():
            a_stack.push(char)
        else:
            if a_stack.size() != 0:
                temp1 = a_stack.top()
                a_stack.pop()
                if a_stack.size() == 0:
                    return temp1
                temp2 = a_stack.top()
                a_stack.pop()
                if char == '+':
                    result = int(temp1) + int(temp2)
                    a_stack.push(result)
                elif char == '-':
                    result = int(temp2) - int(temp1)
                    a_stack.push(result)
                elif char == '*':
                    result = int(temp1) * int(temp2)
                    a_stack.push(result)
                elif char == '/':
                    result = int(temp1) / int(temp2)
                    a_stack.push(result)

    return str(a_stack.top())

    

def main():
    # test1 = Stack(['cow', 'pig', 'llama', 'chicken'])
    # print(test1, 'Size: ', test1.size())
    # print(test1.below_top())
    # test1.push('cat')
    # print(test1, 'Size: ', test1.size())
    # test1.pop()
    # print(test1, 'Size: ', test1.size())
    # test2 = Stack()
    # # test2.pop()
    # print(test1.top())
    # # print(test2.top())
    # test1.clear()
    # print(test1)

    infix_l = []
    postfix_l = []
    answer_l = []
    
    data = open("data.txt", "r")
    
    for line in data:
        equation = line
        infixed = str(equation.replace("\n", ""))
        
        infix_l.append(infixed)
        postfix_l.append(in2post(infixed))

    for el in range(0, len(infix_l)):
        answer_l.append(eval_postfix(postfix_l[el]))

        print('infix: ', infix_l[el])
        print('postfix: ', postfix_l[el])
        print('answer: ',answer_l[el])
        print()


    

if __name__ == "__main__":
    main()