testperson="student"
testpersonage=19
testpersonadress=True
if testpersonadress and testpersonage>=18 and not testperson=="student":
    print("yes you could do visa card ")
else:
    print("you couldn't do visa card ")
#and or not用法跟其他语法一样
    
for number in range(3):
    print("type one word")
    print(number)
#循环
  

for number in range(1,10):
    print("number was try")
    if number==7:
        print("number was seven")
        break
#break跳出循环
    
for x in range(3):
   for y in range(3):
       print(f"({x},{y})")#不加f会导致都是x,y

testNumber5=1
while testNumber5<100:
    testNumber5=testNumber5+1
    print(testNumber5)
#while循环