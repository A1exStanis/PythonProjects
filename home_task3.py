# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
# To each file append a random number between 1 and 100. Create a summary file (summary.txt)
# that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98
import random

file_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
summery = open("Files2/summery.txt","a")
for name in file_name:
    with open(f"Files2/{name}.txt","w") as file:
        rand = random.randint(1,100)
        file.write(str(rand))
        summery.write(f"{name}.txt:{rand} \n")
summery.close()


# Create a file with some content. As example, you can take this one:

# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
# labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
# laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
# voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
# proident, sunt in culpa qui officia deserunt mollit anim id est laborum”.

# Create a second file and copy the content of the first file to the second file in upper case.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut \nlabore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco \nlaboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in \nvoluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non \nproident, sunt in culpa qui officia deserunt mollit anim id est laborum"
with open("Files2/text1.txt", "w") as file:
    file.write(text)
with open("Files2/text1.txt", "r") as file:    
    text = file.read()
with open("Files2/text2.txt", "w") as file:
    for line in text:
        line = line.upper()
        file.write(line)


# Write a program that will simulate user scores in a game. Create a list with 5 players’ 
# names after that simulate 100 rounds for each player. As a result of the game create a list
#  with the player's name and score (0-1000 range). And save it to a CSV file. The file should look like this:

# Player name, Score
# Josh, 56
# Luke, 784
# Kate, 90
# Mark, 125
# Mary, 877
# Josh, 345
# ...

import csv
import random

list_ = ["Josh","Luke","Kate","Mark","Mary"]
scorelist =[]

for round in range(100):
    for name in list_:
        score = random.randint(1,1000)
        scorelist.append([name,score])
        

with open("Files2/scorelist.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Score"])    
    for points in scorelist:   
           writer.writerow(points)     


# Write a script that reads the data from the previous CSV file and creates a new file called high_scores.csv 
# where each row contains the player name and their highest score. 
# The final score should be sorted by descending to the highest score. The output CSV file should look like this:

# Player name, Highest score
# Kate, 907
# Mary, 897
# Luke, 784
# Mark, 725
# Josh, 345

import csv

new_dict ={}
with open("Files2/scorelist.csv", mode="r") as file:
    reader = csv.DictReader(file)
    list_ = [row for row in reader]
list_ = sorted(list_, key=lambda x: x["Score"])

for row in list_:
     new_dict[row["Name"]]={}
     for res in list_:
          new_dict[row["Name"]]=row["Score"]
new_dict = sorted(new_dict.items(), reverse=True, key=lambda x: x[1])

with open("Files2/highestscore.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name","Highest score"])
    for points in new_dict:   
            writer.writerow(points)