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
