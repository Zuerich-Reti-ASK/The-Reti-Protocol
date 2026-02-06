import datetime
import requests
import time
from url_generator import generate_swisschess_url

def check_url_validity(url):
    """
    Prüft, ob die Zielseite Daten enthält oder einen validen Fehler liefert.
    """
    try:
        response = requests.get(url, timeout=10)
        # Ein 404 oder ein Redirect auf die Startseite signalisiert oft das Fehlen der Daten
        if response.status_code != 200:
            return False, f"HTTP {response.status_code}"
        
        # Prüfung auf spezifische Textbausteine, wenn keine Daten vorhanden sind
        if "Keine Daten gefunden" in response.text or "unbekanntes Turnier" in response.text:
            return False, "Leere Datenmenge"
            
        return True, "Success"
    except Exception as e:
        return False, str(e)

def run_deep_harvest():
    # Dynamische Zeitrechnung
    start_jahr = 2000
    aktuelles_jahr = datetime.date.today().year
    end_jahr = aktuelles_jahr + 1  # Inklusive Planung für die nächste Saison
    
    turnier_meta = {
        "smm": {"ligen": range(1, 5), "max_runden": 9},
        "sgm": {"ligen": range(1, 4), "max_runden": 7},
        "sjmm": {"ligen": range(1, 3), "max_runden": 5}
    }

    for jahr in range(start_jahr, end_jahr + 1):
        for t_type, config in turnier_meta.items():
            for liga in config["ligen"]:
                # Hinweis: agruppe muss dynamisch aus dem Rulebook kommen
                # Für den Test nutzen wir hier eine Standard-Iteration
                url = generate_swisschess_url(t_type, jahr, liga, runde=1)
                
                valid, message = check_url_validity(url)
                
                if not valid:
                    # Dies sind die "berechtigten Fehler" (z.B. SJMM im Jahr 2002 existiert nicht)
                    print(f"[-] Skip: {t_type.upper()} {jahr} | Grund: {message}")
                    continue
                
                print(f"[+] Data found: {t_type.upper()} {jahr} Liga {liga} -> URL valid.")
                # Hier folgt der Aufruf des eigentlichen Scraping-Prozesses
                
                # Höflichkeits-Pause zur Vermeidung von IP-Sperren
                time.sleep(0.5)

if __name__ == "__main__":
    run_deep_harvest()
