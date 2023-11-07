# https://codeforces.com/problemset/problem/460/A

count_socks, day = map(int,input("Enter socks and day").split())
current_day = 0
while count_socks > 0:
    count_socks -= 1
    current_day += 1
    if current_day % day == 0:
        count_socks += 1

print(current_day)