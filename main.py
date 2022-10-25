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
    stack = Stack()
    result = 0
    
    for char in postfix:
        if char.isnumeric():
            stack.push(char)
        else:
            if stack.size() != 0:
                temp1 = stack.top()
                stack.pop()
                # if stack.size() != 0:
                temp2 = stack.top()
                stack.pop()
                def switch(char):
                    if char == '+':
                        result = temp1 + temp2
                        stack.push(result)
                    elif char == '-':
                        result = temp1 - temp2
                        stack.push(result)
                    elif char == '*':
                        result = temp1 * temp2
                        stack.push(result)
                    elif char == '/':
                        result = temp1 / temp2
                        stack.push(result)

    
    return stack.top()
    

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
        in2post_result = in2post(equation)
        
        print('infix: ', equation)
        print('postfix: ', in2post_result)
        # print(eval_postfix(in2post_result))
        print()
    

    

if __name__ == "__main__":
    main()