# 函数的返回值

'''
函数可以分为两类
    1。 执行过程函数： 函数体内完成一定功能即可，没有返回值
    2。 具有返回值的函数： 函数体内完成一定功能，并且返回一个结果到函数调用处
'''
'''
函数中可以使用return 进行数据返回
可以使用return 返回任意内容和数据
return 会把返回值，返回到函数调用闯江湖
return 意味着函数的结束，return之后的代码不再执行
如果在函数中没有使用return 或者 return后面没有任何内容，那么默认返回None
'''

# 在一个函数中，可以返回一些内容，也可以不返回

# 没有返回值的函数，或者理解为，没有指定返回内容，默认会返回None
def love(a, b):
  print(f'{a} i love you {b}')
r = love('我', '你')
print(r)  # 因为没有返回值所以输出 none

# None 是一个特殊数据表示什么都没有 <class 'NoneType'>

# 如果需要在函数中指定返回内容，可以使用 return 关键字
def love(a, b):
   res = f'{a} i love you {b}'
   print(1)
   return res # 可以在函数体内，使用return 返回任意内容
   print(2)  # 在return之后的内容不会执行了

love('我', '你')


# print(love('老鼠', '猫咪'))
# r = love('狼', '羊')  # 调用带有返回值的函数时，函数中的返回值，会返回到函数调用处
# print(r)