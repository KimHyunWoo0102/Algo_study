n=int(input())

cnt=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            result=str(i) + str(j) + str(k)

            if '3'in result:
                cnt+=1

print(cnt)