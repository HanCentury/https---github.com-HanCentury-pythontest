try:  #可能发生的异常
    test1=int(input("please input number"))
    print(test1)
except ValueError: #抛出异常
    print("you didn't input this")


try:  #可能发生的异常
    test2=int(input("please input number"))
    print(test2)
except ValueError: #抛出异常,这是输入类型错误
    print("you didn't input this")  
except ZeroDivisionError:#还包括很多种异常，不能为0:ZeroDivisionError
    print("warning ,the number was 0!")
else:
    print("no bug")#如果没有异常，抛出else里的内容

try:
    file=open("D://context.txt")
except ValueError:
    print("error")#如果该目录下没有该文件会报错
finally:
    file.close()
    print("finish")