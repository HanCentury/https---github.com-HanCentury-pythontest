class Test:#首字母必须大写
    def __init__(self, x, y):#构造函数
        self.testattribute1 = x
        self.testattribute2 = y

    def test(self):#自定义函数
        print("this was a test")

    @classmethod    #类自定义函数，这样不仅仅实例可以调用，类也可以直接调用
    def class_method(cls, parameter):
        print(f"Class method called with parameter: {parameter}")

test=Test(1,2)#生成实例
test.test()       
print(test.testattribute1)   
print(test.testattribute2)
test.testattribute3=10  #不需要提前定义也可以直接生成
print(test.testattribute3)
Test.class_method(2)
test.class_method(425)





