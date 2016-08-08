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
 
Aufbau
Die Controllerklasse verwaltet (fast) alles: die Spielerin/den Spieler, das Monster, den Timer(oder der Timer wandert in die Controllerklasse?), Vokabeln und Vokabellisten, Frage+Antwort-Klassen.
Die Controllerklasse übernimmt das laden (und speichern?) von Daten.
Die Gui sollte mit der Controllerklassekommunizieren, aber nicht darin enthalten sein, um Abhängigkeiten zu vermeiden. 
Die Gui ist die Bottle-App, der Teil des Programms wo das Bottleframework eingesetzt wird. 
Die Daten für die Gui kommen von der Controllerklasse. Die Controllerklasse sendet der Gui Daten was angezeigt werden soll.

Das Monster (Tamagochi) ist eine eigene Klasse.
Die Monster hat Variablen:
  - Name = Name des Monsters
  - HP = Lebenspunkte
  - Hunger-Zähler
  - Status
  
Den Name kann die Spielerin ändern.
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

Voc-Klasse:
 - Begriff
 - Bedeutung
 - Hinweis-Feld
 - Bild
 - Sprache = zur welcher Sprache gehört die Vokabel
 - repetition_point = Wie häufig wurde die Vokabel schon richtig beantwortet. Die mit dem niedrigsten Wert wird dem Spieler vorgeschlagen. (Das ist ein einfache Version einen Wiederhohlungsmechanismus einzubauen.) 
Zweite Möglichkeit wäre: due_time = Wann soll die Vokabel abgefragt werden als zeit-stempel. Das timer-Object wird dann um die Aktuelle Zeit angefragt und wenn diese größer ist als der Zeitstempel, dann wir die Vokabel abgefragt.
Diese beiden Mechanismen kann man kombinieren und nur die Karten die Fällig sind nach repetition_point_anzahl sortiert anzeigen. 
(Oh, sortieren könnte schwierig werden. Klasse an Attributeingeschaft sortieren... )

VocListe:
Die Voc-Liste beinhaltet meherer Listen in die die Vokabelkarten sortiert/gruppiert werden können,
z.B. je nach repetition-point-anzahl. 

Timer-Klasse
misst die fortgeschrittene Zeit und löst Events aus.
Die Frage ist wie man nun die Gui automatisch per Bottle updatet. 
So sollte auch das Monster animiert werden. Oder man mal eine gif-animation.
 

