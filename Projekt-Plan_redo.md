#Projekt-Plan

##TODO 
FERTIG SCHREIBEN

##Inhalt 
* Projektidee vorstellen (Was ist das? Was wird das? Wozu? Was soll es können?)
* Layout der Website 
* Einzelne Funktionen und Klassen
* Content

### Idee
Ein Vokabellernprogramm, das besonders gut zum lernen motivieren soll.Dazu wird ein Vokabeltrainer mit einem virtuellen Haustier kombiniert. 

#### Wie funktioniert das ganze?
Der Spieler erhält für das richtige beantworten von Vokabelfragen Punkte.
Diese Punkte werden für die Pflege eines Monsters verbraucht. Das Monster, welches ebenfalls benannt werden kann, wird nach einiger Zeit hungrig. Um das Monster zu Füttern kann der Player seine erspielten Punkte gegen Items, wie zb. Beeren oder Schokolade eintauschen mit denen die Kreatur gefüttert werden kann.
Wird es nicht gefüttert wird das Monster hungriger, ist ein bestimmter Wert überschritten, dann verliert das Monster Lebenspunkte. Es verhungert!
Somit funktioniert als "Punkte-Drain", so dass der Spieler ständig neue Punkte 'erlenen', bzw. erspielen muss.
Das Monster selbst besitzt ein Alter und ein Level. Je mehr der Spieler lernt, desto mehr Erfahrungspunkte(Exp) erhält es. Wenn das Monster mehrere Level erreicht hat wird es größer. Es ändert sein Aussehen! 
Vielleicht ändern sich dann auch seine Essgewohnheiten, und es verlangt nach besserem, teureren Items als Essen.

### Ziel
  * Mein Ziel: ein schönes kleines Projekt zum laufen bekommen :)
  * Die Punkte der Must-Have-Liste umsetzen

#### Must-Have:
  * Gui - Anzeige des Programms über das der Nutzer mit dem Spiele interagiert 
  * Monster
  * Spieler
  * Lernmodus (Multiple Choice)
  * Status: Hunger - Monster wird mit der Zeit Hunger
  * Items: Futter 
  * Export (json)
  * Vokabelliste schon vorgeben mit 10 Vokabeln
  
#### Nice-to-Have:
  * weitere Stati: Langeweile, Dreckig, Krank
  * weitere Items um die neuen Stati zu 'heilen'
  * Responsive Design für kleinere Bildschirme
  * Lernmodus: Antwort eintippen
  * Lernmodus: 1-5 Wie gut gewusst
  * vorgefertigte Vokabellisten
  * Import (json)

### Umsetzung
Eigentlich würde ich das ganze gerne als Multi-User Programm machen.
Das wird mir im Rahmen des Projekts nicht gelingen.

#### Warum im Webbrowser? 
Bottle (www.bottlepy.org/)ein Webframework für Python + ein wenig HTML & CSS für Website

Das ist ein Kompromiss, ich kann dem Umgang mit einem Webframework üben und 

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
  
  * Multiple Choice
  * (Texteingabe) 

Lernbildschirm: 

  * Player beantwortet Fragen   
  * Fragen werden angezeigt bis Player 'zurück' klickt oder alle Vocs abgefragt wurden


### Objekte des Spiels:

## Spieler
Der Spieler hat ein Bild, einen Namen und Punkte, eine Vokabelliste, die Vokabeln beinhaltet, ein Inventory das Items beinhaltet und sein Vokabel-Monster.

## Monster 
Das Monster hat einen Namen. Der Name kann geändert werden.
Das Monster hat Lebenspunkte (HP), ein Level, Erfahrungspunkte (Exp), einen Hungerwert, einen Pfad zu einem Bild,  einen Status. Der Status kann verschiedene Werte haben:
hunger oder normal. Ist das Monster hungrig, sinkt der Hungerwert des Monsters. Ist dieser Hungerwert bei 0 sinken die HP des Monsters. Sind diese <= 0 dann ist das Monster tot und der Spieler erhält ein neues.
Lernt der Spieler Vokabeln steigen die Exp der Monsters, ist ein Bestimmter Wert erreicht steigt sein Level an (und die Exp werden wieder auf 0 gesetzt).

