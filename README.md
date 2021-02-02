# Induction program - python feladat

## Specifikacio

GPS alapu turautvonal-tervezo programot keszitunk. A program adatbazisaban latvanyossagok vannak eltarolva.
A latvanyossagok mindegyikenek x es y koordinataja van, amelyek -10 es 10 kozottiek lehetnek (ez a jelenlegi pozicionkhoz viszonyitott, km-ben mert helyuket jelzi),
es van 0-1000 kozotti tengerszint feletti magassaguk is.
Ha a programnak megadunk egy pontot, ahonnan indulni akarunk (-10, 10 kozotti koordinatakkal), akkor visszaad egy utvonaljavaslatot, amely az adott kiinduloponthoz
5 km-nel kozelebb levo latvanyossagokat tartalmazza. Egy utvonaljavaslatot reprezentaljunk Utvonal osztallyal.
Az osszes, a program altal ismert latvanyossag egy tombben helyezkedik el, amelyet ugy hozzunk letre, hogy 50-100 db veletlenszeru latvanyossagot
tartalmazzon. Az Utvonalba ezek kozul vesszuk bele a kozel levoket.
Az Utvonal osztaly tartalmazza a kovetkezo funkciokat:

- Tavolsag(), amely visszaadja a teljes ut legvonalban vett hosszat (a magassaggal nem kell szamolni).
- Szintemelkedes(), amely visszaadja a szintemelkedest (a legmasabb es a legmelyebb pont kozotti kulonbseget).
- Szures(x), amely egy uj Utvonalat keszit az aktualis utvonal alapjan, de ugy, hogy az uj Utvonalban nem szerepelnek az aktualis utvonal x-nel magasabb pontjai.
- Ket utvonalat lehessen osszekapcsolni is, azaz eloallitani beloluk egy olyan uj Utvonalat, amely mindket utvonal pontjait tartalmazza, de ugy, hogy egy pontot
  sem tartalmazhat tobbszor.
