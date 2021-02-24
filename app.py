from tkinter import *
from tkinter import ttk

from treys.treys import Card
from treys.treys import Deck
from treys.treys import Evaluator

card = Card()
evaluator = Evaluator()

root = Tk()

root.title("Equity Calculator")
def evaluateHands(h1, h2):
    
    h1Winner = 0
    h2Winner = 0
    for x in range(1000):
        deck = Deck()
        deck.cards.remove(h1[0])
        deck.cards.remove(h1[1])
        deck.cards.remove(h2[0])
        deck.cards.remove(h2[1])
        
        tempBoard = deck.draw(5)
        
        tempScore = evaluator.evaluate(tempBoard, h1)
        tempScore2 = evaluator.evaluate(tempBoard, h2)
        if(tempScore < tempScore2):
            h1Winner = h1Winner + 1
        elif(tempScore > tempScore2):
            h2Winner = h2Winner + 1
    str1 = str(h1Winner / 10) + '%'
    str2 = str(h2Winner / 10) + '%'
    heroEquity.set(str1)
    villainEquity.set(str2)
    

def getEquity(*args):
    try:
        
        hHand = heroHand.get()
        vHand = villainHand.get()
        #treys hands
        htHand = [
            Card.new(hHand[0:2]),
            Card.new(hHand[2:4])
        ]
        vtHand = [
            Card.new(vHand[0:2]),
            Card.new(vHand[2:4])
        ]
        evaluateHands(htHand, vtHand)
    except ValueError:
        pass


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

heroHand = StringVar()
ttk.Label(mainframe, text="Your hand: ").grid(column=1, row=1,sticky=(W,E))
heroHandEntry = ttk.Entry(mainframe, width=7, textvariable=heroHand)
heroHandEntry.grid(column=2, row=1, sticky=(W, E))

heroEquity = StringVar()
ttk.Label(mainframe, textvariable=heroEquity).grid(column=3, row=1, sticky=E)

villainHand = StringVar()
ttk.Label(mainframe, text="Opponent's hand: ").grid(column=1, row=2, sticky=(W,E))
villainHandEntry = ttk.Entry(mainframe, width=7, textvariable=villainHand)
villainHandEntry.grid(column=2, row=2, sticky=(W, E))

villainEquity = StringVar()
ttk.Label(mainframe, textvariable=villainEquity).grid(column=3, row=2, sticky=E)

ttk.Button(mainframe, text="Enter", command=getEquity).grid(column=2, row=3, sticky=(W,E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
heroHandEntry.focus()
root.bind("<Return>", getEquity)
root.mainloop()


