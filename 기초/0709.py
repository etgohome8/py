# print(type(True))

# print(bool(0))

# a = 10

# print(a>0)
# print(a<3)
# print(a==1)
# print(a!=2)
# print(a>=4)
# print(a<=5)

# # 둘다 True 일 때만 True
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print()
# print()
# # 하나라도 True 일때 True
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# A = int(input("수를 입력하세요 : "))

# if A < 10:
#     print("한 자리수 입력!")
# if 100 > A >= 10 :
#     print("두 자리수 입력!")
# if 1000 > A >= 100 :
#     print("세 자리 수 입력!")

# # 두 수를 입력받고 둘 중 큰 수를 출력하는 프로그램
# A = float(input("숫자를 하나 입력해라 : "))
# B = float(input("숫자를 하나 더 입력해라 : "))

# if A == B :
#     print("같다")
# if A > B :
#     print(A,"가 더 크다")
# if A < B :
#     print(B,"가 더 크다")

# A = int(input("자연수를 입력하세요 : "))

# if A%2 == 1 :
#     print("홀수입니다.")
# if A%2 == 0 :
#     print("짝수입니다.")

# # 국영수 점수를 입력받고 평균이 80점 이상일 경우 합격, 80 미만의 경우 불합격
# A = float(input("국어 점수를 입력하세요 : "))
# B = float(input("수학 점수를 입력하세요 : "))
# C = float(input("영어 점수를 입력하세요 : "))
# AVG = (A + B + C)/3

# print("당신의 평균은", AVG, "입니다.")

# if AVG >= 80 :
#     print("합격입니다.")
# if AVG < 80 :
#     print("불합격입니다.")

# # 입력한 수가 3의 배수라면 "3의 배수입니다"
# A = int(input("자연수 입력하세요 : "))
# if A%3 == 0 :
#     print("3의 배수입니다.")
# if A%3 > 0 :
#     print("3의 배수가 아닙니다.")

# # 두자리수 수 두 수를 입력받고 더했을 떄, 1의 자리에서 올림이 발생하는지 판별
# A = int(input("두자리 수를 하나 입력하세요 : "))
# B = int(input("두자리 수를 또 입력하세요 : "))
# C = A%10
# D = B%10
# E = C + D
# if E >= 10 :
#     print("올림이 발생했다.")
# if E < 10 :
#     print("올림이 발생하지 않았다.")

# 두 수와 연산자를 입력받고 연산 결과를 출력하는 프로그램
A = int(input("수를 입력하세요 : "))
B = int(input("수를 입력하세요 : "))
C = input("연산을 입력하세요")


