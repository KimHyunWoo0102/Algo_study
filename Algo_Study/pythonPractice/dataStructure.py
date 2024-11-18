# lambda는 함수를 입력으로 받는 function에서 사용이 매우 유효함
from itertools import *
from collections import Counter

array=[('홍길동',50),('이순신',32),('아무게',75)]

# 다음과 같이 sorted 기능같을때 lambda 사용으로 바로 가능
print(sorted(array, key=lambda x: x[0]))

#map은 리스트 등에 함수를 처리해서 넘김

list1=map(lambda a,b:a+b,(1,2,3,4,5),(5,6,7,8,9))


for item in list1:
    print(item)
#개사기네....

#eval은 사람이 입력한 수식의 답을 줌

#inputData=input("")

#print(eval(inputData))


# sorted 함수에서는 정렬의 기준을 넣어줌
# 사용예시
# sorted(정렬할 객체,방법,reverse=...) 꼴로 사용하며
# 이때 중앙의 방법은 생략이 가능함
array=[('홍길동',50),('이순신',32),('아무게',75)]
sorted(array, key=lambda x: x[0],reverse=True)

# product는 중복순열, combinations_with_replacement 는 중복 조합
# combination은 조합 permutation은 순열

data=['a','b','c','d','e','f']

print(list(combinations(data,3)))
print(list(combinations_with_replacement(data,2)))
print(list(product(data,repeat=2)))
print(list(permutations(data,2)))


# Counter은 각 리스트등의 객체에서 어떤 수가 몇번 나왔는지 빠르게 해결가능함
counter = Counter(['red','blue','red','blue','red','yellow'])

# 이런식으로 사전형으로 바꾸기도 가능함
print(dict(counter))


# math 에서 gcd 제공함 씨발 좆사기다....
# lcm은 a*b//gcd(a,b) 이니 식 외워라

