from url_generator import generate_swisschess_url

def run_harvester_iteration():
    # Hier definieren Sie die Parameter für die Suche
    jahre = [2025, 2026]
    # ... Rest der Iterations-Logik ...
    
    for jahr in jahre:
        url = generate_swisschess_url('sjmm', jahr, 2, runde=3)
        print(f"Erstellte URL: {url}")

if __name__ == "__main__":
    run_harvester_iteration()
