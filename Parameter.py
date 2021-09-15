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
# love(1, 2, 3, 4, 5, 6, 7, 8, 9, name='admin')


def love(age, name):
    print(name)
    print(age)

# love('abc')
love(name="aabbcc", age=123)
