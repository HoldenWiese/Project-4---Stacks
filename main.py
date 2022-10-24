from stacks import *

def main():
    test1 = Stack(['cow', 'pig', 'llama', 'chicken'])
    print(test1, 'Size: ', test1.size())
    test1.push('cat')
    print(test1, 'Size: ', test1.size())
    test1.pop()
    print(test1, 'Size: ', test1.size())
    test2 = Stack()
    # test2.pop()
    print(test1.top())
    # print(test2.top())
    test1.clear()
    print(test1)
    

if __name__ == "__main__":
    main()