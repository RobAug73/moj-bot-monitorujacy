import requests
from bs4 import BeautifulSoup
import os

# KONFIGURACJA
URL = "https://www.gov.pl/web/funduszmodernizacyjny/aktualnosci2"
MOJ_EMAIL = "R.AUGUSTYN88@GMAIL.COM"  # <--- WPISZ SWÓJ ADRES TUTAJ
RESEND_API_KEY = os.getenv("RESEND_API_KEY")

def wyslij_maila(tytul):
    resend_url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "from": "onboarding@resend.dev",
        "to": MOJ_EMAIL,
        "subject": "Nowa aktualizacja: Fundusz Modernizacyjny",
        "html": f"<h3>Znaleziono nową informację:</h3><p>{tytul}</p><br><a href='{URL}'>Przejdź do strony</a>"
    }
    r = requests.post(resend_url, headers=headers, json=data)
    if r.status_code == 200:
        print("E-mail został wysłany!")
    else:
        print(f"Błąd wysyłki: {r.text}")

def sprawdz_nowosci():
    print("Łączenie ze stroną gov.pl...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    pierwszy_news = soup.find('div', class_='art-prev')
    
    if pierwszy_news:
        tytul = pierwszy_news.find('div', class_='title').get_text().strip()
        print(f"Najnowszy news: {tytul}")
        wyslij_maila(tytul)
    else:
        print("Nie znaleziono nowości.")

if __name__ == "__main__":
    sprawdz_nowosci()
