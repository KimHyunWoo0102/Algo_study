n = int(input())  # 모험가 수 입력
arr = list(map(int, input().split()))  # 각 모험가의 공포도 입력

arr.sort()  # 공포도 오름차순 정렬

result = 0  # 그룹의 수
group_count = 0  # 현재 그룹에 포함된 모험가 수

for i in range(n):
    group_count += 1  # 현재 공포도를 가진 사람을 그룹에 포함시킴
    if group_count >= arr[i]:  # 현재 그룹의 인원 수가 공포도 이상이 되면 그룹을 결성
        result += 1  # 그룹 결성
        group_count = 0  # 새로운 그룹을 시작하기 위해 그룹의 수 초기화

print(result)  # 결성된 그룹의 수 출력
