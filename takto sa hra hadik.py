#otvorenie suborov
subor = open("hada.txt","r")
subor1 = open("hada_kopia.txt","w")

#zadeklarovanie premennych
hra = 0
hry = 0
max_kroky = 0
momentalne_pismeno = 0
plnost = 0
posledne_pismeno = ""

#precitanie riadkov suboru
suborik = subor.readlines()

#spocitanie riadkov
hry = len(suborik)

for riadok in suborik: #cyklus na prechadzanie riadkov v subore
    #zmena pomocnej premennej
    hra += 1

    #podmienka na zistenie hry s najvacsim poctom krokov
    if len(riadok) > max_kroky:
        max_kroky = len(riadok)

    for pismeno in riadok: #cyklus na prechadzanie pismen v riadku
        #podmienka na pripocitanie a vypisanie pismen
        if posledne_pismeno == pismeno:
            momentalne_pismeno += 1 

        elif posledne_pismeno != pismeno:  
            if not plnost == 0:
                #vypisanie do suboru
                subor1.write(posledne_pismeno+str(momentalne_pismeno+1))
                
            momentalne_pismeno = 0

        #zmena pomocnych premennych
        posledne_pismeno = pismeno
        plnost = 1

    #podmienka na presun do druheho riadku a zmeny premennej/vypisanie do suboru
    if not hra == hry:
        subor1.write("\n")
        plnost = 0
    else:
        subor1.write(posledne_pismeno+str(momentalne_pismeno+1))

#vypisanie pozadovanych hodnot
print("V súbore sú zapísané",hry,"hry.")
print("Najdlhšia hra mala",max_kroky,"krokov.")

#zatvorenie suborov
subor.close()
subor1.close()
