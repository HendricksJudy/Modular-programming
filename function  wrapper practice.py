# 函数封装的练习题

# 定义函数 打印99乘法表
# def jiujiu(n=0):
#     '''
#         当前函数的功能是顺序打印99乘法表
#         n=0 用于控制 正向输出和反向输出 99乘法表， 0为正向 默认， 1为反向
#     :return:
#     '''
#     if n == 0 :
#         rs = range(1, 10)
#     elif n ==1:
#         rs = range(9, 0, -1)
#     else:
#         print('请输入0或1！')
#     for x in rs:
#         for y in range(1,x+1):
#              print(f'{x}x{y}={x*y}', end=' ')
#         print()
#
#
# jiujiu()

# 封装打印矩形的函数
# def juxing():
#     for x in range(1, 101):
#         print('#', end=" ")
#         if x % 10 == 0:
#             print()
#
# juxing()

# 打印一个空心矩形
'''
# # # # # # # # # # 
#                 # 
#                 # 
#                 #  
#                 # 
#                 #  
#                 # 
#                 # 
#                 # 
# # # # # # # # # #

#            #
# # # # # # # # # #



'''
# def kongxing():
#     for n in range(1, 11):
#         if n == 1:
#             print('# # # # # # # # # # ')
#         elif n == 10:
#             print('# # # # # # # # # # ')
#         else:
#             print('#                 # ')
#
#
# kongxing()
print('输入0输出空心矩形，输入1输出实心矩形')
def juxing(x, t, n=1):
    print('# '*x)
    for x in range(1, x+1):
        if n == 1:
            print('# '*x)
        elif n == 0:
            nbsp = ' '*(2*t-3)
            print(f'#{nbsp}#')
    print('# '*x)

juxing(n=0, x=14, t=14)