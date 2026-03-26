def main():
    #f = open("szoveg.txt","r")
    
    #for line in f:
    #    line = line.rstrip("\n") szó végi sortörés levágása
    #   if line.endswith("."):
    #        print(line)
    
    
    #listában adja vissza
    #sorok = f.readlines()
    #print(sorok)
    
    #teljes file tartalma stringként
    #content = f.read()
    #print("'"+content+"'")
    
    #sortörés mentén vagdossa szét a file-t
    #sorok = f.read().splitlines()
    #print(sorok)
        
    #f.close()
    
    ###FILE-BA ÍRÁS
    #f = open("out.txt","w")
    
    #print("Hello",file=f)
    #print(True,3.14,file=f)
    #name = "Jani"
    #age = 30
    #print(f"{name} {age} éves.",file=f)
    #f.write("aa\n") #nem rak sortörést, nekünk kell oda írni
    #f.write("bb\n")
    
    #f.close() #Be kell zárni különösen írás esetén, de ha kivétel lép fel, akkor nem lesz bezárva a file
    
    
    #file tartalmának másolása a "régi" módszerrel
    
    #f1 = open("szoveg.txt","r")
    #to = open("output.txt","w")
    
    #for line in f1:
    #    to.write(line)
        
    #f1.close()
    #to.close()
    
    #érdemes használni másolásra: import shutil
                                    #shutil.copy(mit,hova)
                                    
    
    total = 0
    with open("szamok.txt","r") as f:
        for line in f:
            number = int(line.strip())
            total += number
    total_str = str(total)
    print("Az első tíz számjegy összege: ",total_str[:10])
    
    
    
###############################


if __name__ == "__main__":
    main()
