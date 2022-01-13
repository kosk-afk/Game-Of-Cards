#for better game experience copy and paste the card you want bcs i use emojis for the symbols
# Import the required Libraries
from playing_game import *
from tkinter import *
import sys
#Create an instance of tkinter frame
win= Tk()

#Set the geometry for the window or frame
win.geometry("300x200")

#Create a button
Button(win, text='Click to Open The Game ',font=('Poppins bold', 10),
command=win.destroy).pack(pady=30)

#Create a Label after button event
text= Label(win, text= "", font= ('Poppins bold', 10))
text.pack(pady=20)
#Keep running the window or frame

win.mainloop()


#function for AI 
def AI_plays():
	global d, table, AI_hand, what_happend   #global variables d=deck, table+AI_hand=[],what_happened=hold the game data 
	target_val=table[-1].value #bcs table is on global variables his output is the same whenever we call it 
	target_sym=table[-1].symbol
	while True:
		for c in AI_hand: #c=card , AI checking the cards in his hand until he find a card with same symbol or same value
			if c.value==target_val or c.symbol==target_sym:#target_val card in the table with a specific value, target_sym card in the table with a specific symbol
				print("Το AI  παίζει... ",c)
				AI_hand.remove(c)
				table.append(c)
				what_happend="AI_played"
				return

		new_card=d.draw()
		if new_card=="empty": #if the card which AI get is nothing this means that our deck is end
			what_happend="deck_finished"
			return
		else:
			print("Το AI τραβάει φύλλο... ")#if AI dont have a card to play he must draw a new card
			AI_hand.append(new_card)
#function for printing the situation of the game
def print_info():
	global d, table, AI_hand, what_happend
	print()
	print("Η τράπουλα έχει ", len(d.content),  "φύλλα")
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	print("Το  AI έχει ", len(AI_hand),  "φύλλα")
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	print("Στο τραπέζι έχουν πέσει ", len(table),  "φύλλα")
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	print("Το πάνω φύλλο είναι",table[-1])
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	print("Τα φύλλα σου  είναι",len(human_hand))
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	DDJ=[str(x) for x in human_hand] #we make this variable bcs if we try to call the human_hand we will get memory addresses 
	#we make a new list which can print  the human_hand
	print(DDJ)
	print("〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰")
	print("Διάλεξε ποιο θα πετάξεις... ")
	print("ή πάτα απλά΄ ENTER για να τραβήξεις")

#function for human
def human_plays():
	global d, table, human_hand, what_happend
	while True:
		print_info()
		ac=input()  # player put the card he wants to play
		if ac=="":  # checking if player press enter and if the deck dosn't finish to give the player a card
			new_card=d.draw()
			if new_card=="empty":
				what_happend="deck_finished"
				return
			else:       human_hand.append(new_card)
		else:
			DDJ=[str(x) for x in human_hand]
			if not(ac in DDJ): #if the player try to play a card which dont exist or dosn't have it get and error
				print(ac,  "!!! Δεν έχεις τέτοιο φύλλο...")
			else:
				t=table[-1]
				target_val=t.value
				target_sym=t.symbol
				if ac[0]!=target_val and ac[1]!=target_sym:   #if the player try to play  a different card from his hand get an error
					print("Απαγορεύεται να ρίξεις το φύλλο!!! ",ac)	
				else:
					print("Ρίχνεις το",ac)
					ind=DDJ.index(ac)
					adc=human_hand[ind]
					human_hand.remove(adc)
					table.append(adc)
					what_happend="human_played"
					return
#function which run all the basic modes for a round
def round():
	global d, table, AI_hand, human_hand, what_happend
	print("Μαζεύω τα χαρτιά ...")
	d.collect()					#<------            #now we use modes from the library whe create			
	table=[]
	AI_hand=[]
	human_hand=[]
	print("Ανακατεύω τα φύλλα της τράπουλας ...")
	d.shuffle()                 #<------
	print("Μοιράζω τα φύλλα ...")
	table.append(d.draw())
	print("Στο τραπέζι έπεσε",table[-1])
	for q in range(7):
		human_hand.append(d.draw())
		AI_hand.append(d.draw())
	print("Στρίβω ένα νόμισμα...", end=" ")#We need a coin to flip to see who gonna play first
	if random.random()<0.5:
		print("... Ο παίχτης παίζει πρώτος")
		what_happend="AI_played"
	else:
		print("... Το AI παίζει πρώτο")	
		what_happend="human_played"
#function which read the content of what_happend and print the correct messages
def show_what_happend():
	global AI_hand, human_hand, what_happend
	if what_happend=="human_wins": print("GG NEXT!!!")
	if what_happend=="AI_wins": print("Το AI ΚΕΡΔΙΣΕ😥")
	if what_happend=="deck_finished": 
		ch=len(AI_hand)
		hh=len(human_hand)
		print("Η τράπουλα τελείωσε, το AI έχει",ch, "φύλλα και ο παίχτης", hh)
		if ch>hh: print("Το AI ΚΕΡΔΙΣΕ😥")
		if ch<hh: print("GG NEXT!!!")
		if ch==hh: print("ΙΣΟΠΑΛΙΑ!!!")
	print()
#function for the turn for each players
def next_turn():  
	global what_happend
	while True:
		if what_happend=="game_start":
			round()
		elif what_happend=="human_played":
			if len(human_hand)==0:
				what_happend="human_wins"
				show_what_happend()
				break
			print()  #Try to make a cool interface for players
			print("〰〰〰〰 ΣΕΙΡΑ ΓΙΑ ΤΟ ΑΙ 〰〰〰〰")	
			print()
			AI_plays()
		elif what_happend=="AI_played":
			if len(AI_hand)==0:
				what_happend="AI_wins"
				show_what_happend
				break
			print()	
			print("〰〰〰〰 ΣΕΙΡΑ ΓΙΑ ΤΟ ΠΑΙΧΤΗ 〰〰〰〰")
			print()
			human_plays()
		elif what_happend=="deck_finished":
			show_what_happend
			break
#ACTUALL MAIN PROGRAMME
print("◾◾◾◾ WELCOME TO THE GAME OF CARDS V.1 ◾◾◾◾")
print("⏳⏳⏳⏳⏳⏳")
print()
#BASIC VARIABLES
d=deck()
table=[]
AI_hand=[]
human_hand=[]
what_happend=""
#Continue the game
next=""
print("Πάμε να παίξουμε το παιχνίδι;")
next=input("Press Yes or No: ")
if next == "yes":
    what_happend="game_start"
    next_turn()
elif next == "no":
        sys.exit()
else:        
	print("Τέλος Προγράμματος")				

	










