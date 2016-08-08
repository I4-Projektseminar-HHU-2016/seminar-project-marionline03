Projekt-Plan:

TODO: Bis Donnerstag fertig machen

  * Bilder/Skizzen
  * Womit realisieren? Bottle 
  --> Problem: Bei Seitenneuladen Daten weg, d.h. Daten irgendwo speichern (man will ja sowieso eine Speicherfunktion haben)
  * Ziel: ein schönes kleines Projekt zum laufen bekommen 
  * Optional: Responsive Design
  * Zeitplan
  * Vokabeln schon vorgeben erstmal nur 3 später 10

 
Klassen + Variablen
technisch konkret
Idee, allgemein
 
-> Klassenaufbau

Das Monster (Tamagochi) ist eine eigene Klasse.
Die Monster hat Variablen:
  - Name = Name des Monsters
  - HP = Lebenspunkte
  - Hunger-Zähler
  - Status
  
Den Name kann der Spieler ändern.
Die HP (Health Points/Lebenspunkte) bei 0 ist das Monster tot.
Der Hungerzähler wird herunter gezählt, 
Status, gibt an in welchem Zustand das Monster ist. Es kann für den Anfang entweder normal oder hungrig sein.
(Stati sollten nachher einfach eingefügt werden, damit das Monster erweiterbar ist.)
Dazu gibt es Status-Klassen, diese enthalten Informationen darüber wie der Status angezeigt wird
und was für Auswirkungen er auf das Monster hat. das Monster hat eine set-status-Funktion, 
mit der die Attribute (z.b. ein anderes Bild) des Monsters an den Status angepasst werden. 

Die Monster- Klasse benötigt folgende Funktionen:
    - Export der eigenen Daten (zum Speichern)
    - set-status: Verändern der eigenen Daten (Status, Hunger-Variable)
    - reduce(Wert, amount): setzt 

Die Playerklasse benötigt:
    - Namen
    - VocPet
    - VocListe
    -

Voc-Klasse:
Begriff
Bedeutung
Hinweis-Feld
