# stats.py

import json
import os
# Tuodaan tiedoston nimi config.py:stä
from config import STATS_FILE

class StatsManager:
    """
    Luokka, joka hallitsee pelin tilastoja ja niiden tallennusta JSON-tiedostoon.
    """
    
    def __init__(self):
        """
        Alustaa tilastot. Yrittää ladata vanhat tilastot tiedostosta.
        """
        self.file_path = STATS_FILE
        self.default_stats = {
            "pelatut_pelit": 0,
            "voitot": 0,
            "haviot": 0,
            "tasapelit": 0
        }
        
        # 1. Lataa tilastot
        self.stats = self._load_stats()

    def _load_stats(self):
        """
        Lataa tilastot JSON-tiedostosta. Jos tiedostoa ei ole, palauttaa oletustilastot.
        
        KÄYTÄMME OS JA TRY/EXCEPT -RAKENTEITA
        """
        if os.path.exists(self.file_path):
            try:
                # 'with open' on paras tapa avata tiedostoja
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    # json.load() lukee tiedoston sisällön ja muuttaa sen Python-sanakiirjaksi
                    data = json.load(f)
                    print(f"✅ Tilastot ladattu tiedostosta: {self.file_path}")
                    return data
            except json.JSONDecodeError:
                # Virhe, jos tiedosto on rikki (ei kelvollista JSON-muotoa)
                print(f"❌ Virheellinen JSON-muoto tiedostossa. Aloitetaan uusilla tilastoilla.")
                return self.default_stats.copy()
            except Exception as e:
                print(f"❌ Odottamaton virhe ladattaessa tilastoja: {e}")
                return self.default_stats.copy()
        else:
            # Jos tiedostoa ei ole olemassa
            print(f"ℹ️ Tilastotiedostoa ({self.file_path}) ei löytynyt. Luodaan uusi.")
            return self.default_stats.copy()

    def save_stats(self):
        """
        Tallentaa nykyiset tilastot JSON-tiedostoon.
        
        KÄYTÄMME JSON.DUMP -FUNKTIOTA
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                # json.dump() kirjoittaa Python-sanakiirjan tiedostoon JSON-muodossa
                # indent=4 tekee tiedostosta siistin ja luettavan
                json.dump(self.stats, f, indent=4) 
                print(f"✅ Tilastot tallennettu onnistuneesti.")
        except Exception as e:
            print(f"❌ Virhe tallennettaessa tilastoja: {e}")

    def update_stats(self, result):
        result = result.lower()
        """
        Päivittää tilastoja pelin tuloksen perusteella.
        
        KÄYTÄMME SANAKIRJOJA
        """
        self.stats["pelatut_pelit"] += 1
        
        if result == "voitto":
            self.stats["voitot"] += 1
        elif result == "häviö":
            self.stats["haviot"] += 1
        elif result == "tasapeli":
            self.stats["tasapelit"] += 1
        
        # TÄRKEÄÄ: Aina kun tilastot muuttuvat, ne pitää tallentaa!
        self.save_stats()
        
    def get_stats_teksti(self):
        """
        Palauttaa tilastot tulostettavassa muodossa.
        """
        total = self.stats["pelatut_pelit"]
        if total == 0:
            return "Ei pelattuja pelejä."
            
        win_percent = (self.stats["voitot"] / total) * 100
        
        # KÄYTÄMME F-STRINGEJA MUOTOILUUN
        return (f"📊 Tilastot:\n"
                f"  Pelatut pelit: {total}\n"
                f"  Voitot: {self.stats['voitot']} ({win_percent:.1f}%)\n"
                f"  Häviöt: {self.stats['haviot']}\n"
                f"  Tasapelit: {self.stats['tasapelit']}\n")

# ============================================
# TESTAUS
# ============================================

if __name__ == "__main__":
    manager = StatsManager()
    print("\nNykyiset tilastot ennen peliä:")
    print(manager.get_stats_teksti())
    
    # Simulaatio: 1 voitto, 1 häviö, 1 tasapeli
    manager.update_stats("voitto")
    manager.update_stats("häviö")
    manager.update_stats("tasapeli")
    
    print("\nTilastot kolmen pelin jälkeen:")
    print(manager.get_stats_teksti())