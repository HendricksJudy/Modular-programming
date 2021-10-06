# 递归函数
'''
递归：
    递归函数就是定义了一个函数，然后在函数内，自己调用了自己这个函数
    递归函数内必须要有结束条件，若无条件，无限调用会导致栈溢出

斐波那契数列
实现一个数的阶乘

'''

def digui(num):
    print(num)
    if num > 0:   # 检测当前值是否到了零
         digui(num-1)  # 调用函数本身
    print(num)


digui(3)
'''
在上述函数中当符合if条件时，直接进入下一次上层过程，将下层过程搁置等待，if条件执行结束，再倒序执行下层过程
一层一层进入，一层一层返回


'''
