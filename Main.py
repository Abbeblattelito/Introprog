__author__ = 'iversen'
# -*- coding: UTF-8 -*-
import random

class Player:
    Name = 0
    Print_List = ["One","Two","Three","Four","Five","Six","Pair","Two Pairs", "Three Of A Kind", "Four Of A Kind","YATZY!"]
    Score_List = [0,0,0,0,0,0,0,0,0,0,0]
    Taken = []
    def Count_Score(self):
        self.Score = self.One+self.Two+self.Three+self.Four+self.Five+self.Six

    def Save(self,Place):
        if Place == 1 and not (1 in self.Taken):
            n = dice.list.count(1)
            self.Score_List[Place-1] = n*1
            self.Taken.append(1)
        elif Place == 2 and (2 not in self.Taken):
            n = dice.list.count(2)
            self.Score_List[Place-1] = n*2
            self.Taken.append(2)
        elif Place == 3 and (3 not in self.Taken):
            n = dice.list.count(3)
            self.Score_List[Place-1] = n*3
            self.Taken.append(3)
        elif Place == 4 and (4 not in self.Taken):
            n = dice.list.count(4)
            self.Score_List[Place-1] = n*4
            self.Taken.append(4)
        elif Place == 5 and (5 not in self.Taken):
            n = dice.list.count(5)
            self.Score_List[Place-1] = n*5
            self.Taken.append(5)
        elif Place == 6 and (6 not in self.Taken):
            n = dice.list.count(6)
            self.Score_List[Place-1] = n*6
            self.Taken.append(6)
        elif Place == 7 and (7 not in self.Taken):
            if dice.list.count(6) == 2:
                self.Score_List[Place-1] = 12
            elif dice.list.count(5) == 2:
                self.Score_List[Place-1] = 10
            elif dice.list.count(4) == 2:
                self.Score_List[Place-1] = 8
            elif dice.list.count(3) == 2:
                self.Score_List[Place-1] = 6
            elif dice.list.count(2) == 2:
                self.Score_List[Place-1] = 4
            elif dice.list.count(1) == 2:
                self.Score_List[Place-1] = 2
            self.Taken.append(7)
        elif Place == 8 and (8 not in self.Taken):
            if dice.list[0] == dice.list[1] and dice.list[2] == dice.list[3]:
                self.Score_List[Place-1] = dice.list[1]*2+dice.list[3]*2
            elif dice.list[1] == dice.list[2] and dice.list[3] == dice.list[4]:
                self.Score_List[Place-1] = dice.list[1]*2+dice.list[3]*2
            elif dice.list[0] == dice.list[1] and dice.list[3] == dice.list[4]:
                self.Score_List[Place-1] = dice.list[1]*2+dice.list[3]*2
            self.Taken.append(8)
        elif Place == 9 and (9 not in self.Taken):
            if dice.list.count(6) == 3:
                self.Score_List[Place-1] = 18
            elif dice.list.count(5) == 3:
                self.Score_List[Place-1] = 15
            elif dice.list.count(4) == 3:
                self.Score_List[Place-1] = 12
            elif dice.list.count(3) == 3:
                self.Score_List[Place-1] = 9
            elif dice.list.count(2) == 3:
                self.Score_List[Place-1] = 6
            elif dice.list.count(1) == 3:
                self.Score_List[Place-1] = 3
            self.Taken.append(9)
        elif Place == 10 and (10 not in self.Taken):
            if dice.list.count(6) == 4:
                self.Score_List[Place-1] = 24
            elif dice.list.count(5) == 4:
                self.Score_List[Place-1] = 20
            elif dice.list.count(4) == 4:
                self.Score_List[Place-1] = 16
            elif dice.list.count(3) == 4:
                self.Score_List[Place-1] = 12
            elif dice.list.count(2) == 4:
                self.Score_List[Place-1] = 8
            elif dice.list.count(1) == 4:
                self.Score_List[Place-1] = 4
            self.Taken.append(10)
        elif Place == 11:
            n = dice.list.count(dice.list[0])
            if n == 5:
                self.Score_List[Place-1] = n*dice.list[0]
            self.Taken.append(11)
        else:
            return False
        return True
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
    name = raw_input("Vad ska spelare %s heta? " %int(x+1))
    spelare[x].Name = name


game = True
dice=Dice()
Place = 0
while game:
    for Player in spelare:
        print "%s tur:" %Player.Name
        dice.Roll()
        print dice.list
        for i in range(2):
            saves = raw_input("Vilka vill du spara ")
            dice.ReRoll(saves)
            print dice.list
        for i in range(len(Player.Score_List)):
            print "(%s) %s: %s" %(i+1,Player.Print_List[i],Player.Score_List[i])
        print "Du har: %s" % dice.list

        while not Player.Save(Place):
            Place = int(raw_input("Vart vill du spara? "))
            if Place in Player.Taken:
                print "Du har redan valt (%s)! Välj en ny!" % Place
        Player.Save(Place)