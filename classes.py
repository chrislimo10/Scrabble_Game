import random
import itertools as it
import json
import os.path

class SakClass:
    def __init__(self):
        self.letters= {'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]
        }
        self.randLetters = []
        for i in self.letters:
            j = self.letters[i][0]

            for k in range(j):
                self.randLetters.append(i)

    def __repr__(self):
        return 'Sack Instance containing the letters'

    def randomize_sak(self):

        random.shuffle(self.randLetters)


    def getletters(self,player,n,p=False):
        if len(self.randLetters)>=n :

          for i in range(n):
              player.playerLetters.append(self.randLetters[0])
              self.randLetters.remove(self.randLetters[0])
        elif p==False:
            letnumber=len(self.randLetters)
            for i in range(letnumber):
                player.playerLetters.append(self.randLetters[0])
                self.randLetters.remove(self.randLetters[0])

        else:
            return False

    def putbackletters(self,player,n):
        for i in range(n):
            self.randLetters.append(player.playerLetters[0])
            player.playerLetters.remove(player.playerLetters[0])

        self.randomize_sak()

    def calculateValue(self,word):
        value = 0
        for i in word:
            value += self.letters[i][1]
        return (value)



class Player:
    def __init__(self):
        self.score = 0
        self.playerLetters = []
    def __repr__(self):
        return 'Parental instance of Human and Computer'




class Human(Player):
    def __init__(self):
        self.name = input("ΠΛΗΚΤΡΟΛΟΓΗΣΕ ΤΟ ΟΝΟΜΑ ΣΟΥ:\n")
        while len(self.name)==0:
            self.name = input("ΠΛΗΚΤΡΟΛΟΓΗΣΕ ΤΟ ΟΝΟΜΑ ΣΟΥ:\n")
        super().__init__()

    def __repr__(self):
        return 'Human player Instance'

    def play(self,sak):

        print("*** Παίκτης: "+self.name+"   *** Σκορ: "+str(self.score))

        letters=''
        for i in range (len(self.playerLetters)):
            letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "

        valid = False
        while valid==False:
          print('Διαθέσιμα γράμματα:' + letters)
          word = input("Πληκτρολόγησε την λέξη που θες , p για να αντικαταστήσεις τα γράμματά σου ή q για τερματισμό του παιχνιδιού:\n")
          while len(word)==0:
              print('Διαθέσιμα γράμματα:' + letters)
              word = input( "Πληκτρολόγησε την λέξη που θες , p για να αντικαταστήσεις τα γράμματά σου ή q για τερματισμό του παιχνιδιού:\n")

          if word == "p":
            holds=len(self.playerLetters)
            if sak.getletters(self,holds,True )==False:
                print('Τα γράμματα που μένουν στο σακουλάκι δεν φτάνουν για να γίνει αλλαγή. Τέλος παιχνιδιού.' )
                return False
            else:
                sak.putbackletters(self, holds)
                letters = ''
                for i in range(len(self.playerLetters)):
                    letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
                print('Τα διαθέσιμα γράμματα μετά τις αλλαγές είναι:' + letters)
                valid = True
                return True;

          elif word== 'q':
              return False

          else:
            templist=self.playerLetters.copy()
            valid=True
            for i in word:
               if i in templist:
                   templist.remove(i)
               else:
                   valid=False
                   break

            if valid == False:
                print("Τα γράμματα που διαθέτεις δεν επαρκούν για την λέξη που πληκτρολόγησες ")
            else:
                if word in Game.wordsdict[word[0]]:
                   value=sak.calculateValue(word)
                   self.score+=value
                   print('Αποδεκτή Λέξη - Βαθμοί: '+str(value)+' - Σκορ: '+str(self.score) )
                   self.playerLetters = templist.copy()
                   sak.getletters(self, 7 - len(self.playerLetters))
                   input("Πάτησε Enter για συνέχεια...")
                   return True;
                else:
                   valid=False
                   print("Η λέξη που πληκτρολόγησες δεν υπάρχει στο λεξικό του παιχνιδιού ")





