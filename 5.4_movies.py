class Movies:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        self.liczba_odtworzen=liczba_odtworzen
    def __str__(self):
        return f"{self.tytul} ({self.rok_wydania})"
    def play(self, step=1):
        self.liczba_odtworzen += step

M001 = Movies(tytul="Diuna", rok_wydania="2021", gatunek="Sci-Fi", liczba_odtworzen=200000)

class Series(Movies):
    def __init__(self, numer_odcinka, numer_sezonu, *args,  **kwargs):
        super().__init__(*args,  **kwargs)
        self.numer_odcinka=numer_odcinka
        self.numer_sezonu=numer_sezonu
    def __str__(self):
        return f"{self.tytul} S{self.numer_sezonu}E{self.numer_odcinka}"

S001 = Series(tytul="Dark", rok_wydania="2017", gatunek="Sci_Fi", numer_odcinka="01", numer_sezonu="01", liczba_odtworzen=500000)

lista = []

lista.append(M001)
lista.append(S001)

for x in lista:
    print(x)

