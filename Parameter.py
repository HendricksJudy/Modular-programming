# 普通参数 默认参数，收集参数 *args

# 命名关键字参数
'''
1. 关键字参数定义在 收集参数 后面
2. 关键字参数必须通过形参的名字进行传递

'''
# c = 3
# def love(a, b, c, *args, name):
#     print(a, b, c, *args)
#     print(name)
# love(1, 2, 3, 4, 5, 6, 7, 8, 9, name='admin')  # 调用时，实参必须用形参名字传递


# def love(age, name):
#     print(name)
#     print(age)
#
# love('abc')
# love(name="aabbcc", age=123)  # 在调用普通函数时，需要按照顺序进行参数的传输
# 也可以把普通函数的普通参数按照关键字参数进行传递
