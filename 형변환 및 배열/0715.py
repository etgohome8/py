# A= []
# N=int(input("수: "))
# for i in range(1,1000000):
#     if i%N ==0:
#         A.append(i)
#         print(i)

# A = []
# N = int(input("num : "))
# for i in range(1,N+1):
#     if N%i == 0:
#         A.append(i)
#         print(i)
# print(A)

# A=int(input("num : "))
# B=int(input("num: "))
# if A>=B:
#     for i in range(1,A+1):
#         if A%i == 0 and B%i == 0:
#             print(i)
# if B>A :
#     for i in range(1,B+1):
#         if A%i == 0 and B%i == 0:
#             print(i)

# A=[]
# N=int(input("num : "))
# if N>1 :
#     for i in range(1,N+1):
#         if N%i==0:
#             A.append(i)
#     if len(A)== 2:
#         print("소수")
#     else:
#         print("소수가 아님")
# else :
#     print("수를 제대로 입력하세요.")

# A = []
# N = int(input("num : "))
# for i in range(1,N):
#     if N%i == 0:
#         A.append(i)
# if sum(A)== N:
#     print(N,"은 완전수",sep=(" "))
# else :
#     print("완전수 아님.")

# A = []
# N = int(input("num : "))
# for i in range(1,N):
#     if N%i == 0:
#         A.append(i)
# if sum(A)== N:
#     print(N,"은 완전수",sep=(" "))

# # 내가 해본거 ㅋㅋㅋ 이상함
# for i in range(1,10):
#     print(i,"의 배수",sep=(" "))
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j)

# # 이렇게 하니까 된다
# for i in range(2,10):
#     print(i,"의 배수",sep=(" "))
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)

# # N단 입력받고, N단 출력
# N = int(input("num : "))
# for i in range(1,10):
#     print(N,"x",i,"=",N*i)

# N= int(input("num:"))
# A=[]
# for i in range(1,N+1):
#     if i%2==0:
#         A.append(i)
# print(len(A))

# N= int(input("num:"))
# for j in range(1,N+1):
#     A=[]
#     for i in range(1,j+1):
#         if i%2==0:
#             A.append(i)
#     print(i,"이하의 짝수의 개수",len(A))

# N = int(input("num : "))
# A=[]
# for i in range(1,N+1):
#     if N%i==0:
#         A.append(i)
# print(A)

# N = int(input("num : "))
# for j in range(1,N+1):
#     A=[]
#     for i in range(1,j+1):
#         if j%i==0:
#             A.append(i)
#     print(i,"의 약수 : ",A)

# N= int(input("num : "))
# A=[]
# for i in range(1,N):
#     if N%i == 0:
#         A.append(i)
# if sum(A)== N:
#     print(N,"은 완전수")

# N= int(input("num : "))
# for j in range(1,N+1):
#     A=[]
#     for i in range(1,j):
#         if j%i==0:
#             A.append(i)
#     if sum(A)==j:
#         print(j,"는 완전수")

# N= int(input("num : "))
# A=[]
# for i in range(1,N+1):
#     if N%i==0:
#         A.append(i)
# if len(A)==2:
#     print(N,"은 소수")

# N= int(input("num : "))
# for j in range(3,N+1):
#     A=[]
#     for i in range(1,j+1):
#         if j%i == 0:
#             A.append(i)
#     if len(A)== 2:

#         print(j,"는 소수")

# N= int(input("num : "))
# num=1
# for i in range(1,N+1):
#     num *= i
# print(N,"! =",num)

# N= int(input("num : "))
# for j in range(1,N+1):
#     num = 1
#     for i in range(1,j+1):
#         num *= i
#     print(j,"! =",num)







