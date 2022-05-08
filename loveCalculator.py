
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
count1 = 0
count2 = 0

# count the number of true character in both name
for i in 'true':
    nc1 = name1.count(i)
    nc2 = name2.count(i)
    count1 = count1 + nc1 + nc2

# count the number of love character in both name
for i in 'love':
    nc1 = name1.count(i)
    nc2 = name2.count(i)
    count2 = count2 + nc1 + nc2


score = int(str(count1) + str(count2))

if  (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score < 50) and (score > 40):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.",)
