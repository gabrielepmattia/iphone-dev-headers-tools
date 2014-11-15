import os
import re


def main() :
    path = input('Write the base dir of your files\n- without " "\n- with double "\\\\" also at the end\n--> EXAMPLE: D:\\\\INCLUDE\\\\: ')
    
    # root = "D:/INCLUDE/"
    # path = "D:\\INCLUDE\\" #!!!!
    root = path.replace("\\\\", "/")

    print("PATH:", path)
    print("ROOT:", root)

    return None
    count = 0
    
    print("Genero l'elenco dei file con directory...")
    elencoFile = generaElencoFile(path)

    print("Inizio programma.")
    # Inizio il ciclo per ogni file presente
    for file in elencoFile :
        count += 1
        
        print(count, "#### FILE")

        print("=== Apro il file:", end = "")
        contenuto = apriFile(file)
        print(" ", file)

        print("=== Cerco le occorenze da sostituire")
        occorrenzeDaSostituire = re.finditer('#import "([a-zA-z]*).h"', contenuto)

        for occorrenza in occorrenzeDaSostituire :
            nomeDelFile = occorrenza.group(1) + ".h"
            
            nuovaDir = cercaFile(nomeDelFile, elencoFile)
            if nuovaDir != "":                
                nuovaDir = nuovaDir.replace("\\", "/")
                nuovaDir = nuovaDir.replace(root, "")

                daSostituire = '#import "' + nomeDelFile + '"'
                sostituente  = "#import <" + nuovaDir + ">"
                
                contenuto = contenuto.replace(daSostituire, sostituente)

                print("==== Sostituisco:", daSostituire, "con" ,sostituente)

        #Scrivo il file
        print("=== Scrivo il file\n")
        scriviFile(file, contenuto)
        
     
def generaElencoFile(path) :
    listaFile = []
    
    for root, dirs, files in os.walk(path) :
        for i in files :
            listaFile.append(root + "\\" +i)

    return listaFile

def cercaFile(nome, listaFile) :
    "Cerca un file con una parola chiave nell'elenco file e ritorna dir + nome"
    n = 0
    for file in listaFile :
        if file.find(nome) > 0 :
            return listaFile[n]
        
        n += 1
        
    return ""

   
def apriFile(nomefilecondirectory) :
    ultimoSlash = nomefilecondirectory.rfind("\\")

    dirFile  = nomefilecondirectory[:ultimoSlash +1]
    nomeFile = nomefilecondirectory[ultimoSlash +1:]
    
    os.chdir(dirFile)
    
    in_file = open(nomeFile,"r")
    text = in_file.read()
    in_file.close()
    
    return text

def scriviFile(nomefile, testo) :

    ultimoSlash = nomefile.rfind("\\")

    dirFile  = nomefile[:ultimoSlash +1]
    nomeFile = nomefile[ultimoSlash +1:]
    
    os.chdir(dirFile)

    
    # Svuoto il file
    open(nomeFile, 'w').close()

    out_file = open(nomeFile,"w")
    out_file.write(testo)
    out_file.close()

main()

input("\n\nDone. Press a button to exit..")
