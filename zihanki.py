n = int(input("コインを入れてください: "))
j = 100
turi = n - j

x = turi // 500  # 500円硬貨の枚数
turi %= 500

y = turi // 100  # 100円硬貨の枚数
turi %= 100

z = turi // 10   # 10円硬貨の枚数
turi %= 10

w = turi         # 1円硬貨の枚数

print(f"500円玉: {x}枚, 100円玉: {y}枚, 10円玉: {z}枚, 1円玉: {w}枚")