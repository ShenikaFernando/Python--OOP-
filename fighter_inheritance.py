class Fighter:

	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attack(self, other_guy):
		other_guy.health = other_guy.health - self.damage
		print("{} attacks {}!".format(self.name, other_guy.name))
		print("{} loses {} health points!".format(other_guy.name, self.damage))


	def __str__(self):
		return "{}: {}".format(self.name, self.health)

jess = Fighter("Jess")
you = Fighter("Pin")

print(jess)
print(you)

#attack first time
you.attack(jess)
jess.attack(you)

print(jess.health)
print(you.health)

#attack second time
you.attack(jess)


#inherit from Fighter class
class Boxer(Fighter):
	def heal(self):
		self.health += 10

boxer_jess = Boxer("Boxer Jess")
print(boxer_jess)
print(boxer_jess.health)

boxer_jess.heal()
print(boxer_jess)