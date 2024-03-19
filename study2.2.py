def save_user(**user):#输入什么保存什么
    print(user)

save_user(id=1,name="hanshiji",age=23)
save_user(id=2,name="century")

global testmessage#全局变量
testmessage=1

print(testmessage)

testString1=["a","b","c"]
testString2=[[0,1],[1.2]]
testString3=[0]*5
testString4=list(range(20))
testString5=list("hello world")
print(testString1)
print(testString2)
print(testString3)
print(testString4)
print(testString5)
print(len(testString1))
print(len(testString2))
print(len(testString3))
print(len(testString4))
print(len(testString5))
#数组，输出和输出大小

testnumber=[1,2,3,4,5]
first,second,*other=testnumber
print(first)
print(second)
print(other)
#数组解压

testnumber2=[1,2,3,4,5]
print(testnumber2)
testnumber2.pop(0)  #泵出第1个字符
print(testnumber2)
del testnumber2[1] #删除第2个字符
print(testnumber2)
testnumber2.pop(2)  #泵出默认第3个字符
print(testnumber2)
print(testnumber2.index(4))#寻找字符位置，字符要加"，数字不加
testnumber2.pop()  #泵出最后一个字符
print(testnumber2)