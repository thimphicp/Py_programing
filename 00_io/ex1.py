# 입출력

a = input()
print(a, end="")
print(type(a))
print(a, type(a), sep=",")

a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

b = float(input())
print(b, type(b))

# 정수 2개 입력
# 100
# 200
a = int(input())
b = int(input())
print(a, b, sep=",")

# 100 200
a, b = input().split()
print(a, type(a))
print(b, type(b))

# map
# map(함수, list 객체)
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트 변환
a = list(map(int, input().split()))
print(a, type(a))