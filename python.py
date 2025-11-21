# ##1-masala
# for i in range(1 ,11):
#     print(i)
##2-masala
# ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
# print("Do'stlarim:")
# for ism in ismlar:
#     print(f"Salom,{ism}!")
##3-masala
# for son in range(2,101,2):
#     print("son")
##4-masala
# son = 0
# for son1 in range(1,11):
#     son = son + son1
#     print(son)
##5-masala
# matn=input("Matn kiriting; ")
# uzunlik = 0
# for belgi in matn:
#     uzunlik = (uzunlik + 1)
#     print("matn uzunligi:",uzunlik, "belgi")
##7-masala
# matn input("\nMatn kiriting: ")
# unlilar = "aueeiooo"
# sanoq = 0
# for belgi in matn.lower():
#     if belgi in unlilar:
#         sanoq  = sanoq +1
#         print("Jami unli harflar:",sanoq,"ta")
##8-masala
# sanoq = 0
# for son in range(1,51):
#     if son % 3 ==0:
#         print(son)
#         sanoq += 1
#         print("Jami:" ,sanoq, "ta son")
##9-masalalar
# son = input("Son kiriting: ")
# son = son.lstrip('-')
# yigindi = 0
# for raqam in son:
#     yigindi += int(raqam)
# print(f"Raqamlar yig'indisi: {yigindi}")
##10-masala
# son = int(input("Son kiritng (faktorial): "))
# if son < 0:
#     print("Manfiy sonni faktoriali aniqlandi")
# else:
#     fakt = 1
#     for i in range(1, son + 1):
#         fakt = fakt * i
#     print(son, "ning faktorili =", fakt)
##11-masala
# def print_multiplication_table(rows=10, cols=10):
#     title = "MULTIPLIKATSIYA JADVALI"
#     row_label_width = 3
#     cell_width = 5
#     print(title)
#     total_width = row_label_width + 3 + cols * cell_width
#     print("=" * total_width)
#     print(" " * row_label_width + " |", end="")
#     for j in range(1, cols + 1):
#         print(f"{j:>{cell_width}}", end="")
#     print()
#     print("-" * total_width)
#     for i in range(1, rows + 1):
#         print(f"{i:>{row_label_width}} |", end="")
#         for j in range(1, cols + 1):
#             product = i * j
#             print(f"{product:>{cell_width}}", end="")
#         print()  # yangi satr
# if __name__ == "__main__":
#     print_multiplication_table(10, 10)
##12-masala
# balandlik = int(input("Piramida balandligini kiriting: "))
# print("\n YULDUZLI PIRAMIDA\n")
# for qator in range(1, balandlik + 1):
#     # Bo'sh joylar
#     for _ in range(balandlik - qator):
#         print(" ", end="")
#     # Yulduzchalar
#     for _ in range(2 * qator - 1):
#         print("*", end="")
#     print()
##13-masala
# a = 0
# b = 1
# print("Fibonachchining birinchi 10 ta soni:")
# for _ in range(10):
#     print(a, end=" ")
#     a, b = b, a + b
##14-masala
# print("1 dan 100 gacha tub sonlar:")
# tub_sonlar = []
# for son in range(2, 101):
#     tub = True
#     for boluvchi in range(2, son):
#         if son % boluvchi == 0:
#             tub = False
#             break
#     if tub:
#         tub_sonlar.append(son)
# for s in tub_sonlar:
#     print(s, end=" ")
# print("\nJami:", len(tub_sonlar), "ta tub son")
##15-masala
# print("Raqamli soat simuliyatori")
# print("========================================")
# sanash = 0
# for soat in range(24):
#     for minut in range(60):
#         for sekund in range(60):
#             print(f"{soat:02d}:{minut:02d}:{sekund:02d}")
#             sanash += 1
# print("\nJami:", sanash, "ta vaqt")