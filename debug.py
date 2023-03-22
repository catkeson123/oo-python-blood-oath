import ipdb
from lib import *

# test your code here
# e.g.

f1 = Follower('Emiley', 31, 'Living the Dream')
f2 = Follower('Bob', 25, 'Here to Party')
f3 = Follower('Kyle', 40, 'Here for a good time not a long time')

c1 = Cult('Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis', 18)
c2 = Cult('My Cult', 'Denver', 1985, 'Human Metamorphosis', 30)
c3 = Cult('Newest Cult', 'Denver', 1990, 'Human Metamorphosis', 20)

bo1 = BloodOath('2019-09-16', f1, c1)
bo2 = BloodOath('2022-03-10', f1, c2)
bo3 = BloodOath('2022-03-10', f3, c2)
bo4 = BloodOath('2022-03-10', f2, c1)
bo5 = BloodOath('2022-03-10', f3, c1)
bo6 = BloodOath('2022-03-10', f3, c3)

print("Mwahahaha!")
ipdb.set_trace()
