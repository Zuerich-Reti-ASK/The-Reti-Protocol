# import base64

# def generate_swisschess_url(turnier_type, jahr, liga, gruppe=None, runde=None):
#     """
#     Generiert die kodierte URL für SMM, SGM oder SJMM.
    
#     :param turnier_type: 'smm', 'sgm' oder 'sjmm'
#     :param jahr: Jahr (z.B. 2025)
#     :param liga: Liga-Nummer
#     :param gruppe: Gruppen-ID (optional)
#     :param runde: Runden-Nummer (optional)
#     """
    
#     # 1. Pfad-Konstruktion
#     # Die Reihenfolge der Parameter ist oft entscheidend für die Server-Akzeptanz
#     path = f"/turniere/{turnier_type}.php?ajahr={jahr}"
    
#     if runde:
#         path += f"&around={runde}"
#     if gruppe:
#         path += f"&agruppe={gruppe}"
#     if liga:
#         path += f"&aliga={liga}"

#     # 2. Base64 Kodierung
#     # Wir kodieren den String in Bytes und dann in Base64
#     encoded_bytes = base64.b64encode(path.encode('utf-8'))
#     encoded_string = encoded_bytes.decode('utf-8')

#     # 3. Padding-Korrektur (Swisschess-Spezialität)
#     # Die Webseite nutzt oft Kommas (,,) statt Gleichheitszeichen (==)
#     encoded_string = encoded_string.replace('=', ',')

#     # 4. Finaler URL-Zusammenbau
#     wrapper = f"https://www.swisschess.ch/{turnier_type}.html?old={encoded_string}"
    
#     return wrapper

# # --- TEST-BEREICH ---
# if __name__ == "__main__":
#     # Test SJMM (dein Beispiel)
#     print(f"SJMM Test: {generate_swisschess_url('sjmm', 2026, 2, runde=3)}")
    
#     # Test SGM (Bundesliga)
#     print(f"SGM Test:  {generate_swisschess_url('sgm', 2025, 1, gruppe=101, runde=2)}")


from url_generator import generate_swisschess_url
import time

def dry_run_iteration():
    """
    Simuliert den Erfassungszyklus ohne Netzwerkzugriff.
    Prüft die Parameter-Logik für Jahre > 1999.
    """
    start_jahr = 2000
    end_jahr = 2026
    
    # Konfiguration der Turnierstrukturen
    turnier_meta = {
        "smm": {"ligen": [1, 2, 3], "runden": [1, 9]},  # Testet Start und Ende
        "sgm": {"ligen": [1, 2], "runden": [1, 7]},
        "sjmm": {"ligen": [1], "runden": [1, 5]}
    }

    print(f"{'Turnier':<8} | {'Jahr':<6} | {'Liga':<5} | {'Runde':<6} | {'Generierte URL'}")
    print("-" * 100)

    count = 0
    for jahr in range(start_jahr, end_jahr + 1):
        for t_type, config in turnier_meta.items():
            for liga in config["ligen"]:
                for runde in config["runden"]:
                    # Generierung der URL
                    url = generate_swisschess_url(t_type, jahr, liga, runde=runde)
                    
                    # Ausgabe zur visuellen Kontrolle
                    print(f"{t_type.upper():<8} | {jahr:<6} | {liga:<5} | {runde:<6} | {url}")
                    
                    count += 1
                    
                    # Begrenzung für den ersten Testlauf (optional)
                    if count > 50:
                        print("\n... Weitere 10.000+ Kombinationen folgen im Vollbetrieb.")
                        return

if __name__ == "__main__":
    dry_run_iteration()
