from typing import List

dinlista = []
fortsätt = True
##9 \n mellan varje programmgrej
print("\n"*40)
while fortsätt:

    print("Vad vill du göra?\n1. Titta på hela listan             2. Titta på en specifik listposition\n3. Lägga till ett värde i listan    4. Ta bort ett värde i listan\n5. Sortera listan                   6. Beräkna listans medelvärde\n7. Avsluta")
    try:
        val = int(input("\n\n\n\nAnge ditt val -> "))
        

        if val == 1:
            listPositioner = len(dinlista) -1
            if  listPositioner < 0:    
                print("\n"*40)
                print("Din lista är tom\n\n")        
            else:    
                print("\n"*40)
                print(f"Här är din lista {dinlista}\n\n")

        if val == 2:
            listPositioner = len(dinlista) -1
            print("\n"*40)
            print(f"Här är listan -> {dinlista}\nFörsta positionen är 0, andra 1 osv\n\n\n\n\n\n\n")
            positionsval = int(input("Ange listnummer du vill titta på -> "))


            if positionsval > listPositioner:
                print("\n"*40)
                print("Positionen finns ej i listan\n\n")

            else:
                print(dinlista[positionsval])

        if val == 3:
            print("\n"*40)
            inlägg = int(input("Vilket tal vill lägga till i din lista? \n\n\n\n\n\n\n\n\nSkriv här ->"))
            dinlista.append(inlägg)
            print("\n"*40)
            print(f"\ndu lade in {inlägg} i listan\n\n")

        if val == 4:
            listPositioner = len(dinlista) -1
            print("\n"*40)
            print(f"Här är listan -> {dinlista}\nFörsta positionen är 0, andra 1 osv\n\n\n\n\n\n\n")
            positionsval = int(input("Vilken positions värde i listan du vill ta bort -> "))


            if positionsval > listPositioner:
                print("\n"*40)
                print("Det finns inget värde på positionen angiven\n\n")

            else:
                removed = dinlista.pop(positionsval)
                print("\n"*40)
                print(f"\nDu tog bort värdet {removed} från position {positionsval}\n\n")


        if val == 5:
            listPositioner = len(dinlista) -1
            if  listPositioner < 0:    
                print("\n"*40)
                print("Din lista är tom\n\n")

            elif listPositioner == 0:
                print("\n"*40)
                print(f"Du har endast ett värde i din lista\n\n")


            else:
                dinlista.sort(reverse=False)
                print("\n"*40)
                print(f"Din är nu sorterad på detta vis {dinlista}\n\n")


        if val == 6:
            listPositioner = len(dinlista) -1
            if  listPositioner < 0:    
                print("\n"*40)
                print("Din lista är tom\n\n")


            elif listPositioner == 0:
                print("\n"*40)
                print(f"Du har endast ett värde i din lista\n\n")

            else:
                listSumma = sum (dinlista)
                listLängd = len (dinlista)
                listMedelvärde = listSumma /listLängd 
                print("\n"*40)
                print(f"Medelvärdet av din lista är: {listMedelvärde}\n\n")


        if val == 7:
            fortsätt = False
            print("\n"*40)
            print("\nProgrammet är nu avslutat\n\n\n\n\n\n\n")
        
        if val > 7:
            print("\n"*40)
            print("Inkorrekt inskrivet\n\n")

        if val < 1:
            print("\n"*40)
            print("Inkorrekt inskrivet\n\n")


    except:
        print("\n"*40)
        print("Inkorrekt inskrivet\n\n")