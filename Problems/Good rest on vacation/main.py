# put your python code here
day = int(input())
food = int(input()) * day
flight = int(input()) * 2
hotel = int(input()) * (day - 1)
print(food + flight + hotel)
