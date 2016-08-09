#Projekt-Plan

##TODO 
FERTIG SCHREIBEN

##Inhalt 
* Projektidee vorstellen (Was ist das? Was wird das? Wozu? Was soll es können?)
* Layout der Website 
* Einzelne Funktionen und Klassen
* Content

### Idee
Ein Vokabellernprogramm das zum Vokabellernen motivieren soll.
Der Spieler erhält für das richtige beantworten erhält der Spieler Punkte. 
Diese Punkte werden für die Pflege eines Monsters verbraucht. Das Monster, welches ebenfalls benannt werden kann, wird nach einiger Zeit hungrig. Um das Monster zu Füttern kann der Player seine erspielten Punkte gegen Items, wie zb. Beeren oder Schokolade eintauschen mit denen die Kreatur gefüttert werden kann.
Wird es nicht gefüttert wird das Monster hungriger, ist ein bestimmter Wert überschritten, dann verliert das Monster Lebenspunkte. Es verhungert!
Somit funktioniert als "Punkte-Drain", so dass der Spieler ständig neue Punkte 'erlenen', bzw. erspielen muss.
Das Monster selbst besitzt ein Alter und ein Level. Je mehr der Spieler lernt, desto mehr Erfahrungspunkte(Exp) erhält es. Wenn das Monster mehrere Level erreicht hat entwickelt es sich!

### Ziel
  * Ziel: ein schönes kleines Projekt zum laufen bekommen 
  * Optional: Responsive Design für kleinere Bildschrime
  * Ein Zeitplan, bis wann soll was fertig werden. (Das kann man bei GitHub als Milestone eintragen)
  * Ein kleines, schönes Programm das läuft

#### Must-Have:
  *
  *
  * Vokabeliste schon vorgeben mit 10 Vokabeln
  
#### Nice-to-Have:

### Umsetzung
Bottle (www.bottlepy.org/)ein Webframework für Python + ein wenig HTML & CSS für Website

Problem:

   * Bei Seitenneuladen Daten weg, d.h. Daten irgendwo speichern (man will ja sowieso eine Speicherfunktion)

### Layout
Hier gehören Bilder, Skizzen von Layout hin

Bild 1
Funktionen:

Menu: Vokabeln, Pet,  Shop 

Lernen -> Testauswahl -> Lernbildschrim 
Vokabeln -> Vokabeltabelle
Shop -> Einkaufsbildschrim
Pet -> Petstatus
Player -> Playerstatus (+ Inventory) 

Testauswahl: Player wählt Art des Abfrage aus
-
-

Lernbildschrim: Player beantwortet Fragen, Fragen werden angezeigt bis Player 'zurück' klickt oder alle Vocs abgefragt wurden.   
-
-






### Funktionen und Klassen 


### nicht so richtige Interaktivität
Die Website fragt jede Minute den Server an.
Der Server sendet dann die Websitedaten erneut.

Das Anfrage geschieht über Javascript/jquery.

mit Workarounds o.ä.,Klassen + Variablen, technisch konkret

## Aufbau
Die Controllerklasse verwaltet (fast) alles: Player, Monster, Timer(oder der Timer wandert in die Controllerklasse?), Vokabeln und Vokabellisten, Frage-Antwort.
Die Controllerklasse übernimmt das laden (und speichern?) von Daten.
Die Gui sollte mit der Controllerklassekommunizieren, aber nicht darin enthalten sein, um Abhängigkeiten zu vermeiden. 
Die Gui ist die Bottle-App, der Teil des Programms wo das Bottleframework eingesetzt wird. 
Die Daten für die Gui kommen von der Controllerklasse. Die Controllerklasse sendet der Gui Daten was angezeigt werden soll.

#### Monsterklasse 
Das Monster (Tamagochi) ist eine eigene Klasse.
Die Monster hat Variablen:
  - Name = Name des Monsters
  - HP = Lebenspunkte
  - Hunger-Zähler
  - Status

  
