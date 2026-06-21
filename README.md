# Laboratorium BI - Raport (Metabase & PostgreSQL)

## 1. Środowisko i uruchomienie
Do uruchomienia projektu użyto narzędzia **Docker Compose** z następującymi obrazami:
*   `postgres:16` (baza danych / hurtownia analityczna na porcie 5432)
*   `metabase/metabase:latest` (narzędzie BI na porcie 3000)


## 2. Ładowanie danych
Dane transakcyjne (200 rekordów, maj-czerwiec 2026) zostały wygenerowane i załadowane za pomocą skryptu w Pythonie wykorzystującego biblioteki `pandas` i `sqlalchemy` (`engine.connect()` + `df.to_sql`). 
Struktura tabeli `transactions`: `event_time`, `user_id`, `category`, `amount`, `status`.

## 3. Pytania i wizualizacje (Questions)
1.  **Struktura zamówień (Wykres kołowy):** Stworzony w kreatorze. Wybór wykresu kołowego uzasadnia mała liczba unikalnych statusów, co pozwala szybko ocenić procentowy udział np. transakcji anulowanych do opłaconych.
2.  **Sprzedaż per kategoria (Wykres słupkowy):** Agregacja (Suma i Liczba) per kategoria. Wykres słupkowy idealnie nadaje się do porównywania niezależnych od siebie grup produktów.
3.  **Trend przychodów w czasie (Wykres liniowy - SQL):** Zapytanie grupujące sumę `amount` po dniach dla statusu 'paid'. Wykres liniowy najlepiej pokazuje dynamikę i trendy (wzrosty/spadki) w czasie.

## 4. Dashboard i KPI
Utworzono **Panel Sprzedaży** zawierający:
*   **Wykresy:** Trzy przygotowane wcześniej pytania analityczne.


## 5. Wnioski i Teoria

*   **Przetwarzanie danych vs BI:** Przetwarzanie (np. Spark/Python) to czyszczenie i przygotowanie surowych danych na zapleczu. Warstwa BI (Metabase) to wizualna nakładka dla biznesu – nie przetwarza danych od zera, tylko czytelnie prezentuje to, co jest już w bazie.
*   **Dashboard vs Raport statyczny:** Dashboard działa "na żywo", aktualizuje się sam i jest interaktywny (można klikać filtry). Raport statyczny (np. PDF) to niezmienny dokument pokazujący "zamrożony" stan danych z przeszłości.
*   **Zapytanie ad-hoc vs KPI:** Zapytanie ad-hoc to jednorazowe, szybkie pytanie do bazy zadane przez analityka, by sprawdzić coś konkretnego. KPI to stały, kluczowy wskaźnik kondycji firmy (np. całkowity przychód), który mierzy się stale w ten sam sposób.