class Computer(Player):
    def __init__(self):
        self.name='Η/Υ'
        super().__init__()
    def __repr__(self):
        return 'Computer player Instance'

    def play(self,sak,mode):
        print("*** Παίκτης: "+self.name+"   *** Σκορ: "+str(self.score))
        letters = ''
        for i in range(len(self.playerLetters)):
            letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
        print('Διαθέσιμα γράμματα:' + letters)

        if mode=='A':
            return self.minLet(sak)
        elif mode=='B':
            return self.maxLet(sak)
        elif mode == 'C':
            return self.smart(sak)
        else:
            return self.smart2(sak)

    def minLet(self,sak):
        y=2
        while y<8:
            for i in it.permutations(self.playerLetters, y):
                word = ''.join(i)
                if word in Game.wordsdict[word[0]]:
                    value = sak.calculateValue(word)
                    self.score += value
                    print('Λέξη Η/Υ: ' + word + ' - Βαθμοί: ' + str(value) + ' - Σκορ: ' + str(self.score))
                    for j in word:
                        if j in self.playerLetters:
                            self.playerLetters.remove(j)

                    sak.getletters(self, 7 - len(self.playerLetters))
                    return True;
            y=y+1
        holds = len(self.playerLetters)

        if holds == 0:
            print('Έχουν τελειώσει τα γράμματα του υπολογιστή. Τέλος παιχνιδιού')
            return False

        if sak.getletters(self, holds,True) == False:
            print('Τα γράμματα που μένουν στο σακουλάκι δεν φτάνουν για να γίνει αλλαγή. Τέλος παιχνιδιού')
            return False
        else:
            sak.putbackletters(self, Holds)
            letters = ''
            for i in range(len(self.playerLetters)):
                letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
            print('Τα διαθέσιμα γράμματα μετά τις αλλαγές είναι:' + letters)
            return True


    def maxLet(self,sak):
        y = 7
        while y > 1:
            for i in it.permutations(self.playerLetters, y):
                word = ''.join(i)
                if word in Game.wordsdict[word[0]]:
                    value = sak.calculateValue(word)
                    self.score += value
                    print('Λέξη Η/Υ: ' + word + ' - Βαθμοί: ' + str(value) + ' - Σκορ: ' + str(self.score))
                    for j in word:
                        if j in self.playerLetters:
                            self.playerLetters.remove(j)

                    sak.getletters(self, 7 - len(self.playerLetters))
                    return True;
            y = y - 1

        holds = len(self.playerLetters)
        if holds == 0:
            print('Έχουν τελειώσει τα γράμματα του υπολογιστή. Τέλος παιχνιδιού')
            return False

        if sak.getletters(self, holds, True) == False:
            print('Τα γράμματα που μένουν στο σακουλάκι δεν φτάνουν για να γίνει αλλαγή. Τέλος παιχνιδιού')
            return False

        else:
            sak.putbackletters(self, holds)
            letters = ''
            for i in range(len(self.playerLetters)):
                letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
            print('Τα διαθέσιμα γράμματα μετά τις αλλαγές είναι:' + letters)
            return True

    def smart(self,sak):
        possibleWords=[]
        values=[]
        for y in range (2,8):
            for i in it.permutations(self.playerLetters, y):
                word = ''.join(i)
                if word in Game.wordsdict[word[0]]:
                    value = sak.calculateValue(word)
                    possibleWords.append(word)
                    values.append(value)
        if len(possibleWords)==0:

            holds = len(self.playerLetters)
            if holds==0:
                print('Έχουν τελειώσει τα γράμματα του υπολογιστή. Τέλος παιχνιδιού')
                return False
            if sak.getletters(self, holds, True) == False :
                print('Τα γράμματα που μένουν στο σακουλάκι δεν φτάνουν για να γίνει αλλαγή. Τέλος παιχνιδιού')
                return False
            else:
                sak.putbackletters(self, holds)
                letters = ''
                for i in range(len(self.playerLetters)):
                    letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
                print('Τα διαθέσιμα γράμματα μετά τις αλλαγές είναι:' + letters)
                return True

        else:
            maxv = max(values)
            index = values.index(maxv)
            self.score += maxv
            print('Λέξη Η/Υ: ' + possibleWords[index] + ' - Βαθμοί: ' + str(maxv) + ' - Σκορ: ' + str(self.score))
            for j in possibleWords[index]:
                if j in self.playerLetters:
                    self.playerLetters.remove(j)

            sak.getletters(self, 7 - len(self.playerLetters))
            return True;

    def smart2(self,sak):
        wordsFound=[]
        values=[]
        for y in range (2,8):
            for i in it.permutations(self.playerLetters, y):
                word = ''.join(i)
                if word in Game.wordsdict[word[0]]:
                    wordsFound.append(word)
                    value = sak.calculateValue(word)
                    values.append(value)

        if len(wordsFound)!=0:

            chosen = max(values)
            position = values.index(chosen)
            chosenWord = wordsFound[position]
            self.score += chosen
            print('Λέξη Η/Υ: ' + chosenWord + ' - Βαθμοί: ' + str(chosen) + ' - Σκορ: ' + str(self.score))
            for j in chosenWord:
                if j in self.playerLetters:
                    self.playerLetters.remove(j)

            sak.getletters(self, 7 - len(self.playerLetters))
            return True;


        else:
            playerHolds = len(self.playerLetters)
            if playerHolds == 0:
                print('Έχουν τελειώσει τα γράμματα του υπολογιστή. Τέλος παιχνιδιού')
                return False
            if sak.getletters(self, playerHolds, True) == True:
                sak.putbackletters(self, playerHolds)
                letters = ''
                for i in range(len(self.playerLetters)):
                    letters += " " + self.playerLetters[i] + "," + str(sak.letters[self.playerLetters[i]][1]) + " "
                print('Τα διαθέσιμα γράμματα μετά τις αλλαγές είναι:' + letters)
                return True

            else:
                print('Τα γράμματα που μένουν στο σακουλάκι δεν φτάνουν για να γίνει αλλαγή. Τέλος παιχνιδιού')
                return False

