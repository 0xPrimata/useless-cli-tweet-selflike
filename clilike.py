import numpy as np
import sys
import tweepy

if len(sys.argv) > 4:
    print('Too many arguments')
    sys.exit()

if len(sys.argv) < 4:
    print('You have to input your user, password, consumer key and consumer secret. In that order.\n Me not stealing it, pinky promise.')
    sys.exit()

auth = tweepy.OAuthHandler(sys.argv[3], sys.argv[4])
user = sys.argv[1]
password = sys.argv[2]

api = tweepy.API(auth)

print("Would you like to like your latest tweet? y/n")
status = api.home_timeline(count = 1)
a = input()

if a == "n":
    print("Good choice")
    sys.exit()

while (a !='y'):
    print("Typo mate, it's y, not yes, not Yes, not Y. Just 'y'")
    a = input()

print("Are you sure? You are liking your OWN tweet. That's sad.")
b = input()

while (b !='Y'):
    print("Typo mate, it's Y, not yes, not Yes, not y. Just 'Y'")
    b = input()

print("uhh okay then. You sure? y/n")
c = input()

while (c !='y'):
    print("Typo mate, it's y, not yes, not yes, not Y. Just 'y'")
    c = input()

print("you will be able to dislike it later on, naturally.")
d = input()

while (c !='okay'):
    print("I don't need an yes or no, just say 'okay', dummie")
    d = input()

api.create_favorite(status.id)

print("okay, now your fate will be decided by this computing intensive 48.5/51.5 (life ain't easy) sofisticated mechanism we've created.\nIt should take you about an hour to know if you were granted a like to your own tweet.")

def random_it(amount):
    counter = 0
    while amount != 0:
        amount += np.random.choice([-1,1], p=[0.515, 0.485])
        counter+=1
    return counter

list = [200, 200, 200, 200]
b = []
for a in list:
    c = []
    for i in range(1000):
        c.append(random_it(a))
    b.append(np.mean(c))
print(b)
if np.mean(b) > 3320:
    api.create_favorite(status.id)
    print("You were lucky.")
    sys.exit()
else:
    print("Ohh too bad. You can try it again :D")
    sys.exit()