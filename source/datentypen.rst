****************
Erste Datentypen
****************

Zahlen
======

Python kann verschiedene Arten von Zahlen darstellen und speichern. Wir werden
uns hier auf die Zahlen beschränken, welche in der Programmierung oft
benutzt werden. Dies sind ganze Zahlen und Fliesskommazahlen. Python kann auch
mit Brüchen, komplexen Zahlen oder Dezimalzahlen mit einer festen Anzahl
Dezimalstellen rechnen. Diese werden wir aber hier nicht genauer anschauen.

Integer : Ganze Zahlen
  Ganze Zahlen sind sowohl negative als auch positive Zahlen ohne
  Nachkommastellen. Mit diesen kann Python sehr gut umgehen. Im Gegensatz zu
  anderen Programmiersprachen sind sie in der Grösse nicht eingeschränkt. Ihr
  könnt beliebig grosse ganze Zahlen speichern. [#]_

Float : Fliesskommazahlen
  Fliesskommazahlen gibt es in den meisten Programmiersprachen. Sie werden
  benutzt, um Dezimalzahlen zu speichern. Die Arbeit mit Fliesskommazahlen bietet
  aber auch einiges an Stolpersteinen. Vor allem wenn die Zahlen betragsmässig
  sehr gross werden oder sehr nahe bei 0 liegen, kann es Probleme mit der
  Genauigkeit geben - wie wir weiter unten selbst beobachten werden.

Die folgenden Zahlen sind in Python alle zulässig. Sobald ein Punkt,
ein ``e`` oder ein ``E`` vorkommt werden sie als Fliesskommazahl interpretiert::

  # Ganze Zahlen (Integer)
  0
  12
  1220200399948882888338278
  -5
  -11692013098647223345629478661730264157247460343808

  # Fliesskommazahlen (Float)
  0.0
  23.0
  0.234
  -1e-1
  12E4

Eine kurze Erklärung braucht der Buchstabe ``e`` oder ``E``. Beide Schreibweisen
stehen für das gleiche und sind dir vielleicht schon vom Taschenrechner
bekannt. Es handelt sich dabei um die wissenschaftliche Schreibweise von Zahlen
mit Zehnerpotenzen. So steht zum Beispiel ``1.2E4`` für :math:`1.2\cdot 10^{4}`
oder ``-1e-1`` für :math:`-1\cdot 10^{-1}`. 

.. seealso::

   Brüche :
     Das Modul :py:mod:`fractions` unterstützt auch Bruchrechnen. Falls man
     präzise und ausschliesslich mit rationalen Zahlen rechnet, können damit die
     Probleme der Fliesskommazahlen umgangen werden.

   Dezimalzahlen:
     Das Modul :py:mod:`decimal` kann zum präziseren - jedoch langsameren -
     Rechnen mit Dezimalzahlen benutzt werden.

  
Aufgaben
~~~~~~~~

1. Probiere die unten stehenden Operatoren mit verschiedenen Zahlen aus und
   notiere dir, was sie tun. Setze für ``x`` und ``y`` verschiedene Zahlen ein,
   bis du herausgefunden hast, was die Operatoren tun.

   >>> x + y

   >>> x - y

   >>> x % y

   >>> -x

   >>> x * y

   >>> x / y

   >>> x**y

   >>> x // y
   
2. Was ist der Rückgabewert des unten stehenden Programms? Gehe es zuerst im Kopf
   durch und probiere es anschliessend aus, in dem du das Programm mit IDLE in
   einer neuen Datei abspeicherst.

   .. code-block:: python
      :linenos:
      
      x = 2
      y = 3
      z = x + y
      x = z
      y = x
      print(x)
      print(y)
      print(z)

3. Probiere die folgenden Rechnungen am Python-Prompt aus. Welches Ergebis
   erwartest du? Woran liegt es, dass du nicht das erwartete Ergebnis erhältst?

   >>> 0.1 + 0.1 + 0.1 - 0.3

   >>> 5 + 10**40 - 10**40

   >>> 5.0 + 10**40 - 10**40

4. Angenommen, du hast pro Semester vier Prüfungen in einem Fach. Nun sind drei
   dieser Prüfungen vorbei und du möchtest wissen, welche Note du in der vierten
   Prüfung haben musst, um deinen Wunschschnitt zu erreichen.

   Schreibe ein Programm, welches dir diese Frage beantwortet. Benutze vier
   Variablen um die drei Noten und den Wunsch-Durchschnitt abzuspeichern und
   lasse das Programm daraus die letzte Note berechnen, welche du brauchst, um
   den Wunsch-Durchschnitt zu erreichen. Diese kannst du mit dem
   :py:func:`print()` Befehl ausgeben.


Zeichenketten
=============

Beim Programmieren möchte man nicht nur mit Zahlen arbeiten. Man möchte auch
Text abspeichern können, um dem Benutzer etwas mitzuteilen oder um den Text zu
verarbeiten.

Diesen Datentyp nennt man Zeichenketten oder auf englisch *String*. Er wird so
genannt, weil wir nicht nur Text darin abspeichern können, sondern beliebige
Zeichen wie Satzzeichen, Zahlen. Sogar Leerschläge, Tabulatoren und
Zeilenumbrüche werden vom Computer als Zeichen behandelt.

Wir haben zwei Möglichkeiten Zeichenketten in Python darzustellen. So kann der
String "Hallo Welt" wie folgt dargestellt und z.B. in einer Variable
abgespeichert werden::

  'Hallo Welt'
  "Hallo Welt" 

Dies dient dazu, dass auch ein String, welcher ``'`` oder ``"`` enthält,
ausgedrückt werden kann::

  'Eine Zeichenkette, welche "Anführungszeichen" enthält'

Teilweise haben wir Zeichenketten, welche auch Zahlen darstellen können. So ist
zum Beispiel ``'2.73'`` eine Fliesskommazahl oder ``'42'`` eine ganze
Zahl. Python kann damit jedoch nicht rechnen, da alles zwischen Anführungs- und
Schlusszeichen nur als Abfolge von Zeichen interpretiert wird.

In diesem Fall müssen wir die Zeichenketten in Zahlen konvertieren. Dies
geschieht mit dem :py:func:`float()` Befehl für Fliesskommazahlen respektive mit dem
:py:func:`int()` Befehl für Integer.

>>> int('42') # Dies gibt die Zahl ohne Anführungszeichen zurück
42
>>> float('23.22') # Dies gibt eine Fliesskommazahl zurück
23.22

Haben wir hingegen eine Zahl, können wir mit dem Befehl :py:func:`str()` daraus
eine Zeichenkette machen.

>>> str(7)
'7'
>>> str(2.5)
'2.5'

Dies funktioniert unabhängig davon, ob es sich um eine ganze Zahl oder eine
Fliesskommazahl handelt.

Aufgaben
~~~~~~~~

1. Probiere die Operationen mit verschiedenen Strings in der Pythonkonsole aus
   und notiere dir, was der entsprechende Befehlt tut. Speichere dafür zuerst
   unter den Variablen ``string_eins`` und ``string_zwei`` zwei
   Zeichenketten, zum Beispiel so:

   >>> string_eins = "Hallo schöne, neue Welt"
   >>> string_zwei = "Hallo Mars, ich bin ein Marsroboter"

   Probiere nun die folgenden Befehle aus. Setze im folgenden Befehlanstelle der
   Zahl ``3`` auch andere Zahlen ein.

   >>> string_eins[3]

   >>> string_eins.capitalize()

   >>> string_eins.lower()

   Probiere die folgenden zwei Befehle auch mit anderen Buchstaben anstelle von
   ``'e'`` aus.

   >>> string_eins.count('e')

   >>> string_eins.find('e')

   >>> string_eins + string_zwei


   Weitere Befehle um mit Strings zu arbeiten findest du hier:

   http://docs.python.org/release/3.1.5/library/stdtypes.html#string-methods


2. Benutzereingaben: Das folgende Programm liest eine Eingabe vom Benutzer ein
   und speichert dies in der Variable ``eingabe``. Der Befehl :py:func:`input()`
   liest immer Zeichenketten -- nicht etwa Zahlen -- ein.

   .. code-block:: python
      :linenos:
      
      eingabe = input("Gib einen Text ein: ")
		   
      # Ab hier kann das Programm nun den in der Variable eingabe
      # gespeicherten Text benutzen ...

   Erweitere das Programm so, dass auch die folgenden Schritte ausgeführt
   werden:
		   
   * Der erste Buchstabe der Benutzereingabe wird in Grossbuchstaben
     konvertiert.
   * Dem Text wird ein Ausrufezeichen angehängt.
   * Ergebnis wird mit :py:func:`print()` auf dem Bildschirm ausgegeben.


3. Erkläre den Unterschied der folgenden Code-Zeilen. Was passiert hier? Kann
   Python nicht rechnen oder gibt es für dieses Verhalten eine Erklärung?

   >>> '23' + '7'
   '237'
   >>> 23 + 7
   30

4. Schreibe ein Programm, welches vom Benutzer zwei ganze Zahlen einliest und
   anschliessend die Summe der beiden Zahlen ausgibt.


Listen
======

Oft reichen Integer, Float und String Datentypen nicht aus, um die notwendigen
Daten zu speichern. Meist wissen wir nämlich im Voraus nicht, wie viele Datensätze
gespeichert werden sollen. Wenn du dich an die Aufgabe zur Berechnung der Noten
zurückerinnerst, sind wir davon ausgegangen, dass du im Semester vier grosse
Prüfungen hast. Dies ist aber natürlich von Fach zu Fach verschieden, und es
wäre vorteilhaft, wenn unser Programm eine im Voraus unbekannte Anzahl Noten
speichern könnte.

Python bietet für solche Problemstellungen verschiedene Datentypen. Die
einfachste Struktur sind die Listen, welche wir in diesem Kapitel genauer
anschauen wollen. [#]_

In Python können in einer Liste beliebige Datentypen gemischt gespeichert
werden - es können sogar Listen in Listen gespeichert werden. Eine Liste beginnt
mit einer geöffneten, eckigen Klammer ``[``. Anschliessend werden die Elemente
mit Kommas getrennt aufgelistet. Am Schluss wird die Liste wieder mit ``]``
geschlossen. 

Dies ist ein Beispiel einer Liste:

>>> liste = [3, 'King Arthur', ['Rabbit', 3.4], 2.44]

Auf die einzelnen Elemente der Liste kann anschliessend genau wie bei
Zeichenketten über die Nummer des Elements in eckigen Klammern zugegriffen
werden. Die Elemente werden auch hier, wie bei den Strings, ab 0 nummeriert.

>>> liste[0]
3
>>> liste[1]
'King Arthur'
>>> liste[2]
['Rabbit', 3.4]

Falls wir Listen geschachtelt haben - also als Element einer Liste wieder eine
Liste gespeichert, können wir mehrere eckige Klammern hintereinander setzen, um
auf die einzelnen Elemente zuzugreifen.

Im obigen Beispiel ist an der Stelle 2 eine Liste gespeichert. Um auf die
Elemente zuzugreifen, müssen wir in den ersten eckigen Klammern angeben, dass
wir die Liste an Stelle 2 meinen und in den zweiten eckigen Klammern geben wir
dann an, welches Element in der Unterliste wir herausholen möchten:

>>> liste[2][0]
'Rabbit'
>>> liste[2][1]
3.4

Die eckigen Klammern können auch benutzt werden, um einen Wert in einer Liste zu
überschreiben. Wir benutzen den Ausdruck, welcher auf ein Element zugreift
(z.B. ``liste[1]``) genau wie eine Variable, unter der wir mit ``=`` einen Wert
speichern:

>>> liste
[3, 'King Arthur', ['Rabbit', 3.4], 2.44, 4]
>>> liste[0] = 11  # An der Stelle 0 wird nun 11 gespeichert.
>>> liste
[11, 'King Arthur', ['Rabbit', 3.4], 2.44, 4]

Wie bei anderen Datentypen haben Listen in Python viele nützliche Methoden. In
den Aufgaben unten findest du wiederum eine Aufgabe, bei der du solche Methoden
ausprobieren kannst.

Eine vollständige Auflistung findest du auch hier in der Dokumentation unter

http://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Aufgaben
~~~~~~~~

1. Speichere die Elemente ``'Schwalbe'``, ``'Kokosnuss'``, ``13``, ``'Spam'``
   und ``3.14`` in einer Liste mit dem Namen ``liste`` ab und versuche
   herauszufinden, was die folgenden Methoden machen.

   >>> liste[2] = 666 

   >>> len(liste)

   >>> liste.append('Ni')

   >>> liste.extend([4, 5, 3.14])

   >>> liste.insert(2, 'Taube')

   >>> liste.count(3.14)

   >>> liste.index(3.14) 

   >>> liste.remove(3.14)

   >>> liste.pop()

   >>> liste.reverse()

   >>> sum([1,3,5])

2. Lies das folgende Programm und versuche zu erraten, was die Ausgabe
   ist. Probiere es anschliessend aus und suche nach einer Erklärung des
   Verhaltens.
  
   .. literalinclude:: code/list-pointer-example.py
      :linenos:
  
   Das Verhalten dieses Programms ist der Grund, warum wir uns in Python
   Variablen nicht als Speicherplätze sondern als Namensschilder für Objekte
   vorstellen. Kannst du dies erklären?

3. In einer früheren Aufgabe hast du ein Programm erstellt, welches eine
   feste Anzahl Noten einliest und anschliessend die notwendige Berechnung
   macht. Wir möchten dieses Programm nun anpassen, so dass die Noten in
   einer Liste gespeichert werden.

   Dies hilft uns dann im nächsten Kapitel, dass wir eine beliebige, vom
   Benutzer wählbare, Anzahl Noten speichern können.

   
.. rubric:: Footnotes
	  
.. [#] Dies ist natürlich nur theoretisch korrekt. Der Arbeitspeicher deines
       Computers ist beschränkt. Das heisst, wenn dieser voll ist, kann die Zahl
       nicht mehr grösser werden. Aber um den Arbeitspreicher heutiger Rechner
       zu füllen, braucht es unvorstellbar grosse Zahlen.

.. [#] Weiter gibt es noch Key-Value Speicher, welche in Python "Dictionaries"
       heissen. Oder auch Mengen und Tupel im mathematischen Sinn.

