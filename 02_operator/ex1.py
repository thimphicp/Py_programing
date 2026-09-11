# 연산자

# 산술 연산자
a = 10
b = 3

print(a * b)
print(a + b)
print(a - b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

# 정수 / 정수 = 정수
print(10 / 5)
print(10 // 5)

# 복합 대입 연산자
a += 4
print(a)

a -= 2
print(a)


# 증감 연산자
# b = a++
a += 1

# 비교 연산자  
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble")
print(1 < 2 < 3)    # 1 < 2 and 2 < 3
print(1 < 3 < 2)    # 1 < 2 and 2 < 3

# 논리 연산자 (and, or, not)
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Short-circuit 테스트
a = 10
b = 0

# print(a / b)
if a > 0 or a / b:
    print("yes")
else:
    print("no")