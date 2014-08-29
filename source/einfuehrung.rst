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
anderes macht, als den Text "Hello World" auf dem Bildschirm auszugeben.

In Python ist ein solches Programm im Verlgeich zu anderen Programmiersprachen
sehr einfach umzusetzen. Es besteht nur aus einer Zeie:

.. literalinclude:: code/HelloWorld.py
   :linenos:

Beachte: Die Zahl ``1`` vor dem Programm gehört nicht zum Programm. Dies ist die
Zeilennummer. In diesem Skript sind alle Programme mit Zeilennummern versehen.
Zeilennummern sind im Programmieren wichtig, um über Programme zu sprechen und
Fehler zu finden. So wird zum Beispiel bei einer Fehlermeldung oft die
Zeilennummer angegeben, wo der Fehler passiert ist. Die hilft dir dann, den
Fehler in deinem Programm zu finden.


IDLE - Ein Python IDE
=====================

Zum Programmieren reicht ein einfacher Texteditor. Oft werden aber sogenannte
*IDEs (Integrated Development Environment)* benutzt. Diese besitzen viele
hilfreiche Funktionen, welche ein Texteditor nicht hat. Sie unterstützen einen
beim Programmieren. Die folgenden Funktionen werden wir auch benutzen:

* Die Syntax der Programmiersprache wird durch Farben hervorgehoben, um den Code
  leserlicher zu machen.
* Das Programm kann direkt im IDE ausgeführt werden und muss nicht separat
  aufgerufen werden.
* Die Befehle werden automatisch vervollständigt, so dass man nicht die ganzen
  Befehle tippen oder erinnern muss. 

Wir werden ein sehr einfaches IDE namens IDLE [#]_ benutzen.

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
sie nur einzeln hintereinander ausprobieren. In diesem Skript werden wir oft
Beispiele benutzen, welche dafür gedacht sind, dass du sie direkt am
Befehlspromt ausprobierst. Sie sind immer duch ``>>>`` markiert und haben keine
Zeilennummern wie andere Programme. Du könntest also zum Beispiel

>>> print("Hallo Welt!")

oder

>>> 2 + 3

ausprobieren. IDLE hat immer nur einen Befehlsprompt. Du kannst also kein neues
Befehlsprompt-Fenster öffnen.

Es macht aber oft keinen Sinn, die Befehle für ein Programm jedes mal am
Befehlsprompt von neuem einzutippen. Wollen wir ein Programm mehrmals benutzen,
macht es Sinn, es in einer Datei abzuspeichern. So kannst du es später auch
wieder öffnen, verändern oder erneut ausführen.

Im Menu von IDLE kannst du unter *File* - *New Window* ein neues Fenster
öffnen. In dieses Fenster kannst du dein Programm schreiben, in dem du die
Befehle untereinander auf einzelne Zeilen schreibst.

Sobald du die Datei unter *File* - *Save* abgespeichert hast, kannst du mit der
Taste ``F5`` das Programm starten. 

.. note:: Du musst die Endung ``.py`` selbst anhängen, IDLE macht dies nicht für
	  dich. Wenn du es vergisst, erkennt IDLE deine Datei nicht als Programm
	  und wird dir den Code nicht farbig darstellen.

Beachte, dass du ein solches neues Fenster erst in Aufgabe 2 benötigsts. Die
ersten Befehle kannst du am Befehlsprompt ausprobieren. 
   
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


2. a) Erstelle wie oben erklärt ein neues Fenster. Erstelle nun in diesem
      Fenster ein Hello-Wolrld-Programm. Falls du nicht weiter weisst, kannst du
      noch einmal den Anfang dieses Kapitels lesen.
   b) Das Programm kannst du mit der F5-Taste ausführen und testen. Wo wird der
      Text "Hello World" ausgegeben?

      
3. a) Speichere das folgende Programm in einer Datei namens ``gui-beispiel.py``
      und führe es aus. Was macht das Programm?
   b) Musst du wirklich alle Zeilen kopieren, damit es funktioniert?

   .. literalinclude:: code/CanvasExample.py
      :linenos:


.. rubric:: Footnotes
	  
.. [#] Oft erfinden Informatiker zweideutige Namen für ihre Programme. Schau
       nach was "idle" auf englisch bedeutet.
    
