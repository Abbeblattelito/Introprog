# -*- coding: UTF-8 -*-
import random

test

class Player:
    Name = 0
    Print_List = ["One","Two","Three","Four","Five","Six","Pair","Two Pairs", "Three Of A Kind", "Four Of A Kind"]
    Score_List = [0,0,0,0,0,0,0,0,0,0]
    def Count_Score(self):
        self.Score = self.One+self.Two+self.Three+self.Four+self.Five+self.Six
    def Save(self,Place):
        if Place == 1:
            n = dice.list.count(1)
            self.Score_List[Place-1] = n*1
        elif Place == 2:
            n = dice.list.count(2)
            self.Score_List[Place-1] = n*2

class Dice:
    list = []
    def Roll(self):
        self.list = []
        for i in range(5):
            self.list.append(random.randint(1,6))
        self.list.sort()
    def ReRoll(self,saves):
        save = []
        for c in saves:
            save.append(int(c)-1)
        Save_list = []
        for i in save:
            pop = self.list[i]
            Save_list.append(pop)
        while len(Save_list) != 5:
                Save_list.append(random.randint(1,6))
        Save_list.sort()
        self.list = Save_list


# Main
Antal_Spelare = int(raw_input("Hur många spelare? "))
spelare = []
for x in range(Antal_Spelare):
    spelare.append(Player())
    name = raw_input("Vad ska spelare %s heta? " %x)
    spelare[x].Name = name


game = True
dice=Dice()
while game:
    for Player in spelare:
        print "%s tur:" %Player.Name
        dice.Roll()
        print dice.list
        saves = raw_input("Vilka vill du spara ")
        dice.ReRoll(saves)
        print dice.list
        saves = raw_input("Vilka vill du spara ")
        dice.ReRoll(saves)
        for i in range(len(Player.Score_List)):
            print "(%s) %s: %s" %(i+1,Player.Print_List[i],Player.Score_List[i])
        print "Du har: %s" % dice.list
        Place = int(raw_input("Vart vill du spara? "))
        Player.Save(Place)

    break