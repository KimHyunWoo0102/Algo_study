# 문자열 S가 주어졌을때 왼쪽부터 곱하기를 넣을지 더하기를 넣을지
# 가장 큰 숫자가 나오도록함
# 모든 문자열은 +인가? 음수는 없는가?


# 0이상의 정수라고 우선 가정

# 0 or 1 일때만 더하는게 유리하고 나머지는 곱하는게 무조건 좋음
data=input()

result=int(data[0])

for i in range(1,len(data)):
    if int(data[i])<=1 or result<=1:
        result+=int(data[i])
    else:
        result=result*int(data[i])

print(result)