## Item
Items haben ein Bild, einen Preis, ggf. eine Beschreibung und einen Nutzen.
Ein Nutzen wäre z.B. dass das Monster satt wird, wenn man es mit Schokolade füttert.

## Vokabelliste  
Die Vokabelliste beinhaltete Vokabeln.
Die Vokabeln werden aus der Liste raus in weitere Listen sortiert: alle aktiven Vokabeln in eine eigene Liste, alle ungesehenen Vokabeln in eine Liste, alle fälligen Vokabeln in eine eigene Liste. Die Anzahl der Listenelemente wird wieder auf der Website angezeigt und aktualisiert.

## Voc
Ein 'Voc' stellt eine Vokabelkarte da. Sie hat einen Begriff (die Frage) und eine Bedeutung (die gesuchte Antwort). zwecks usability hat ein 'Voc' auch ein Hinweis-Feld, ein Feld wo ein Bild angegeben werden kann, einen Vermerkt um welche Sprache es sich handelt. 
Ein Voc hat repetition_points, die messen wie häufig wurde die Vokabel schon richtig beantwortet wurde.Die mit dem niedrigsten Wert kann dem Spieler vorgeschlagen werden. (Das ist ein einfache Version einen Wiederhohlungsmechanismus einzubauen.) 
Außerdem haben Voc ein Fälligkeitsdatum, einen Zeitstempel. Ist dieser größer als die aktuelle Zeit, ist die Vokabel fällig und soll abgefragt werden. Diese beiden Mechanismen kann man kombinieren und nur die Karten die Fällig sind nach repetition_point_anzahl sortiert anzeigen. (Sortieren könnte gegebenfalls schwierig werden. Klasse an Attribut-Eingenschaft sortieren... )

#### VocListe:
Die Voc-Liste beinhaltet mehrerer Listen in die die Vokabelkarten sortiert/gruppiert werden können,
z.B. je nach repetition-point-anzahl. 

Timer-Klasse
misst die fortgeschrittene Zeit und löst Events aus. Die Frage ist wie man nun die Gui automatisch per Bottle updatet. So sollte auch das Monster animiert werden. Oder man mal eine gif-animation..

Nach einigem Versuchen stelle ich fest: Das scheint nicht einfach zu sein. 

#### Alternativlösung:
Alternativ kann man per javascript den Client die Seite immer wieder neu anfragen lassen. Ist zwar nicht ganz so gut, aber es funktioniert. Habe ich im Netz gefunden, einmal das time interval und dann den Code um eine json Datei vom Bottle-Server anzufragen. 

code:    
INSERT CODE HERE


### Gamification 
Nun zu den Gamification-Dingen:
Item, Archivements, Fortschrittsbalken. Wie wird das clientseitig dargestellt? 

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
    * Bild
    * Beschreibung
    * Ton?

Archivementmanager: gehört zur logic, observiert und zählt Aktionen um Archievements zu vergeben
Archivementliste: Hier kommen die Archievements rein, die der Player gesammelt hat

Frageklasse:
Diese Klasse ist die Elternklasse der verschiedenen Fragearten: 
Erstmal machen wir nursowas wie eine Texteingabe-Klasse, oder eine MultipleChoice-Klasse.
Die Frageklasse enthält bei MultipleChoice die Frage, die möglichen Antworten, die die Spieler wählen kann, und eine Liste welche Antworten ausgewählt werden müssen. 
Das alles kann in einer Datei gespeichert un geladen werden. Am besten so dass der Spieler es nicht lesen kann, also z.B. gehasht.(Aber das ist optional und nice-to-have.)

### Content


#### Graphiken:




###Probleme
### Kein Steicherung von Zuständen(?)
Bei Seitenneuladen Daten weg, 
Workaround: Daten irgendwo speichern (man will ja sowieso eine Speicherfunktion)
    
### nicht so richtige Interaktivität
Die Website fragt jede Minute den Server an.
Der Server sendet dann die Websitedaten erneut.
Das Anfrage geschieht über Javascript/jquery.
Das ist ein Workaround, schöner wäre es wenn das serverseitig gereget würde. 


