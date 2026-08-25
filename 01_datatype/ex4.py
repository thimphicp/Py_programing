# 문자열(str)
# "", ''

a = "python"
print(a, type(a))

print("I'll be back")

# 여러줄 문자열
a = """
Life is short
You need python
"""
print(a)

def func():
    """
    func 함수에 대한 설명 작성
    """
    pass
print(func.__doc__)

# 문자열 연결
print("Hello" + " Python")
print("Hello" * 10)
print("-" * 50)

# print("Hello" + 3)
print("Hello" + str(3))

print("10" + "2")
print(int("10" + "2"))

# 문자열 포맷팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15d}")
print(f"{num:<15d}")
print(f"{num:15,d}")
print(f"{num:015d}")
print(f"{num:<015d}")