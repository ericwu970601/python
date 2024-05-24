'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
number = int(input(""))  # 從使用者輸入一個整數，並將其轉換為 int 型態，賦值給變數 number
res = 0  # 初始化計數器變數 res，初始值為 0

for i in range(number):  # 開始一個 for 迴圈，迴圈次數為使用者輸入的 number 值
    member = int(input(""))  # 每次迴圈中，從使用者輸入一個整數，並將其轉換為 int 型態，賦值給變數 member
    if member % 3 == 0 and member > 0:  # 判斷 member 是否是正數且能被 3 整除
        res = res + 1  # 如果條件成立，將 res 增加 1

print(res)  # 迴圈結束後，打印變數 res 的值，即符合條件的數字個數
