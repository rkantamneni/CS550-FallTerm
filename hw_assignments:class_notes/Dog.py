class Soccer:
	def __init__(self, name, age, pace, shot, passing, dribbling, defence, physical, wage, repsect, social, alcohol):
		self.name = name
		self.pace = pace
		self.shot = shot
		self.age = age
		self.passing = passing
		self.dribling = dribling
		self.defence = defence
		self.physical = physical
		self.wage=wage
		self.game=True
		self.respect = respect
		self.social=social
		self.alcohol=alcohol
	def fitness(self, amount):
		if self.physical > 50 and self.age<35:
			print("You're pretty fit!")
		else:
			print(self.name+" needs more excerscise and/or needs to retire")
			self.physical-=amount
			self.game=False

	def mental(self):
		if pace > 60 and  shot> 60 and passing> 60 and dribbling> 60 and defence> 60 and physcial> 60:
			print(self.name+" is a great professional player with tremendous skill")

		else:
			print("You should find another job")
			self.game=False
	def lockerroom(self):
		if age>28:
			respect=100
		elif age<24:
			respect=70
	def wage(self):
		if pace > 60 and  shot> 60 and passing> 60 and dribbling> 60 and defence> 60 and physcial> 60:
			wage="$100,000"
		if pace > 80 and  shot> 80 and passing> 80 and dribbling> 80 and defence> 80 and physcial> 80:
			wage= "$500,000"
	def social(self)：
		if social>90 and alcohol>80:
			print("You're sitting on the bench")
			game=False


	def stats(self):
		print("Player Stats:")
		print("Name: "+self.name)
		print("Age: "+str(self.age))
		print("Pace: "+str(self.pace))
		print("Shot: "+str(self.shot))
		print("Passing: "+str(self.passing))
		print("Dribbling: "+str(self.dribbling))
		print("Defence: "+str(self.defence))
		print("Physical: "+str(self.physical))
		print("Is Game Ready: "+str(self.game))

player = Soccer("Lionel Messi", 30, 80, 95, 97, 65, 80)
player.fitness(5)
player.stats()
player.fitness(15)
player.stats()
player.fitness(25)
