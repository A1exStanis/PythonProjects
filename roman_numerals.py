# Symbol Value
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written from largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a Roman numeral, convert it to an integer.
roman = {
        "CM":900,"M":1000,"CD":400,
        "D":500,"XC":90,"C":100,"XL":50,
        "L":50,"X":10,"IX":9,"IV":4,"V":5,"I":1
         }
two_sumb = ["CM", "CD", "XC", "XL", "IX", "IV"]

def roman_to_int(r: str,roman=roman,two_sumb=two_sumb) -> int:
    roman_list = []
    next_step(roman,two_sumb,roman_list,r)
    
def next_step(roman,two_sumb,roman_list,r):    
    for i,il in enumerate(r):
        while r[i:i+2] in roman:
            roman_list.append(r[i:i+2])
            r = r[i+2:]
            return next_step(roman,two_sumb,roman_list,r)   
        roman_list.append(r[i])
        r = r[i+1:]
        return next_step(roman,two_sumb,roman_list,r)
    print(roman_list)
    return test_roman_to_int(roman_list,roman)


def test_roman_to_int(roman_list,roman):
    sum_ = 0
    for q in roman_list:
        sum_ += roman[q]
    print(sum_)

roman_to_int('CM')