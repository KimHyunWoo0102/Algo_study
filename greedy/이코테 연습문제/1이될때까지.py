n,k=map(int,input().split())
cnt=0

tmp=n//k*k
print(tmp)
cnt+=n-tmp

while tmp!=1:
    tmp=tmp//k
    cnt+=1

print(cnt)

'''
cnt=0

while n!=1:
    if n%k==0:
        n=n//k
    else :
        n-=1

    cnt += 1
'''

