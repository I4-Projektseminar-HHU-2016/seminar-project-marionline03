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
Das ist ein Kompromiss, ich kann dem Umgang mit einem Webframework üben, ohne mich um Probleme kümmern zu müssen, welche die Erstellung von die multi-user Software mitsichbringt.

### Layout und Funktionen
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

#### Spieler
Der Spieler hat ein Bild, einen Namen und Punkte, eine Vokabelliste, die Vokabeln beinhaltet, ein Inventory das Items beinhaltet und sein Vokabel-Monster.

#### Monster 
Das Monster hat einen Namen. Der Name kann geändert werden.
Das Monster hat Lebenspunkte (HP), ein Level, Erfahrungspunkte (Exp), einen Hungerwert, einen Pfad zu einem Bild,  einen Status. Der Status kann verschiedene Werte haben:
hunger oder normal. Ist das Monster hungrig, sinkt der Hungerwert des Monsters. Ist dieser Hungerwert bei 0 sinken die HP des Monsters. Sind diese <= 0 dann ist das Monster tot und der Spieler erhält ein neues.
Lernt der Spieler Vokabeln steigen die Exp der Monsters, ist ein Bestimmter Wert erreicht steigt sein Level an (und die Exp werden wieder auf 0 gesetzt).

#### Item
Items haben ein Bild, einen Preis, ggf. eine Beschreibung und einen Nutzen.
Ein Nutzen wäre z.B. dass das Monster satt wird, wenn man es mit Schokolade füttert.

#### Inventory
Es ist im Besitz des Spielers und sammelt die Items die der Spieler besitzt. 
Die Items und Informationen über die Items werden im Client dargestellt.

#### Vokabelliste  
Die Vokabelliste beinhaltete Vokabeln.
Die Vokabeln werden aus der Liste raus in weitere Listen sortiert: alle aktiven Vokabeln in eine eigene Liste, alle ungesehenen Vokabeln in eine Liste, alle fälligen Vokabeln in eine eigene Liste. Die Anzahl der Listenelemente wird wieder auf der Website angezeigt und aktualisiert.

#### Voc
Ein 'Voc' stellt eine Vokabelkarte da. Sie hat einen Begriff (die Frage) und eine Bedeutung (die gesuchte Antwort). zwecks usability hat ein 'Voc' auch ein Hinweis-Feld, ein Feld wo ein Bild angegeben werden kann, einen Vermerkt um welche Sprache es sich handelt. 
Ein Voc hat repetition_points, die messen wie häufig wurde die Vokabel schon richtig beantwortet wurde.Die mit dem niedrigsten Wert kann dem Spieler vorgeschlagen werden. (Das ist ein einfache Version einen Wiederhohlungsmechanismus einzubauen.) 
Außerdem haben Voc ein Fälligkeitsdatum, einen Zeitstempel. Ist dieser größer als die aktuelle Zeit, ist die Vokabel fällig und soll abgefragt werden. Diese beiden Mechanismen kann man kombinieren und nur die Karten die Fällig sind nach repetition_point_anzahl sortiert anzeigen. (Sortieren könnte gegebenfalls schwierig werden. Klasse an Attribut-Eingenschaft sortieren... )

#### VocListe:
Die Voc-Liste beinhaltet mehrerer Listen in die die Vokabelkarten sortiert/gruppiert werden können,
z.B. je nach repetition-point-anzahl. 

#### Fragen+Antworten
Die Frage mit der richtigen Lösung muss auf dem Server gespeichert werden, denn beim Laden der Seite vergisst der Server alles. Die Frage-object erhält diese Daten, es enthält alle Informationen für die Gui, die gebraucht werden um die Vokabelabfragen durchzuführen und um die falschen und richtigen Antworten dem Spieler anzuzeigen. Das ist wichtig für den Lerneffekt. Bei unterschiedlichen Abfragearten werden unterschiedliche Daten benötigt, es müssen unterschiedliche Elemente (Eingabefelder, Buttons, ...) auf der Website dargestellt werden. 
  
#### Archivement
Ein Archivement erhält ein Spieler durch eine Handlung oder eine Anzahl von Handlungen.
Ein Archievement ist eine Belohnung. Es belohnt mit einem Bild, Items und Exp und soll zu noch mehr Leistung motivieren. Es gibt Ketten von Archievements, die schwittweise in der Schwierigkeit steigen. Beispiel: 
  * Archievement 1: füttere das Monster mit 5 Beeren, 
  * Archivement 2: füttere das Monster mit 10 Beeren.
Die Archivements sieht man auf der Player-Status-Seite, wo auch Einstellungen vorgenommen werden können.
Für welche Aktionen man Archivements erhält wird nicht bekannt gegeben, bis man das Archivement erhält.
Die neusten, erspielen Archivemnts (5 Stück?) werden auf der Hauptseite angezeigt.

#### Playerstatusseite:
Hier kann der Spieler sein Icon auswählen, einen Namen und seine Schriftfarbe/oder das Layout ändern.
Außerdem sieht er hier alle Archivements aufgelistet.      
  
#### Graphiken:

### Weitere Sachen, die man bedenken kann:

#### Übersetzbarkeit:
Übersetzbarkeit der Website, hierfür wird der Text in eine eingene Pythondatei geschrieben und geladen wenn benötigt.

###Probleme
### Kein Steicherung von Zuständen(?)
Bei Seitenneuladen Daten weg, 
Workaround: Daten irgendwo speichern (man will ja sowieso eine Speicherfunktion)
    
### nicht so richtige Interaktivität
Die Website fragt jede Minute den Server an.
Der Server sendet dann die Websitedaten erneut.
Das Anfrage geschieht über Javascript/jquery.
Das ist ein Workaround, schöner wäre es wenn das serverseitig gereget würde. 


