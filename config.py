# config.py

# ============================================
# PELIN ASETUKSET
# ============================================

# Pelaajan mahdolliset valinnat (Lista)
valinta = ["Kivi", "Sakset", "Paperi"]

# Voittosäännöt (Sanakirja)
# Avain: Voittava valinta
# Arvo: Lista valinnoista, jotka avain voittaa
voitto_saannot = {
    "Kivi": ["Sakset"],
    "Sakset": ["Paperi"],
    "Paperi": ["Kivi"]
}


# ============================================
# TEKSTIT
# ============================================

Teksti_tervehdy = "Tervetuloa pelaamaan Kivi-Sakset-Paperia! Kirjoita 'lopeta' lopettaaksesi pelin."
Teksti_kehote = "Valitse Kivi, Sakset tai Paperi: "
Teksti_virhe_ilmoitus = "Virheellinen valinta! Valitse Kivi, Sakset tai Paperi."


#===============================================
# Tilasto Asetukset
#===============================================

#Tilastotiedoston nimi
STATS_FILE = "konsoli_tilastot.json"