#Optional Try to create a function that will do reverse operation - from integer to Roman
int_roman = {
    900:"CM",1000:"M",400:"CD",
    500:"D",90:"XC",100:"C",50:"XL",
    50:"L",10:"X",9:"IX",4:"IV",5:"V",1:"I"
     }
hard_list = [
    2,3,6,7,8,20,30,
    60,70,80,200,
    300,600,700,800
    ]

def int_to_roman(r: int) -> str:   
    int_list = []
    prsnt = 10
    for i in str(r):
        if r%prsnt != 0:
            int_list.append(r%prsnt)
            r = r - r%prsnt
        prsnt *=10
    easy_list = []
    int_list.reverse()
    next_step(int_list,easy_list)

    
def next_step(int_list,easy_list):
    for x in int_list:
        if x not in hard_list:
            easy_list.append(x)
        else:
            while x >= 100: 
                if x>=500:
                    x = x - 500
                    easy_list.append(500)
                if x >= 100:    
                    while x > 0:
                        easy_list.append(100)
                        x -= 100
            while x >= 10 and x < 100: 
                if x >= 50:
                    x = x - 50
                    easy_list.append(50)
                if x >= 10:
                    for i in range(x//10):
                        x -= 10
                        easy_list.append(10)
            while x > 0 and x < 10: 
                if x>=5:
                    x = x - 5
                    easy_list.append(5)
                if x >= 1:    
                    for i in range(x):
                        easy_list.append(1)
                        x -= 1
    test_int_to_roman(easy_list)
    

def test_int_to_roman(easy_list):
    easy_list.sort(reverse=True)
    print(easy_list)
    sum_ = []
    for i in easy_list:
        sum_.append(int_roman[i])
    sum_ = "".join(sum_)   
    print(sum_)    


int_to_roman(1036)