# main.py

import sys
# Tuodaan kaikki vakiot config.py tiedostosta
from config import valinta, Teksti_tervehdy, Teksti_kehote, Teksti_virhe_ilmoitus
# Tuodaan logiikka game_logic.py tiedostosta
from game_logic import get_tietokone_valinta, determine_voittaja

def main():
    """
    Pelin pääfunktio, joka sisältää pelin käynnissä pitävän silmukan.
    """
    # 5. LISÄTÄÄN PISTEIDEN LASKEJAT (Tehtävä #5)
    pelaaja_voitto = 0
    tietokone_voitto = 0
    tasa = 0
    
    print("=" * 30)
    print(Teksti_tervehdy)
    print("=" * 30)
    
    # KÄYTETÄÄN WHILE SILMUKKAA
    # while True pitää pelin käynnissä, kunnes käyttäjä kirjoittaa 'lopeta'
    while True:
        # Näytetään nykyiset pisteet ennen kierrosta
        print(f"\n🏆 Pisteet: Pelaaja {pelaaja_voitto} - Tietokone {tietokone_voitto} - Tasapelit {tasa}")
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
            continue # Jatka seuraavaan silmukan kierrokseen (hyppää takaisin alkuun)
            
        # 4. Tietokoneen valinta
        tietokone_valinta = get_tietokone_valinta()
        
        print(f"Sinun valintasi: {pelaajan_valinta}")
        print(f"Tietokoneen valinta: {tietokone_valinta}")
        
        # 5. Määritys ja tuloksen tulostus
        tulos = determine_voittaja(pelaajan_valinta, tietokone_valinta)
        
        # 6. Päivitä pisteet ja ilmoita tulos (Tehtävä #5)
        if tulos == "Voitto":
            print("🎉 Voitit kierroksen!")
            pelaaja_voitto += 1 # KÄYTETÄÄN MUUTTUJIA
        elif tulos == "Häviö":
            print("🙁 Hävisit kierroksen.")
            tietokone_voitto += 1 # KÄYTETÄÄN MUUTTUJIA
        else: # tasapeli
            print("🤝 Tasapeli!")
            tasa += 1 # KÄYTETÄÄN MUUTTUJIA
            
    # Silmukan loputtua tulostetaan yhteenveto
    print("\n" + "=" * 30)
    print("PELI PÄÄTTYI")
    print(f"Lopulliset pisteet: Pelaaja {pelaaja_voitto} - Tietokone {tietokone_voitto}")
    print("=" * 30)
    
if __name__ == "__main__":
    main()