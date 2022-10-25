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
                output += op_sym.top()
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
        output += op_sym.top()
        op_sym.pop()
        if op_sym.size() == 0:
            break

    return output

def eval_postfix():
    return ''

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

    
    data = open("data.txt", "r")
    
    for line in data:
        equation = line
        equation = equation.replace("\n", "")
        print('infix: ', equation)
        print('postfix: ', in2post(equation))
        print('answer: ')
        print()
    

    

if __name__ == "__main__":
    main()