class Game:
    words = []
    moves=0
    wordsdict={'Α':[],'Β':[],'Γ':[],'Δ':[],'Ε':[],
        'Ζ':[],'Η':[],'Θ':[],'Ι':[],'Κ':[],
        'Λ':[],'Μ':[],'Ν':[],'Ξ':[],'Ο':[],
        'Π':[],'Ρ':[],'Σ':[],'Τ':[],'Υ':[],
        'Φ':[],'Χ':[],'Ψ':[],'Ω':[]
        }

    def __init__(self):
        self.ph= Human()
        self.pc = Computer()
        self.sak = SakClass()

    def __repr__(self):
        return 'Game Instance'


    def setup(self,mode):

       self.sak.randomize_sak()

       if mode!='E':
           with open('greek7expert.txt', 'r', encoding="utf-8") as f7:
               for line in f7:
                   Game.words.append(line.strip('\n'))
                   Game.wordsdict[line[0]].append(line.strip('\n'))
       else:
           with open('greek7expert.txt', 'r', encoding="utf-8") as f7:
               for line in f7:
                   Game.words.append(line.strip('\n'))
                   Game.wordsdict[line[0]].append(line.strip('\n'))

    def run(self,mode):

        self.sak.getletters(self.ph, 7)
        self.sak.getletters(self.pc, 7)
        run = True
        while run == True:
            print("*************************************")
            print("Στο σακουλάκι: " + str(len(self.sak.randLetters)) + ' γράμματα')
            run = self.ph.play(self.sak)
            Game.moves+=1
            if run == False:
                break
            print("*************************************")
            print("Στο σακουλάκι: " + str(len(self.sak.randLetters)) + ' γράμματα')
            run = self.pc.play(self.sak, mode)
            if run == False:
                break
            Game.moves+=1

    def end(self):
        print("*************************************")
        if self.ph.score>self.pc.score:
            print('Συγχαρητήρια!! Είστε νικητής!!')
            print('Παίκτης: '+self.ph.name+' - Πόντοι: '+str(self.ph.score))
            print('Παίκτης: '+self.pc.name+' - Πόντοι: '+str(self.pc.score))

        elif self.ph.score==self.pc.score:
            print('Το παιχνίδι έληξε με ισοπαλία')
            print('Παίκτης: '+self.ph.name+' - Πόντοι: '+str(self.ph.score))
            print('Παίκτης: '+self.pc.name+' - Πόντοι: '+str(self.pc.score))
        else:
            print('Δυστυχώς χάσατε. Νικητής είναι ο Υπολογιστής')
            print('Παίκτης: '+self.pc.name+' - Πόντοι: '+str(self.pc.score))
            print('Παίκτης: '+self.ph.name+' - Πόντοι: '+str(self.ph.score))

        stats={'name':self.ph.name,'moves':Game.moves,'userscore':self.ph.score,'pcscore':self.pc.score}

        exists = os.path.exists('scoreboard.json')

        if exists == False:
            print(exists)
            with open('scoreboard.json', 'w') as f:
                json.dump([], f)

        listObj = []
        with open("scoreboard.json") as fp:
            listObj = json.load(fp)
        listObj.append(stats)
        with open("scoreboard.json", "w") as outfile:
            json.dump(listObj, outfile)

        print("*************************************")
