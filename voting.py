# https://codeforces.com/problemset/problem/1030/A

def voting():
    voters_count = int(input("How many voters?"))
    marks_list = map(int,input("Type marks:").split())
    if 1 in marks_list:
        print("Hard")
    else:
        print("Easy")

voting()