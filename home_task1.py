# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. 
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). 
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# In The first round, you stop at every cat, placing a hat on each one.
# In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# Optional: Make a function that can calculate hats with any amount of rounds and cats.



def cat_in_hats(number_cats,number_round):
    dict_of_cats = {}
    for i in range(1,number_cats+1):
        dict_of_cats.update({i:0})
    return second_step(number_round,dict_of_cats)


def second_step(number_round,dict_of_cats):
    for numb_round in range(1,number_round+1):
        for key in dict_of_cats:
            if key % numb_round == 0:
                if dict_of_cats[key] == 1:
                    dict_of_cats[key] = 0
                else:
                    dict_of_cats[key] = 1
    return result(dict_of_cats)


def result(dict_of_cats):
    result = []
    for cat in dict_of_cats:
        if dict_of_cats[cat] == 1:
            result.append(cat)
    print(result)


cat_in_hats(number_cats = 100,number_round = 100)