# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

#                   # 끝에 추가
langs.append("go")
print(langs)

#                # 인덱스 2에 "c#" 추가
langs.insert(2, "c#")
print(langs)


#              # 인덱스 3을 "javascript"로 변경
langs[3] = "javascript"
print(langs)

#                  # "c++" 삭제 (첫번째 데이터만 삭제)
langs.remove("c++")
print(langs)

#                         # 인덱스 1 삭제
langs.pop(1)
print(langs)

#                          # 인덱스 생략 시 마지막 항목 삭제
langs.pop()
print(langs)


print(langs.index("python"))        # "python" 인덱스 찾기

#                      # 리스트 순서를 거꾸로 뒤집기
langs.reverse()
print(langs)

#                         # 오름차순 정렬
langs.sort()
print(langs)

#             # 내림차순 정렬
langs.sort(reverse=True)
print(langs)

#                        # 모든 item 삭제
langs.clear()
print(langs)

# 리스트 복사
ori = [1, 2, 3]

result = ori.copy()
result.append(10)

print(ori, result)


# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]

result2 = ori.copy()    # 원본이 같이 바뀜
result2[0].append(10)

print(ori, result2)


# 깊은 복사를 하려면?
import copy
result3 = copy.deepcopy(ori)
result3[0].append(100)  # 사본만 바뀜


# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
nums = [1, 2, 3, 4]

print(*nums)

a, b, c, d = nums
print(a,b,c,d)

a, *b, c = nums
print(a,b,c)

nums2 = [5, 6]
print(nums + nums2)

print([*nums, *nums2])

# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어", "과학"]
scores = [80, 90, 95]

a, b, c = zip(subjects, scores)
print(a, b, c)

for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}점")

# [x] : x자체를 원소 하나로 해서 넣음
print([zip(subjects, scores)])
# list(x) : x를 풀어서 리스토로
print(list(zip(subjects, scores)))


# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
list1 = []
for i in range(1, 11):
    list1.append(i ** 2)
print(list1)

result =[i ** 2 for i in range(1, 11)]
print(result)   
# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
list2 = []
for i in range(1, 11):
    if i % 2 == 0:
        list2.append(i ** 2)
print(list2)

result = [i ** 2 for i in range(1, 11) if i % 2 == 0]

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기
result = ["짝" if i % 2 == 0 else "홀" for i in range(1, 11)]

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(name) for name in names]

# 길이가 5 이상인 이름만 뽑기
result = [name for name in names if len(name) >= 5]

# 중첩 for문도 가능
# x = 0 1 2
# y = 0 1 2
# x * y로 이루어진 리스트 [0,0,0,1,2,0,2,4]
print([x * y for x in range(3) for y in range((3))])


# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
# scores = [85, 42, 73, 55, 90, 68, 35, 100]

# result = []
# print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
# result = []
# print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
# result = None
# print(result)                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
# words = ["apple", "banana", "kiwi", "mango"]

# result = []  
# print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
# scores = [
#     [90, 80, 70],       # 학생 1
#     [100, 90, 80],      # 학생 2
#     [80, 70, 60],       # 학생 3
# ]

# result = []
# print(result)                       # ✅ [90.0, 80.0, 70.0]