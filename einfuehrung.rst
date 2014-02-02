****************************
Einführung ins Programmieren
****************************

In den meisten Programmiersprachen - so auch in Python - ist ein Programm eine
einfache Textdatei, welche mit einem beliebigen Texteditor bearbeitet werden
kann.

Das Ausführen des Programms bedeutet einfach, dass Python die Anweisungen in der
Textdatei Zeile für Zeile durcharbeitet, bis es am Ende der Datei angelangt
ist.

Das erste Beispielprogramm, welches üblicherweise in einer Programmiersprache
verfasst wird, ist ein sogenanntes "Hello World"-Programm, welches nichts
anderes macht, als den Text "Hello World" auf dem Bildschirm ausgeben.

.. literalinclude:: code/HelloWorld.py
   :linenos:

Beachte: Die Zahl ``1`` vor dem Programm gehört nicht zum Programm. Dies ist die
Zeilennummer. In diesem Skript sind alle Programme mit Zeilennummern versehen.
Zeilennummern sind im Programmieren wichtig um über Programme zu sprechen und
Fehler zu finden. So werden zum Beispiel bei Fehlermeldungen oft die
Zeilennummer angegeben, wo der Fehler passiert ist. Die hilft dir dann wiederum,
den Fehler in deinem Programm zu finden.

what : how
  test hier bin


IDLE - Ein Python IDE
=====================

Zum Programmieren reicht eigentlich ein Texteditor. Oft werden aber sogenannte
*IDEs (Integrated Development Environment)* benutzt. Diese besitzen viele
hilfreiche Funktionen, welche ein Texteditor nicht hat. Unterstützt einem beim
Programmieren mit den folgenden


* Die Syntax der Programmiersprache wird durch Farben hevorgehoben, um den Code
  leserlicher zu machen.
* Das Programm kann direkt im IDE ausgeführt werden und muss nicht separat
  ausgeführt werden.
* Die Befehle werden automatisch vervollständigt, so dass man nicht die ganzen
  Befehle tippen oder erinnern muss.

Wir werden ein sehr einfaches IDE namens IDLE [#]_ benutzen.
  
.. [#] Oft erfinden Informatiker zweideutige Namen für ihre Programme. Schau
       nach was "idle" auf englisch bedeutet.

Falls du Python auf deinem eigenen Computer zu Hause installieren möchtest,
findest du die nötigen Dateien hier:

http://www.python.org/download/releases/3.3.2/

Die Dokumentation von Python findest du entweder in IDLE im Menu unter
*Help* - *Python Docs* oder online unter

http://docs.python.org/py3k/

Wenn du IDLE startest, siehst du zuerst nur den sogenannten
Befehlsprompt. Dieser sieht ungefähr so aus::
  
   Python 3.2.3 (default, Feb 20 2013, 14:44:27) 
   [GCC 4.7.2] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

Die Befehle im Befehlsprompt kannst du nicht als Programm speichern, du kannst
sie nur einzeln hintereinander ausprobieren.  Nun wollen wir ein Programm
erstellen, welches in einer Datei gespeichert ist. So kannst du es später auch
wieder öffnen und verändern.

Im Menu von IDLE kannst du unter *File* - *New Window* ein neues Fenster
öffnen. In dieses Fenster kannst du dein Programm schreiben, in dem du die
Befehle untereinander auf einzelne Zeilen schreibst.

Speichere aber die leere Datei zuerst unter dem Namen ``helloworld.py``
ab.

.. note:: Du musst die Endung ``.py`` selbst anhängen, IDLE macht dies nicht für
	  dich. Wenn du es vergisst, erkennt IDLE deine Datei nicht als Programm
	  und wird dir den Code nicht farbig darstellen.

   
Aufgaben
========

1. Probiere die folgenden Befehle aus und notiere dir, was sie tun. Überlege dir,
   ob sie wirklich tun, was du vermutest.

   >>> 1 + 2 * 4

   >>> print("Hello World!")

   >>> sorted( [4,3,2,5,10,9] )

   >>> sum( [4,3,2,5,10,9] )

   >>> (4 + 3) / 5

   >>> (4 + 3) // 5


2. a) Erstelle in einem leeren Fenster ein "Hello World"-Programm. Falls du
      nicht weiter weisst, kannst du noch einmal den Anfang dieses Kapitels
      lesen.
   b) Das Programm kannst du mit der F5-Taste ausführen und testen. Wo wird der
      Text "Hello World" ausgegeben'?
   c) Wie sieht das Nassi-Shneiderman-Diagramm für dieses einfache Programm aus?

      
3. a) Speichere das folgende Programm in einer Datei namens ``gui-beispiel.py``
      und führe es aus. Was macht das Programm?
   b) Musst du wirklich alle Zeilen abtippen, damit es funktioniert?

   .. literalinclude:: code/CanvasExample.py
      :linenos:


  
