# finner gjennsomsnitt av en liste med tall
liste = [2,5,67,3,2,6,89,23]

def gjennomsnitt():
    antall = len(liste)
    total = sum(liste)
    gjennomsnitt = total/antall
    return gjennomsnitt
result = gjennomsnitt()
print(result)    
    