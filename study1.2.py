import math
#数学计算

print(math.ceil(2.2))
testcount=math.ceil(55.2)
print(testcount)
#向上取整

testinput=input("please input:")
testNumber=int(testinput)+1
print(testNumber)
#类型转换

testNumber2=1
if testNumber2==1:
  print("number was one")
else:
 print("finish")
#判断
 
testNumber3=input("please  first input:")
testNumber3=int(testNumber3)#注意字符转换
if testNumber3==1:
  print("number was one")
elif testNumber3==2:
   print("number was two")
else:
   print("NO")
#连续判断

testNumber4=input("please second input:")
testNumber4=int(testNumber4)#注意字符转换
if testNumber4==1:
  massage="number was one"
elif testNumber4==2:
   massage="number was two"
else:
   massage="number wasn't one or two"
print(massage)
#统一判断


testNumber2=1
if testNumber2==1:
  print("number was one")
else:
 print("finish")
#等价于
massage=1
massage="number was one"if massage==1 else "finish"
print(massage)


