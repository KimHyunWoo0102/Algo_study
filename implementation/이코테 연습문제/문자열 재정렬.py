data=input()

nums=['1','2','3','4','5','6','7','8','9','0']

result=sorted(data)
print(result)

sum=0

#isalpha는 알파벳인지 아닌지 확인

for item in result:
    if item.isalpha():
        print(item,end='')
    else:
        sum+=int(item)

print(sum)