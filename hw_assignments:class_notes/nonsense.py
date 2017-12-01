import sys

first = ["stinky","lumpy","buttercup","gidget","crusty","greasy","fluffy","cheeseball","chim-chim","poopsie","flunky","booger","pinky","zippy","goober","doofus","slimy","loopy","snotty","falafel","dorkey","squeezit","oprah","skipper","dinky","zsa-zsa"]

middle = ["diaper","toilet","giggle","bubble","girdle","barf","lizard","waffle","cootie","monkey","potty","liver","banana","rhino","burger","hamster","toad","gizzard","pizza","gerbil","chicken","pickle","chuckle","tofu","gorilla","stinker"]

last = ["head","mouth","face","nose","tush","breath","pants","shorts","lips","honker","butt","brain","tushie","chunks","hiney","biscuits","toes","buns","fanny","sniffer","sprinkles","kisser","squirt","humperdinck","brains","juice"]

userinput = input("What is your name? ")
username = userinput.strip().lower().split(" ")

indexfirst = ord(username[0][0])-97
indexmiddle = ord(username[1][0])-97
indexlast = ord(username[1][-1])-97
print("Computer dubs thee: "+ first[indexfirst]+" "+middle[indexmiddle]+last[indexlast])