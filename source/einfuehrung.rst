.. _kap-einfuehrung:

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


Editoren und IDEs
=================

Zum Programmieren reicht ein einfacher Texteditor. Im Gegensatz zu
Textverarbeitungsprogrammen unterstützt das benutzte Textformat keine
Formatierungen wie Schriftgrössen oder Schriftarten. Alle Farben, welche du im
Texteditor siehst, werden vom Editor erstellt und sind nicht in der Datei selbst
gespeichert. Texteditoren wurden schon in den Anfängen der
Computerprogrammierung benutzt, gewisse aus dieser Zeit werden heute noch
benutzt, unter ihnen zum Beispiel Emacs_ und `Vi(m)`_. Wer einen moderneren Editor
benutzen möchte, schaut sich Atom_ an

Jedoch werden oft sogenannte *IDEs (Integrated Development Environment)* benutzt. 
Diese besitzen viele hilfreiche Funktionen, welche ein Texteditor nicht hat,
welche einem beim Programmieren unterstützen. Die folgenden Funktionen werden 
wir auch benutzen:

* Die Syntax der Programmiersprache wird durch Farben hervorgehoben, um den Code
  leserlicher zu machen.
* Das Programm kann direkt im IDE ausgeführt werden und muss nicht separat
  aufgerufen werden.
* Die Befehle werden automatisch vervollständigt, so dass man nicht die ganzen
  Befehle tippen oder erinnern muss.
* Gewisse Fehler im Programm werden schon während dem programmieren erkannt und
  als solche gekennzeichnet.

Wir werden ein für Python entwickeltes IDE namens PyCharm_ benutzen. Dieses
kannst du auf der Webseite herunterladen und zu Hause installieren.

Da es sich nur um ein IDE handelt, welches Python noch nicht dabei hat, musst du
auch Python selbst noch herunterladen und installieren. Die nötigen Downloads
findest du hier:

https://www.python.org/downloads/

Die Dokumentation von Python findest du auch online unter:

https://docs.python.org/py3k/

PyCharm_ lässt dich nicht nur Python-Programme editieren, sondern auch mehrere 
Dateien zu einem *Projekt* zusammenfassen. Erstelle aus diesem Grund beim ersten 
Starten von PyCharm_ ein Projekt. Achte darauf, dass du einen Speicherort
innerhalt deinen eigenen Dateien wählst, etwa in einem Ordner mit dem Namen
"Informatik". Bennenne das Projekt jeweils nach dem Kapitel, an welchem du
gerade arbeitest. Innerhalb des Projekts kannst du für jede weitere Aufgabe eine
neue Python-Datei anlegen, in dem du im Menu `File` -> `New...` anklickst und
anschliessens `New Python-File` wählst.

Die erste Aufgabe, in welcher du eine Datei benötigst ist die Aufgabe 2. Nenne
also deine erste Datei "Aufgabe 2".

Im unteren Bereich des PyCharm_-Fensters siehst du einen Reiter mit dem Namen
"Konsole". Wenn du ihn öffnest, siehst du etwas den folgenden Text::

   Python 3.5.3 (default, Mar 14 2016, 16:02:22) 
   [GCC 4.8.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 

Dies ist der Python Befehlspromt, hier kannst du Befehle nicht als Programm 
speichern, du kannst sie nur einzeln hintereinander ausprobieren. In diesem 
Skript werden wir in Aufgaben oft
kurze Beispiele im Befehlspromt ausprobieren. Sie sind immer duch ``>>>`` 
markiert und haben keine Zeilennummern wie andere Programme. Du könntest 
also zum Beispiel

>>> print("Hallo Welt!")

oder

>>> 2 + 3

eingeben. PyCharm_ hat immer nur einen Befehlsprompt. Du kannst also keine zweite
Konsole öffnen.

Es macht aber oft keinen Sinn, die Befehle für ein Programm jedes mal am
Befehlsprompt von neuem einzutippen. Für diesen Fall benutzen wir die oben
erstellte, neue Python-Datei. Dort kannst du mehrere Befehle hintereinander
aufschreiben um sie dann der Reihe nach ausführen zu lassen. So kannst du das Programm
später auch wieder öffnen, verändern oder erneut ausführen.

Um die Befehle auszuführen, kannst du auf das grüne Dreieck neben der ersten
Zeile des Programms klicken oder die `Shift` und `F10` Tasten zusammen drücken.

   
Aufgaben
========

1. Probiere die folgenden Befehle in der Python-Konsole aus und notiere dir,
   wozu sie benutzt werden.

   >>> 1 + 2 * 4

   >>> print("Hello World!")

   >>> sorted( [4,3,2,5,10,9] )

   >>> sum( [4,3,2,5,10,9] )

   >>> (4 + 3) / 5

   >>> (4 + 3) // 5


2. a) Erstelle, falls nicht schon erledigt, wie oben erklärt, eine neue Python-Datei. 
      Schreibe in dieser Datei die nötigen Befehle für ein "Hello
      World"-Programm. Falls du nicht weiter weisst, kannst du noch einmal den Anfang
      dieses Kapitels lesen.
   b) Das Programm kannst du mit den `Shift` und `F10` Tasten ausführen und testen. Wo wird der
      Text "Hello World" ausgegeben?

      
3. a) Speichere das folgende Programm in einer Python-Datei namens ``gui-beispiel.py``
      und führe es aus. Was macht das Programm?
   b) Welche Zeilen kannst du aus dem Programm löschen, ohne dass sich seine
      Funktionsweise ändert oder es nicht mehr funktioniert? 

   .. literalinclude:: code/CanvasExample.py
      :linenos:


.. _Emacs: https://www.gnu.org/software/emacs/
.. _Vi(m): http://www.vim.org/
.. _Atom: https://atom.io
.. _PyCharm: http://www.jetbrains.com/pycharm/
