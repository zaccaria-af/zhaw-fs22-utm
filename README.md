# zhaw-fs22-utm

## Übung 4 - Turing-Maschinen

### Aufgabe 1. Universelle TM.
Entwickeln Sie (in einer beliebigen Programmiersprache) ein Programm, das eine Universelle
TM emuliert. Das Programm soll die kodierte Funktion einer TM (konkret für die Multiplikation
von zwei natürlichen Zahlen) und eine Eingabe dazu einlesen und verarbeiten. Als Kodierung
verwenden Sie am besten die in der Vorlesung eingeführte Codierung über eine Binärzeichenreihe.

Als Ausgabe (Bildschirm) wird folgendes erwartet:

- a) das korrekte Ergebnis,
- b) die Angabe des aktuellen Zustandes der TM,
- c) das Band mit mindestens 15 Elementen vor und nach dem Lese-/Schreibkopf,
- d) die aktuelle Position des Lese-/Schreibkopfes und
- e) ein Zähler, der die Anzahl der bisher durchgeführten Berechnungsschritte angibt.
  
Es sind zwei Modi zu realisieren:

- ein Step-Modus: Ausgabe (b bis e) nach jedem einzelnen Berechnungsschritt
- ein Laufmodus: einmalige Ausgabe nach Abschluss der ganzen Berechnung (Also alle Berechnungsschritte ohne Halt /
  Ausgabe nach Halt der Turing-Maschine durchführen.)
