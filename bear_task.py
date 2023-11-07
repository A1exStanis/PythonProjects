# https://codeforces.com/problemset/problem/791/A

limak, bob = map(int,input("Enter the weight:").split())
year = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    year += 1
print(f"Limak need {year} years for that")