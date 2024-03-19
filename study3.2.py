def testfunction(testnumber):#定义一个会报错的函数
    if testnumber<=0:
        raise ValueError("the number was little to 0")#会反馈一个ValueError报错
    return testnumber


try:
    test=int(input("please input the number"))
    testfunction(test)#调用函数
except ValueError:
    print("the number was little to 0") 
else:
    print(test)
