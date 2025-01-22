import classes
import json
import os.path

def guidelines():
    """
         Οι κλάσεις που έχουν υλοποιηθεί είναι οι SakClass, Player, Human, Computer και Game.

         Αναφορικά με την κληρονομικότητα , η κλάση Player είναι η βασική , ενώ οι Player και Human οι παράγωγες. Η
         επέκταση μεθόδων αφορά απλά τον κατασκευαστή των κλάσεων Player και Human που επεκτείνουν αυτόν της βασικής
         κλάσης Player.

         Οι λέξεις της γλώσσας έχουν οργανωθεί σε μια δομή λεξικού με κλειδί κάθε γράμμα του ελληνικού αλφάβητου και τιμή
         μια λίστα από λέξεις που ξεκινάνε με αυτό το γράμμα. Έτσι γίνεται πολύ πιο γρήγορα η εύρεση μιας λέξης σε σχέση
         με το αν ήταν αποθηκευμένες σε μια απλή λίστα.

         Οι αλγόριθμοι που υλοποιήθηκαν περιλαμβάνει τους MIN Letters, MAX Letters και  SMART.

         ΣΗΜΕΙΩΣΗ: Για την εκτέλεση του SMART χρησιμοποιείται η ίδια συνάρτηση smart 2 κα κατά το setup χρησιμοποιείται το αρχείο
         greek7expert.txt αντί για το greek7.txt.
            """



mode = 'A'
while True:
    print("***** SCRABLE *****")
    print("-------------------")
    print("1: ΣΚΟΡ")
    print("2: ΡΥΘΜΙΣΕΙΣ")
    print("3: ΠΑΙΧΝΙΔΙ")
    print("q: ΕΞΟΔΟΣ")
    print("-------------------")
    option = input()

    while (option != "1" and option != "2" and option != "3" and option != "q"):
        print("-------------------")
        print("1: ΣΚΟΡ")
        print("2: ΡΥΘΜΙΣΕΙΣ")
        print("3: ΠΑΙΧΝΙΔΙ")
        print("q: ΕΞΟΔΟΣ")
        print("-------------------")
        print("ΔΙΑΛΕΞΕ ΜΙΑ ΑΠΟ ΤΙΣ ΠΑΡΑΠΑΝΩ ΕΠΙΛΟΓΕΣ")
        option = input()

    if option == "q":
        print("ΕΛΠΙΖΟΥΜΕ ΝΑ ΣΕ ΞΑΝΑΔΟΥΜΕ")
        break

    elif option == "1":
        exists = os.path.exists('scoreboard.json')

        if exists == False:
            with open('scoreboard.json', 'w') as f:
                print("ΔΕΝ ΕΧΕΙ ΓΙΝΕΙ ΚΑΤΑΓΡΑΦΗ ΣΚΟΡ ΠΡΟΗΓΟΥΜΕΝΩΝ ΠΑΙΚΤΩΝ")
                json.dump([], f)
        else:
            listObj = []
            with open("scoreboard.json") as fp:
                listObj = json.load(fp)
            print('********ΣΤΑΤΙΣΤΙΚΑ ΠΡΟΗΓΟΥΜΕΝΩΝ ΠΑΙΧΝΙΔΙΩΝ********')
            for i in range (len(listObj)):
                print('Όνομα: '+listObj[i]['name']+' - Σκορ παίκτη: '+str(listObj[i]['userscore'])
                      +' - Σκορ υπολογιστή: '+str(listObj[i]['pcscore'])
                      +' - Κινήσεις που έγιναν: '+str(listObj[i]['moves']))
            input("Πάτησε Enter για συνέχεια...")

    elif option == "2":
        print("-------------------")
        print("ΔΙΑΛΕΞΕ ΚΑΠΟΙΟΝ ΑΠΟ ΤΟΥΣ ΠΑΡΑΚΑΤΩ ΑΛΓΟΡΙΘΜΟΥΣ")
        print("Ο ΠΡΟΚΑΘΟΡΙΣΜΕΝΟΣ ΕΙΝΑΙ Ο ΜΙΝ Letters")
        print("-------------------")
        print("ΑΛΓΟΡΙΘΜΟΙ ΤΟΥ ΑΕΜ 3687")
        print("Α: ΜΙΝ Letters")
        print("B: ΜΑΧ Letters")
        print("C: SMART")
        print("-------------------")
        print("ΑΛΓΟΡΙΘΜΟΙ ΤΟΥ ΑΕΜ 3753")
        print("D: SMART")
        print("E: EXPERT")




        mode = input()
        while (mode != "A" and mode != "B" and mode != "C" and mode != "D" and mode != "E"):
            print("-------------------")
            print("ΔΙΑΛΕΞΕ ΚΑΠΟΙΟΝ ΑΠΟ ΤΟΥΣ ΠΑΡΑΚΑΤΩ ΑΛΓΟΡΙΘΜΟΥΣ")
            print("Ο ΠΡΟΚΑΘΟΡΙΣΜΕΝΟΣ ΕΙΝΑΙ Ο ΜΙΝ Letters")
            print("ΑΛΓΟΡΙΘΜΟΙ ΤΟΥ ΑΕΜ 3687")
            print("Α: ΜΙΝ Letters")
            print("B: ΜΑΧ Letters")
            print("C: SMART")
            print("")
            print("ΑΛΓΟΡΙΘΜΟΙ ΤΟΥ ΑΕΜ 3753")
            print("D: SMART")
            print("E: EXPERT")

            print("ΔΙΑΛΕΞΕ ΜΙΑ ΑΠΟ ΤΙΣ ΠΑΡΑΠΑΝΩ ΕΠΙΛΟΓΕΣ")
            mode = input()
        print('Η ΑΛΛΑΓΗ ΠΡΑΓΜΑΤΟΠΟΙΗΘΗΚΕ ΕΠΙΤΥΧΩΣ ')
        input("Πάτησε Enter για συνέχεια...")


    elif option == "3":
        game = classes.Game()
        game.setup(mode)
        game.run(mode)
        game.end()
        print("ΕΛΠΙΖΟΥΜΕ ΝΑ ΣΕ ΞΑΝΑΔΟΥΜΕ")
        break
