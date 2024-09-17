import tkinter as tk

class Perso:
	self.HealthPoints = 10
	self.DamagePoints = 2
	
	def receiveDamage(self, damage):
		self.HealthPoints -= damage

class Ennemy:
	self.HealthPoints = 4
	self.DamagePoints = 1
	
	def receiveDamage(self, damage):
		self.HealthPoints -= damage

totem = {hp=10, buff=1} 

def runGame():
	fenetre = tk.Tk()
	

