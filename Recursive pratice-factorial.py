# 实现阶乘


# def jiecheng(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
#
# res = jiecheng(7)
# print(res)

'''
递归函数的效率并不高，能不用尽量不用
一个函数如果调用后，没有结束，那么在栈空间就一直存在，直到这个函数运算结束后才销毁

'''

# 斐波那契数列
# 求第n位上的数是多少
num = 0
def feibona(n):
    global num
    num += 1
    if n == 1 or n==2:
        return 1
    elif n <= 0:
        print('请输入一个正整数')
    else:
        return feibona(n-1) + feibona(n-2)

rs = feibona(6)
print(rs)
print(num)