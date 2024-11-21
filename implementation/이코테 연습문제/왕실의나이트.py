# 1. 8*8이 있음
# 2. 나이트는 두칸 + 오른쪽 두칸 + 왼쪽만 가능함
# 3. 이걸로 비교하면됌

turn=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
arr=[[0 for _ in range(8)]for _ in range(8)]
nights=input("")

x=ord(nights[0])-ord('a')
y=int(nights[1])


cnt=0

for dy,dx in turn:
    ny=y+dy
    nx=x+dx

    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    else:
        cnt+=1

print(cnt)