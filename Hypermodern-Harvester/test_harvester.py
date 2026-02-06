from url_generator import generate_swisschess_url

def test_url_generation():
    # Bekannte URL zum Abgleich
    expected = "https://www.swisschess.ch/sjmm.html?old=L3R1cm5pZXJlL3NqbW0ucGhwP2FqYWhyPTIwMjYmYXJvdW5kPTMmYWxpZ2E9Mg,,"
    result = generate_swisschess_url('sjmm', 2026, 2, runde=3)
    assert result == expected

def test_base64_padding():
    result = generate_swisschess_url('smm', 2025, 1)
    # Prüfen, ob das Padding korrekt durch Kommas ersetzt wurde
    assert "=" not in result
