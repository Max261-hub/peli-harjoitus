# game_logic.py

import random
from config import valinta, voitto_saannot

def get_tietokone_valinta():
    
    
    tietokone_valinta = random.choice(valinta)
    return tietokone_valinta



def determine_voittaja(pelaajan_valinta, tietokone_valinta):
    
    
    #1. TASAPELI?
    #KÄYTÄ EHTOLAUSETTA
    
    if pelaajan_valinta == tietokone_valinta:
        return "Tasapeli"
    
    #2. VOITTO
    # Tarkista onko pelaaja valinta (pelaajan_valinta) sanakirjan avain voitto_saannot
    #Sitten tarkista, voittaako se tietokoneen valinnan (tietokone_valinta).
    # Käytä sanakirjaa ja lista
    
    if tietokone_valinta in voitto_saannot.get(pelaajan_valinta, []):
        return "Voitto"
    
    # 3. HÄviö
    # jos ei ollu tasapeli eikä voitto, sen on oltava häviö
    else:
        return "Häviö"
        
if __name__=="__main__":
    
    print("\n Testataan voittajan määritystä.....")
    
    #Pelaaja voittaa
    print(f"Kivi vs Sakset: {determine_voittaja('Kivi', 'Sakset')}") #Odotettu: voitti
    
    # Tasapeli
    print(f"Paperi vs Paperi: {determine_voittaja('Paperi', 'Paperi')}") # Odotettu: Tasapeli
    
    #Pelaaja häviö
    print(f"Sakset va Kivi: {determine_voittaja('Sakset', 'Kivi')}") #Odotettu: Häviö
    