testlist1=[1,2,3]
testlist2=[10,20,30]
print(list(zip("abc",testlist1,testlist2)))

browsing_session1=[]
browsing_session1.append(1)
browsing_session1.append(2)
print(browsing_session1)
browsing_session1.pop()
print(browsing_session1)

testnumber1={1,1,2,3,4}
testnumber2={1,5}
print(testnumber1 | testnumber2)#并集
print(testnumber1 & testnumber2)#交集
print(testnumber1 - testnumber2)#差集
print(testnumber1 ^ testnumber2)#不知道什么集合

