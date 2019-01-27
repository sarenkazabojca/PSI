class Wypozyczenie:
    def zwroc(self, termin_zwr):
        self.termin_zwr = termin_zwr
        self.egzemplarz.wypozyczenie = None

    def __init__(self, egzemplarz, klient, pracownik, termin_wyp):
        self.egzemplarz = egzemplarz
        self.klient = klient
        self.pracownik = pracownik
        self.termin_wyp = termin_wyp
        self.termin_zwr = None
        egzemplarz.wypozyczenie = self


class Rezerwacja:
    def wypozycz(self, termin_wyp):
        if self.egzemplarz.wypozyczenie is None:
            self.wypozyczenie = Wypozyczenie(self.egzemplarz, self.klient, self.pracownik, termin_wyp)
            return self.wypozyczenie
        else:
            print("Błąd: Egzemplarz aktuanie wypożyczony.")

    def __init__(self, egzemplarz, klient, pracownik, termin_rez):
        self.egzemplarz = egzemplarz
        self.klient = klient
        self.pracownik = pracownik
        self.termin_rez = termin_rez
        self.wypozyczenie = None


class Egzemplarz:
    def wypozycz(self, klient, pracownik, termin_wyp):
        if self.wypozyczenie is None:
            return Wypozyczenie(self, klient, pracownik, termin_wyp)
        else:
            print("Błąd: Egzemplarz aktuanie wypożyczony.")

    def __init__(self, tytul, id_egzemparza, kod_kreskowy, typ, miejsce_przechowywania, ograniczenie_wypozyczenia):
        self.tytul = tytul
        self.id_egzemplarza = id_egzemparza
        self.kod_kreskowy = kod_kreskowy
        self.typ = typ
        self.miejsce_przechowywania = miejsce_przechowywania
        self.ograniczenie_wypozyczenia = ograniczenie_wypozyczenia
        self.wypozyczenie = None


class Tytul:
    def __init__(self, aktor, autor, tytul, wydawnictwo, isbn):
        self.aktor = aktor
        self.autor = autor
        self.tytul = tytul
        self.wydawnictwo = wydawnictwo
        self.isbn = isbn


class Autor:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Aktor:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Klient:
    def __init__(self, imie, nazwisko, pesel, id_klienta):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.id_klienta = id_klienta


class Pracownik:
    def __init__(self, imie, nazwisko, id_pracownika):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id_pracownika = id_pracownika
