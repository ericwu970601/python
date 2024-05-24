import random

x1 = 1  # 目標數字範圍的下限
x2 = 100  # 目標數字範圍的上限
n = 10  # 最大猜測次數

target = random.randint(x1, x2)  # 系統隨機生成一個目標數字
attempts = 0  # 猜測次數初始化為 0

print(f"猜數字遊戲開始！目標數字在 {x1} 到 {x2} 之間。你有 {n} 次機會。")

while attempts < n:
    guess = int(input("請輸入你的猜測："))  # 玩家提交猜測數字
    attempts += 1  # 猜測次數增加

    if guess < target:
        print("太低了！")
    elif guess > target:
        print("太高了！")
    else:
        print(f"恭喜你猜對了！目標數字是 {target}。你總共猜了 {attempts} 次。")
        break  # 結束迴圈

    if attempts < n:
        print(f"你還剩下 {n - attempts} 次機會。")
    else:
        print(f"很遺憾，你已經用完了所有 {n} 次機會。目標數字是 {target}。")
