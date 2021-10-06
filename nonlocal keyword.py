# nonlocal

# 变量和函数都有作用域
# 在内函数中如何使用上一级函数中的局部变量

'''
在内函数中如果想使用外层函数的变量，那么需要使用 nonlocal 关键字引用
'''

def outer():
    '''
    这里是写当前函数文档说明的
    需要说明当前函数的作用
    如果当前函数还有形参，也需要对形参进行逐一说明
    :return:
    '''
    num = 10  # 外函数的局部变量
    def inner():
        nonlocal num  # nonlocal 关键字在局部函数中使用 可以引用上级函数定义的局部变量，但依旧不能提升为全局变量
        num += 1
        print(num)
    inner()


outer()



# 关于函数文档
print(globals())
print(__name__)  # 获取当前脚本的文件名
print(__doc__)  #
print(outer.__doc__)  # 获取当前函数的说明文档
'''
魔术变量：未设置原有的变量 
__name__ ==> 当前脚本如果作为主程序，那么值是_main_ ， 如果是作为模块，在另外一个脚本中引用，那么值就是当前文件的名字
__doc__ ==>  当前脚本的文档说明 在当前脚本中的第一个 三引号文档注释是当前脚本的说明文档

{'__name__': '__main__', 
'__doc__': '\n在内函数中如果想使用外层函数的变量，那么需要使用 nonlocal 关键字引用\n', 
'__package__': None
'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10aa69ca0>, 
'__spec__': None,
'__annotations__': {}, 
'__builtins__': <module 'builtins' (built-in)>, 
'__file__': '/Users/a3910/PycharmProjects/Modular programming/nonlocal keyword.py'
'__cached__': None
'outer': <function outer at 0x10aab4040>}

'''