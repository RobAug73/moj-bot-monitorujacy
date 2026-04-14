import requests
from bs4 import BeautifulSoup

# Adres strony do monitorowania
URL = "https://www.gov.pl/web/funduszmodernizacyjny/aktualnosci2"

def sprawdz_nowosci():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Szukamy pierwszego nagłówka aktualności
    # Na gov.pl newsy są zazwyczaj w listach z konkretną klasą
    pierwszy_news = soup.find('div', class_='art-prev')
    
    if pierwszy_news:
        tytul = pierwszy_news.get_text().strip()
        print(f"Najnowszy news to: {tytul}")
        # Tutaj w przyszłości dodamy kod wysyłający e-mail
    else:
        print("Nie znaleziono aktualności - sprawdź strukturę strony.")

if __name__ == "__main__":
    sprawdz_nowosci()
