D = input()
N = int(input())
X = N % 7 - 1

Days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if D in Days:
    Init_index = Days.index(D)
    Days = list(Days)
    print(Days[Init_index + X])
