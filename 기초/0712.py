# A = float(input("수학 : "))
# B = float(input("과학 : "))
# C = float(input("국어 : "))
# X = (A+B+C)/3

# print()
# print("당신의 성적은 ")
# if X>= 90 :
#     print("A")
# elif X >= 80 : 
#     print("B")
# elif X >= 70 :
#     print("C")
# else :
#     print("D")
# print("입니다.")

# A = float(input("숫자 1 : "))
# B = float(input("숫자 2 : "))
# C = input("사칙연산 : ")

# print(A,C,B,"=")
# if C == "+" :
#     print(A+B)
# elif C == "-" :
#     print(A-B)
# elif C == "/" :
#     print(A/B)
# elif C=="x" :
#     print(A*B)
# elif C=="X" :
#     print(A*B)
# elif C=="*" :
#     print(A*B)
# else :
#     print("연산자가 이상합니다.")

# 아이디 = input("아이디 : ")
# 패스워드 = input("패스워드 : ")
# if 아이디 =="admin" :
#     if 패스워드 == "admin" :
#         print("로그인 성공")
#     else :
#         print("패스워드가 틀렸습니다.")
# else:
#     print("계정이 존재하지 않습니다.")

# 아이디 = input("아이디 : ")

# if 아이디 =="admin" :
#     패스워드 = input("패스워드 : ")
#     if 패스워드 == "admin" :
#         print("로그인 성공")
#     else :
#         print("패스워드가 틀렸습니다.")
# else:
#     print("계정이 존재하지 않습니다.")

# A = int(input("월 : "))
# if 3<=A<6 :
#     print(A,"월은 봄입니다.",sep=(""))
# elif 6<=A<9 :
#     print(A,"월은 여름입니다.",sep=(""))
# elif 9<=A<12 :
#     print(A,"월은 가을입니다.",sep=(""))
# elif 1<=A<=12 :
#     print(A,"월은 겨울입니다.",sep=(""))
# else :
#     print("입력이 바르지 않습니다.")

# A = int(input("정수를 압력하세요 : "))

# if 0<A :
#     print("절대값은",A)
# else :
#     print("절대값은",-A)

# print("="*8)
# print("사과는 3000원, 배는 2000원")
# print("="*8)
# A = int(input("소지하고 계신 금액 : "))
# X = int(input("구매하려는 사과 갯수 : "))
# Y = int(input("구매하려는 배 갯수 : "))
# Z = 3000*X + 2000*Y

# if A>=Z :
#     print("잔돈",A-Z,"원")
# else :
#     print("구매불가.")
#     print(Z-A,"원 모자랍니다.",sep=(""))

# A = int(input("자연수 : "))

# if A == 0 :
#     print("0은 자연수가 아냐!")
# elif A%15 == 0 :
#     print("15의 배수")
# elif A%3 == 0 :
#     print("3의 배수")
# elif A%5==0:
#     print("5의 배수")
# else :
#     print("3과 5의 배수가 아님")


# print("="*18)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print("="*18)
# 메뉴 = int(input("메뉴 선택 : "))
# if 1<=메뉴<=2 :
#     print("="*18)
#     print("1. HOT")
#     print("2. ICE")
#     print("="*18)
#     온도 = int(input("온도 선택 : "))
#     if 메뉴 == 1 :
#         if 온도 == 1 :
#             print("아이스 아메리카노 선택")
#         elif 온도 == 2 :
#             print("따뜻한 아메리카노 선택")
#         else :
#             print("온도를 다시 선택하세요.")
#     elif 메뉴 == 2 :
#         if 온도 == 1 :
#             print("아이스 카페라떼 선택")
#         elif 온도 == 2 :
#             print("따뜻한 카페라떼 선택")
#         else :
#             print("온도를 다시 선택하세요.")
# else :
#     print("메뉴를 다시 선택하세요.")



# N = int(input("몇번째 날인가요? "))
# print("당번은 ")
# if N%4==1 :
#     print(" A")
# elif N%4==2 :
#     print(" B")
# elif N%4==3 : 
#     print(" C")
# else :
#     print("D")
# print("입니다.")

# print("오늘은 화요일입니다.")
# A = int(input("며칠 후의 요일이 궁금하니? "))
# if 0<A : 
#     if A%7==0 :
#         print("화요일")
#     elif A%7==1 :
#         print("수요일")
#     elif A%7==2 :
#         print("목요일")
#     elif A%7==3 :
#         print("금요일")
#     elif A%7==4 :
#         print("토요일")
#     elif A%7==5 :
#         print("일요일")
#     else :
#         print("월요일")
# else :
#     print("1 이상의 숫자 입력하세요~")

# A = int(input("년도를 입력하세요: "))

# if A >0 :
#     if A%400 == 0 :
#         print("윤년")
#     elif A%100 == 0 :
#         print("윤년 아님")
#     elif A%4 == 0 : 
#         print("윤년")
#     else :
#         print("윤년 아님")    
# else :
#     print("1 이상의 수 입력")

print("시간은 4자리수로 입력해 주세요.")
print("예) 오전 30시 30분 = 1030, 오후 10시 30분 = 2230")
A = int(input("시간을 입력해주세요: "))

if 0<= A <=2400 :
    if A%100 >=60 :
        print("정확한 시간을 입력해주세요.")
    elif A<30 :
        print("30분 전 :", "23시",A%100+30,"분")
    elif A//100 == 0 and A%100>30 :
        print("30분 전 : 23시", A%100-30,"분")
    elif A%100>30:
        print("30분 전 :", A//100 ,"시", A%100-30,"분")
    elif A%100<=30 :
        print("30분 전 :",A//100-1,"시",A%100+30,"분")
    else :
        print("시간을 제대로 입력해주세요")
else :
    print("24시간 이내의 수를 입력해주세요.")








