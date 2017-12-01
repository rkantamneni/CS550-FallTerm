import sys

first=[
"stinky", "lumpy", "buttercup","gidget","crusty","greasy","fluffy","cheeseball","chim-chim","poopsie","flunky","booger","pinky","zippy","goober","doofus","slimy","loopy","snotty","falafel","dorkey","squeezit","oprah","skipper","dinky","zsa-zsa"]
last=[
"diaper","toilet","giggle","bubble","girdle","barf","lizard","waffle","cootie","monkey","potty","liver","banana","rhino","burger","hamster","toad","gizzard","pizza","gerbil","chicken","pickle","chuckle","tofu","gorilla","stinker"]
last22=[
"head", "mouth", "face", "nose", "tush", "breath", "pants", "shorts", "lips", "honker", "butt", "brain", "tushie", "chunks", "hiney", "biscuits", "toes", "buns", "fanny", "sniffer", "sprinkles", "kisser", "squirt", "humperdinck", "brains", "juice"] 
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

name = input("What is your first and last name? ")

fullname=[name.lower().split(' ')]
first1=fullname[0][0]
last1=fullname[0][1]

for i in range(0,25):
	if first1[0]==alpha[i]:
		x=first[i]

	if last1[0]==alpha[i]:
		y=last[i]

	if last1[-1]==alpha[i]:
		print(last1[-1])
		z=last22[i]

print("Your changed name is "+x+" "+y+" "+z)










