import matplotlib.pyplot as plt
import random
from resistancevirus import ResistantVirus   
from Patient import Patient

def part5():
    maxPop = 1000
    time = []
    pop = []
    viruses = []
    resistances = {'guttagonol':False}
    for i in range (0,100):
        a = ResistantVirus(.1,0.5,resistances,0.005)
        viruses.append(a)
    aPatient1 = Patient(viruses, maxPop)
    aPatient2 = aPatient1
    aPatient3 = aPatient1
    aPatient4 = aPatient1	
    for i in range (0,451):
        if i == (300):
            aPatient1.addPrescription('guttagonol')
            
        pop.append(aPatient1.update())
        time.append(i)
    print pop
    pop = []
    time = []	

    for i in range (0,301):
        if i == (150):
            aPatient2.addPrescription('guttagonol')
            
        pop.append(aPatient2.update())
        time.append(i)	
    print pop 
    pop = []	
    time = []

    for i in range (0,226):
        if i == (75):
            aPatient3.addPrescription('guttagonol')
            
        pop.append(aPatient3.update())
        time.append(i)
    print pop
    pop = []
    time = []

    for i in range (0,151):
        if i == (0):
            aPatient4.addPrescription('guttagonol')
            
        pop.append(aPatient4.update())
        time.append(i)
    print pop
    pop = []
    time = []

if __name__ == '__main__':
    part5()
