# print(input("입력 : "))

# a = input("입력 : ")
# print(a)

# name = input("이름 : ")
# age = input("나이 : ")
# mail = input("이메일 : ")
# print("이름은 " + name, "나이는 " + age, "이메일은 "+mail, sep=("\n"), end=("\n"))

# a = int(input("숫자 하나 입력하세요 : "))
# b = int(input("다른 숫자를 입력하세요 : "))

# print(a, " 곱하기 " , b , " 는 " , a*b , "입니다.")
# print()
# print(a*b)

# 국어 = int(float(input("국어 점수 : ")))
# 수학 = int(float(input("수학 점수 : ")))
# 과학 = int(float(input("과학 점수 : ")))

# 평균 = (국어+수학+과학)/3
# print("평균은 ", int(평균) , " 입니다")
# print("당신의 평균은 " , 평균 , " 입니다."")

# 사과가격 = 3000
# 배가격 = 2000
# print("="*20)
# print("사과 가격은", 사과가격, "입니다.")
# print("배 가격은", 배가격, "입니다.")
# print("="*20)

# a = int(input("사과의 개수 : "))
# b = int(input("배의 개수 : "))

# print("총 금액은", 사과가격*a+배가격*b, "입니다.")


# h = int(input("시를 입력하세요 : "))
# m = int(input("분 : "))
# s = int(input("초 : "))
# 총 = 3600*h + 60*m + s
# print("총 시간의 초는 ", 총 , "입니다.")


# 세자리수를 입력받고, 수를 뒤집어주세요
# ex) 수입력 : 123asd
#    뒤집힌 수는 321 입니다

# num = int(input("세 자리수를 입력하세요 : "))
# a = num//100
# b = num//10%10
# c = num%10
# print(c,b,a,sep=(""))


# 총 sec를 입력받고, 시간 분 초를 출력해주는 프로그램
sec = int(input("초를 입력하세요 : "))

시간 = sec//3600
분 = sec%3600//60
초 = sec%60
print("입력하신 시간은", 시간,"시간",분,"분",초,"초 입니다.")


# 썹씨를 화씨로 바꾸기
# (2°C × 9/5) + 32 = 35.6°F
# C = float(input("섭씨 온도 : "))
# F = (C*9/5)+32
# print("섭씨온도", C,"는 화씨온도",F,"입니다.")


# 세자리수를 입력받고 각 자리수를 출력하는 프로그램
# a = int(input("세 자리수 입력 : "))
# q = a//100
# w = a%100//10
# e = a%10
# print("백의 자리 ",q)
# print("십의 자리 ",w)
# print("일의 자리 ",e)


#생년월일을 정수로 입력받고, 년 월 일을 나눠서 출력하세요
# a = int(input("생년월일을 6자리로 입력 : "))

# 년 = a//10000
# 월 = a%10000//100
# 일 = a%100

# print("year :", 1900+년)
# print("month :", 월)
# print("day :", 일)



