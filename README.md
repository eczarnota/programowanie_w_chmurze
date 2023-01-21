# programowanie_w_chmurze
Program wyświetlający wykres równania funckji kwadratowej na podstawie parametrów pobranych z adresu URL, przykład:
http://localhost:5000/?a=-3&b=1&c=6&xmin=-5&xmax=5&ymin=-1&ymax=10
gdzie:
- a, b, c: parametry równania kwadratowego 
- xmin, xmax, ymin, ymax: graniczne wartości obszaru wykresu 

Przydatne komendy:

Tworzenie obrazu:
- docker build -t funkcja_kwadratowa_app:v1.0 .  

Uruchamianie kontenera:
- docker run --rm -it -p 5000:5000 funkcja_kwadratowa_app:v1.0 

Usuwanie obrazu:
- docker image rm funkcja_kwadratowa_app:v1.0 
