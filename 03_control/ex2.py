# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
while i < len(nums):
    if nums[i] == target:
        print("found")
    i += 1
else:
    print("target not found")

# if nout found:
    # print(f"{target} not found")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0
while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(tot)

print(f"sum = {tot}")
