#Projekt-Plan

### Idee
Ein Vokabellernprogramm, das besonders gut zum lernen motivieren soll. Dazu wird ein Vokabeltrainer mit einem virtuellen Haustier kombiniert. 

### Was sind typische Elemente von Vokabeltrainersoftware?
Mir bekannte Beispiele für Vokabeltrainersoftware sind unter anderem:
  * Anki (http://ankisrs.net/)
  * Memrise (https://www.memrise.com/)
  * Mnemosyne (http://mnemosyne-proj.org/)

#### Anki und Mnemosyne
Anki und Mnemosyne sind OpenSource-Programme, sie laufen offline. Anki kann mit Plugins erweitert werden. Mnemosyne ebenfalls. Beide können über das Internet synchronisiert werden, um die Vokabeln auf dem gleichen Stand zu halten, wenn man von verschiedenen Geräten aus lernt. Die beiden Programme funktionieren nach dem Karteikartenkasten-Prinzip. Eine Frage wird angezeigt,wenn der Nutzer klickt erscheint die Antwort. Dann bewertet der Nutzer auf einer Skala wie schwer oder leicht ihm die Lösung fiel. Die Karte erhält dem entsprechend ein neues “Fälligkeitsdatum”,an dem sie dem Nutzer erneut angezeigt werden wird.

#### Memrise
Es handelt sich hierbei um ein kommerzielles Produkt, allerdings kann man es kostenlos nutzen. Memrise benötigt eine Internetverbindung und läuft im Browser. Für einige Smartphonebetriebssyteme gibt es kostenpflichtige Apps. Den Content, den man auf der Memrisewebsite erstellt, kann die Firma weiter nutzen. So füllen die Nutzer als Prosumer die Vokabeldatenbank. Memrise arbeitet mit Bildern, sogenannten Mems die einer Vokabel zugeordnet und bei fehlerhafter Antwort angezeigt werden, um das lernen zu erleichtern. Erstellte Bilder und Vokabeln, werden in Datenbanken gespeichert. Es gibt allgemeine Datenbanken, aus denen Nutzer Vokabeln beziehen können, sowie Datenbanken nur für bestimmte Kurse, bzw. Sprach-Kombinationen. Gewinn macht Memrise dadurch, dass die Nutzer gegen monatliche Gebühr ihre Accounts upgraden können, wodurch ihnen mehr Features zur Verfügung stehen.

Von den drei Beispielen nutzt Memrise die meisten Gamificationelemente: Lernende erhalten Punkte für das erfolgreiche Beantworten der Vokabelabfragen. Die zu lernenden Vokabeln symbolisieren Blumen die gepflanzt werden sollen, durch Lernen gießt man sozusagen die Vokabel-Blumen. Auch werden Level benutzt: Mit bestimmter Punktanzahl steigen Nutzer auf und erhalten einen höheren Rang, dies zeigt sich am Logo.

Das Programm ist gut gemacht, aber, nach einiger Zeit wird es langweilig und eintönig. Der Abstand gerade bei hohen Leveln ist sehr groß und die Punkte zu sammeln ist an sich sind ziemlich nutzlos.

### Was ist ein Tamagochi?
Tamagochi ist ein Spielzeug für Kinder, das ein Monster bzw. Haustier simuliert um das der Spieler sind kümmern muss, sonst stirbt es. Ja nachdem wie gut man das Tamagochi pflegt entwickelt es sich weiter, das heißt es ändert Form und Aussehen. Zu Zeiten des PokemonGo-Hypes, einem Spiel wo Spieler Monster fangen und großziehen um sie Kämpfen zu lassen, spricht wenig gegen das Spielelement Monsteraufzucht.

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
  * Progressbar
  * Dokumentation
  * Animationen
  
#### Nice-to-Have:
  * weitere Stati: Langeweile, Dreckig, Krank
  * weitere Items um die neuen Stati zu 'heilen'
  * Responsive Design für kleinere Bildschirme
  * Lernmodus: Antwort eintippen
  * Lernmodus: 1-5 Wie gut gewusst
  * vorgefertigte Vokabellisten
  * Import (json)
  * Badges
  * Tutorial

### Umsetzung
Eigentlich würde ich das ganze gerne als Multi-User Programm machen.
Das wird mir im Rahmen des Projekts nicht gelingen.

#### Warum im Webbrowser? 
Bottle (www.bottlepy.org/)ein Webframework für Python + ein wenig HTML & CSS für Website
Das ist ein Kompromiss, ich kann dem Umgang mit einem Webframework üben, ohne mich um Probleme kümmern zu müssen, welche die Erstellung von die multi-user Software mitsichbringt.

### Layout und Funktionen
Ich behalte mir vor das Layout und Design  zwecks usability und Ästetik anzupassen, (vorallem in der Betatestphase).


#### Hauptbildschirm
![](http://up.picr.de/26466728za.png)

#### Mulpiplechoicelernbildschirm 
![](http://up.picr.de/26466740ct.png)

#### Lernmodus wählen
![](http://up.picr.de/26466727sz.png)

#### Item einkauf:
![](http://up.picr.de/26466726fb.png)

#### Vokabelliste
![](http://up.picr.de/26466732ec.png)

#### Inventar
![](http://up.picr.de/26466730wb.png)
wird wohl noch überarbeitet, es sieht aus wie der Einkaufsbildschrim.

#### Einstellungen
![](http://up.picr.de/26466731ao.png)

#### Skizze des Monsters
![](http://up.picr.de/26466742nx.png)
Das Monster wurde kurzerhand zum Alien erklärt, das menschliche Sprachen lernen will.
Das wäre die 'Geschichte' des Spiels.

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
### Kein Speicherung von Zuständen(?)
Bei Seitenneuladen Daten weg, 
Workaround: Daten irgendwo speichern (man will ja sowieso eine Speicherfunktion)
    
### nicht so richtige Interaktivität
Die Website fragt jede Minute den Server an.
Der Server sendet dann die Websitedaten erneut.
Das Anfrage geschieht über Javascript/jquery.
Das ist ein Workaround, schöner wäre es wenn das serverseitig gereget würde. 


