# # 수를 입력받고, 수를 이어적었을 때 길이를 출력하세요!!! 참고로 문자열의 길이는 len(문자열) 입니다!!

# N = int(input("수 입력 : "))
# st = ''

# for i in range(1,N+1):
#     st += str(i)
# print("이어적은 결과 :", st)
# print("길이 : ", len(st))

# N = int(input("수 : "))
# if N%2 == 0 :
#     print("짝수")
# else :
#     print("홀수")

# 수를 입력받고 1 ~ N 까지짝수, 홀수를 판별하는 프로그램 

# 방법1
# N = int(input("수 : "))
# for i in range(1,N+1) :
#     if i % 2 == 0 :
#         print(i,"짝수")
#     else :
#         print(i, "홀수")

# #방법2
# N = int(input("수 : "))
# # if N%2 == 0 :
# #     print(N,"짝수")
# # else :
# #     print(N,"홀수")
# for k in range(1,N+1):
#     if k%2 == 1:
#         print(k,"홀수")
#     else :
#         print(k,"짝수")

# 수를 입력받고 1 ~ N 까지 짝수의 합, 홀수의 합을 구해라
# N = int(input("수 : "))
# 짝 = 0
# 홀 = 0
# for i in range(1,N+1):
#     if i%2 == 0:
#         짝 += i
#     else :
#         홀 += i
# print ("짝수의 합", 짝)
# print ("홀수의 합", 홀)

# 내가 한거 틀림 ㅋㅋ
# N = int(input("수 : "))
# 홀 = 0
# 짝 = 0
# for j in range(1,N+1):
#     if j%2 == 1 :
#         홀 += j
#         print("홀", 홀)
#     else :
#         짝 += j
#         print("짝", 짝)

# 수를 입력받고 (N) 리스트에 추가하는 프로그램

# N=[]
# n = int(input("수 :"))
# N.append(n)
# print(N)

# M = []
# m = int(input("수 : "))
# 합 = 0
# for i in range(1,m+1):
#     합 += i
#     M.append(i)
# print(M)

# H = []
# h = int(input("수 : "))
# 홀 = 0
# for j in range(1,h+1):
#     if j%2 == 1:
#         홀 += j
#         H.append(j)
# print(H)

# A = []
# a = int(input("수 : "))
# 홀합 = 0
# for k in range(1,a+1):
#     if k%2 == 1 :
#         홀합 += k
#         A.append(k)
# print(A, " 합은:",sum(A))

# N = int(input("수 : "))
# for k in range(1,N+1):
#     if k%3 ==0:
#         print(k,end=" ")
# print()

# A=[]
# N = int(input("수 : "))
# for i in range(1,N+1):
#     if i%3 == 0:
#         A.append(i)
# print(A)

# A = []
# B = 0
# N = int(input("수 : "))
# for i in range(1,N+1):
#     if i%3 == 0 :
#         B += i
#         A.append(i)

# print(N,"까지 3의 배수들의 합은",B,"입니다.")
# print(sum(A))

# N = int(input("수: "))
# if N>0 :
#     if N%4 ==1 :
#         print ("A")
#     elif N%4 == 2 :
#         print("B")
#     elif N%4 == 3 :
#         print("C")
#     else :
#         print("D")    
# else :
#     print("1 이상의 수를 입력")

# N = int(input("수: "))
# for i in range(1,N+1):
#     if i%4 == 1:
#         print (i,"A")
#     elif i%4 == 2 :
#         print(i,"B")
#     elif i%4 == 3 :
#         print(i,"C")
#     else:
#         print(i,"D") 

# N = int(input("년 : "))
# if N% 400 == 0 :
#     print(N, "윤년")
# elif N%100 == 0 :
#     print(N, "윤년 아님")
# elif N%4 == 0 :
#     print(N, "윤년")sss
# else :
#     print(N, "윤년 아님")
# for i in range(2000,N+1):
#     if i% 400 == 0 :
#         print(i, "윤년")
#     elif i%100 == 0 :
#         print(i, "")
#     elif i%4 == 0 :
#         print(i, "윤년")
#     else :
#         print(i, "")

# N = int(input("수: "))
# j = 1
# for i in range(1,N+1):
#     j *= i
# print(j)

# for k in range(5,21) :
#     su = 1
#     for i in range(1,k+1):
#         su *= i
#     print (k, su)

# M = int(input("num : "))
# if M%2 == 0 :
#     print(M,"은 짝수")
# else :
#     print(M,"은 홀수")
# O = int(input("num : "))
# if O%2 == 0 :
#     print(O,"은 짝수")
# else :
#     print(O,"은 홀수")
# P = int(input("num : "))
# if P%2 == 0 :
#     print(P,"은 짝수")
# else :
#     print(P,"은 홀수")

# for i in range(4) :
#     N = int(input("num : "))
#     if N%2 == 0:
#         print(N,"은 짝수")
#     else :
#         print(N,"은 홀수")


# A = []
# for i in range(1,10):
#     N = int(input(str(i)+". num: "))
#     A.append(N)

# for i in A:
#     if i%2 == 0:
#         print(i,"짝수")
#     else :
#         print(i,"홀수")

# for i in range(5):
#     A= int(input("num: "))
#     B= int(input("num: "))
#     if (A%10 + B%10) <10 :
#         print("받아올림 발생하지 않음")
#     else :
#         print("받아올림 발생")

A= []
for i in range(5):
    N = int(input("점수:"))
    A.append(N)
print("5 과목의 평균은", sum(A)/len(A))
for i in A:
    if i < sum(A)/len(A):
        print(i,"는 평균 이하입니다.")
