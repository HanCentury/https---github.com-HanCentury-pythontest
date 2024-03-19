from functools import total_ordering


def testfunction():
    print("this  was a  test function")
#定义一个函数

testfunction()
#调用函数

def testfunction2(first_name,last_name):
    print(f"myname was {first_name}{last_name}")
#定义一个有两个形参的函数
    
testfunction2("han","shiji")
#调用参数

def testfunction3(name):
        return "yes"
    
testprint=testfunction3("hanshiji")
print(testprint)#return不会打印出来，注意！

def greet_person(name):
        return f"Hello, {name}! You are awesome!"

# 示例调用
result = greet_person("hanshiji")
print(result)#return不会打印出来，注意！
file=open("context.txt","w")#file=open("context.txt","w")就是写入到py文件所在的目录。file=open("D://context.txt","w")是写在固定目录
file.write(result)

def testadd(number1,number2=2): #默认为2
    return number1+number2

print(testadd(1))
print(testadd(1,3))

def multiply(*numbers):#可变个数的形参
      total=1
      for number in numbers:
           total=total*number
      return total
      
print(multiply(1,2,3,4,5))