Der Name kann geändert werden. 
Die HP (Health Points/Lebenspunkte) bei 0 ist das Monster tot.
Der Hungerzähler wird herunter gezählt, 
Status, gibt an in welchem Zustand das Monster ist. Es kann für den Anfang entweder normal oder hungrig sein.
(Stati sollten nachher einfach eingefügt werden, damit das Monster erweiterbar ist.)
Dazu gibt es Status-Klassen, diese enthalten Informationen darüber wie der Status angezeigt wird
und was für Auswirkungen er auf das Monster hat. das Monster hat eine set-status-Funktion, 
mit der die Attribute (z.b. ein anderes Bild) des Monsters an den Status angepasst werden. 

Die Monster- Klasse benötigt folgende Funktionen:
    - Namen
    - Export der eigenen Daten (zum Speichern)
    - set-status: Verändern der eigenen Daten: Status, Hunger-Variable)
    - reduce(Wert, amount): setzt Wert herab
    - add(WErt, amount): hebt Wert um amount an
    
    Optional:
    - Birthday
    - Alter
    - Item: Monster kann ein Item halten
    - Farbe: Spieler kann Monsterfarbe ändern

Die Playerklasse benötigt:
    - Namen
    - VocPet
    - VocListe
    - Punkte

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
Die Frage ist wie man nun die Gui automatisch per Bottle updatet. So sollte auch das Monster animiert werden. Oder man mal eine gif-animation..

Nach einigem Versuchen stelle ich fest: Das scheint nicht einfach zu sein. 
Alternativ kann man per javascript den Client die Seite immer wieder neu anfragn lassen. Das gefällt mir zwar nicht ganz, aber 
es funktioniert. Habe ich im Netz gefunden, einmal das time interval und dann den Code um eine json Datei vom Bottle-Server anzufragen. 

code:    
INSERT CODE HERE


In der Variablen data.test und werden die daten aus der jsondatei gespeichert. Das ganze wird dann im html-tag mit der ID 'response' angezeigt.
Diese Funktion ruft sich selbst jede Sekunde auf. 
Man könnte theoretisch die ganzen Daten per json senden, dann hätte man eine API und könnte Clients mit beliebigen Programmen bauen. 
(Das ist aber erstmal gar nicht Sinn der Sache.)

Nun zu den Gamification-Dingen:
Item, Archivements, Fortschrittsbalken (ich fürchte die muss man clientseitig per css oder javascript darstellen, da muss ich nochmal nachlesen..)

Items:
Ein Item hat:
    einen Preis (der Spieler hat das Geld in From von Punkten, Punkte gibt es bei richtigem Antworten auf Fragen.)  
    eine Funktion, zb. Hunger-Counter erhöhen etc.
    eine Bildchen/Icon
    ggf. eine Beschreibung
    Item halten sich erstmal ewig

Inventory:
    im Besitz vom Spieler, sammelt die Items die der Spieler besitzt
    sollte Infos über den Besitz des Spielers herausrücken, damit diese per Controller an GUI gesendet werden können, (vllt. im json-format bzw. als dictionary) um angezeigt zu werden
    hat erstmal keine Platzbegrenzung

Archivements:
    Player erhält für das tun von Dingen Archievements.
    Laut einem Buch ('Pattern für Spieleprogammierung') programmiert man diese Funktion die ein Archievement gibt nicht in andere unbeteiligte Berreiche, sondern nutzt das Observer-Pattern dafür.
    Mal schauen ob ich das umsetzen kann. Erstmal betrachte ich Archivements auf 'nice to have + optional'.
    Ein Archievement benötigt:
    - Bild
    - Beschreibung
    - Ton?

Archivementmanager: gehört zur logic, observiert und zählt Aktionen um Archievements zu vergeben
Archivementliste: Hier kommen die Archievements rein, die der Player gesammelt hat

Frageklasse:
Diese Klasse ist die Elternklasse der verschiedenen Fragearten: 
Erstmal machen wir nursowas wie eine Texteingabe-Klasse, oder eine MultipleChoice-Klasse.
Die Frageklasse enthält bei MultipleChoice die Frage, die möglichen Antworten, die die Spieler wählen kann, und eine Liste welche Antworten ausgewählt werden müssen. 
Das alles kann in einer Datei gespeichert un geladen werden. Am besten so dass der Spieler es nicht lesen kann, also z.B. gehasht.(Aber das ist optional und nice-to-have.)

### Content


#### Graphiken:





