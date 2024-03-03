"""
creare una funzione che permetta di cercare una diretta parola all'interno di un documento
"""

def cerca_parola(parola, testo):
    return parola in testo #cerca una determinata parola all'interno di un testo

def leggi():
    percorso_del_file = input("inserisci il percorso del file: ") #inserire il percorso del file da leggere
    testo_dove_cercare = "" # settare una variabile vuota
    with open(percorso_del_file, 'r') as file: # apre il file in questione
        contenuto = file.read()  # Legge tutto il contenuto del file
        testo_dove_cercare = contenuto # setta la variabile con il contenuto del file

    parola_da_cercare = input("inserisci la parola che vuoi cercare: ") # inserire la parola da cercare

    risposta = cerca_parola(parola_da_cercare, testo_dove_cercare) # impostare il risultato della risposta

    if risposta: # se è True fa i complimenti
        print(f"complimenti la parola <{parola_da_cercare}> esiste all'interno del testo \n {testo_dove_cercare}")
    else: # altrimenti ti dice che non è presente
        print(f"La parola <{parola_da_cercare}> non è presente nel testo \n {testo_dove_cercare}")
        procedere = input("Vuoi riprovare? y/n: \n")
        if procedere == "y":
            leggi()
        else:
            print("Grazie per aver provato il servizio di ricerca")

leggi()
