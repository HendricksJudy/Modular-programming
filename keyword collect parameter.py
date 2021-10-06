# 关键字参数收集

def love(a, b, c=3, *args, name, age, **kwargs):  # kw = ket word
    print(a, b, c)
    print(args)  # 普通搜收集参数，会把多余的参数收集为 元组
    print(name, age)
    print(kwargs)  # 关键字参数收集，会把多余的关键字参数收集为 字典

love(a=111, b=222, c=333, name='a', age=20, gender=0)

# love(1, 2, 3, 112, 123, name='aaa', age=222, gender='ccc', aa='aa', bb='bb')
# 注意形参的声明位置
'''
1.普通参数 2. 默认参数 3.收集参数 4.关键字参数  5.关键字收集参数
极少情况下五种形参共同出现
一般是：普通参数， 收集参数，关键字收集参数
'''