"""
creare una funzione che permetta di cercare una diretta parola all'interno di un documento
"""

def cerca_parola(parola, testo):
    return parola in testo

testo_dove_cercare = "C'era una volta un developer che voleva diventare programmatore python"
parola_da_cercare = input("inserisci la parola che vuoi cercare: ")

risposta = cerca_parola(parola_da_cercare, testo_dove_cercare)

if risposta:
    print(f"complimenti la parola <{parola_da_cercare}> esiste all'interno del testo \n <{testo_dove_cercare}>")
else:
    print(f"La parola <{parola_da_cercare}> non è presente nel testo \n <{testo_dove_cercare}>")
