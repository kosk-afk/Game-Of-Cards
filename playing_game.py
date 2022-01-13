#Game
import random
#Class for cards
class card():
	def __init__(self,val,sym):
		self.value=val
		self.symbol=sym
		if self.symbol in "sc": self.color='B'
		else: self.color='R'
		if self.value in "JQK": self.fig=True
		else: self.fig=False	
	def __str__(self):
		return self.value+self.symbol	
	def detailed_info(self):
		print('Αξια=', self.value, '       Συμβολο=',self.symbol)		

#Class for the deck
class deck():
	values="A23456789TJQK"  #ALL THE PRICES T=10 
	symbols="🔷❤☘⚜"   #ALL THE SYMBOLS   
	def __init__(self):
		self.content=[] #CARDS IN DECK
		self.pile=[]  #CARD OUT OF THE DECK
		for i in deck.symbols:
			for j in deck.values:
				c=card(j,i)
				self.content.append(c)
	def __str__(self):
		s=""
		cntr=0
		for c in self.content:
			s=s+str(c)+""
			cntr=cntr+1	
			if cntr%13==0: s=s+'\n'
		if s[-1]!='\n': s=s+'\n'	
		s=s+str(len(self.content))+"-"+str(len(self.pile))
		return s	
	def shuffle(self):		#shuffle the cards
		random.shuffle(self.content)
	def draw(self):   #give cards to the players
		if len(self.content)<1: return "empty"
		c=self.content[0]
		self.content=self.content[1:]
		self.pile.append(c)
		return c	
	def collect(self):
		self.content=self.content+self.pile	
		self.pile=[]	
d=deck()










