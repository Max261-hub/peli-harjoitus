#congif.py
#===============================================
#Pelin asetukset
#===============================================

#pelaajan mohdooliset valinnat (listasta)
valinta = ["Kivi", "Sakset", "Paperi"]

# voittosäännöt (sanakirja)
# Avain: voittava valinta
#Arvo: Listan valinnoista, jotka avain voitto

voitto_saannot = {
    "Kivi" : ["Sakset"],
    "Sakset" : ["Paperi"],
    "Paperi" : ["Kivi"]
    }

#=====================================================
#Tekstit
#=====================================================

tervehdys = "Tervetuloa pelamaan Kivi-Sakset-Paperi! kirjoittaa 'lopeta' lopetaaksesi pelin."
kehote = "Valitse Kivi, Sakset tai Paperi."
virhe_ilmoitus = "Virhellinen valinta! valitse Kivi, Sakset tai Paperi."