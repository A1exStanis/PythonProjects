# https://codeforces.com/problemset/problem/492/A

cubes = int(input("Enter number of cubes: "))
floor = 1
cube_for_floor = 1
while cubes - cube_for_floor >= 0:
    cubes = cubes - cube_for_floor
    floor = floor + 1
    cube_for_floor = cube_for_floor +  floor
print(floor-1)
