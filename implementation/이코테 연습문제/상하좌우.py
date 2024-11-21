n=int(input())

route=list(input().split())

arr=[[0 for _ in range(n)] for _ in range(n)]
x,y=0,0

arr[y][x]=1
for cmd in route:
    dx,dy=0,0
    if cmd == 'R':
        dx,dy=1,0
    elif cmd == 'L':
        dx,dy,=-1,0
    elif cmd=='U':
        dx,dy=0,-1
    else:
        dx,dy=0,1

    if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0:
        continue

    y+=dy
    x+=dx

    arr[y][x]=1


print(y+1,x+1)


