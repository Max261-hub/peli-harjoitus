# main.py

import sys
# Tuodaan kaikki vakiot config.py tiedostosta
from config import valinta, Teksti_tervehdy, Teksti_kehote, Teksti_virhe_ilmoitus
# Tuodaan logiikka game_logic.py tiedostosta
from game_logic import get_tietokone_valinta, determine_voittaja
# Tuo uusi luokka
from stats import StatsManager # Lisätty

def main():
    # Pelin pääfunktio, joka sisältää pelin käynnissä pitävän silmukan.
    
    # aloitetaan tilastojen hallinta
    stats_manager = StatsManager() # Lisätty
    
    # Vanhat pisteiden alustukst poistetiin tästä, StatsManager hoittaa ne
    
    print("=" * 30)
    print(Teksti_tervehdy)
    print("=" * 30)
    
    # KÄYTETÄÄN WHILE SILMUKKAA
    # while True pitää pelin käynnissä, kunnes käyttäjä kirjoittaa 'lopeta'
    while True:
        # Näytetään nykyiset pisteet ennen kierrosta
        print(stats_manager.get_stats_teksti().strip()) # Lisätty (strip() siistii rivinvaihtoja)
        print("-" * 30)
        
        # 1. Käyttäjän valinta
        # KÄYTETÄÄN INPUT FUNKTIOTA
        syote = input(Teksti_kehote).strip().lower()

        if syote == "lopeta":
            break # Poistutaan while-silmukasta
        
        # 2. Muutetaan syöte oikeaan muotoon
        # Sanakirja jolla muutetaan syötteet (k, s, p) oikeiksi nimiksi (Kivi, Sakset, Paperi)
        mapping = {'k': 'Kivi', 's': 'Sakset', 'p': 'Paperi', 'kivi': 'Kivi', 'sakset': 'Sakset', 'paperi': 'Paperi'}
        pelaajan_valinta = mapping.get(syote, None)
        
        # 3. Virheellisen syötteen tarkistus
        # KÄYTETÄÄN LISTOJA JA EHTOLAUSEITA
        if pelaajan_valinta not in valinta:
            print(Teksti_virhe_ilmoitus)
            continue # Jatka seuraavaan silmukan kierrokseen (hyppää 
        tietokone_valinta = get_tietokone_valinta()
        
        print(f"Sinun valintasi: {pelaajan_valinta}")
        print(f"Tietokoneen valinta: {tietokone_valinta}")
        
        # 5. Määritys ja tuloksen tulostus
        tulos = determine_voittaja(pelaajan_valinta, tietokone_valinta)
        
        # 6. Päivitä pisteet ja ilmoita tulos (Tehtävä #5)
        if tulos == "Voitto":
            print("🎉 Voitit kierroksen!")
        elif tulos == "Häviö":
            print("🙁 Hävisit kierroksen.")
        else: # tasapeli
            print("🤝 Tasapeli!")
            
        # Päivittä tilastot json- tiedostoon
        stats_manager.update_stats(tulos) # Lisätty
            
    # Silmukan loputtua tulostetaan yhteenveto
    print("\n" + "=" * 30)
    print("PELI PÄÄTTYI")
    # Lopulliset tilastot
    print(stats_manager.get_stats_teksti()) # Lisätty
    print("=" * 30)
    
if __name__ == "__main__":
    main()