**********
Funktionen
**********

In den vorherigen Kapiteln haben wir immer wieder auf Funktionen zurückgegriffen,
welche uns von Python zur Verfügung gestellt wurden. Wenn du beispielsweise den 
Befehl ``len("Haus")`` eingibst, bekommen wir von der Funktion 
:py:func:`len` den *Rückgabewert* ``4`` zurück. Dieser Wert ändert sich 
natürlich, wenn ein anderes *Argument* als ``"Haus"`` der Funktion übergeben
wird.

In diesem Kapitel besprechen wir, 
wie man selber solche Funktionen definieren kann. 
Es gibt verschiedene Gründe, 
warum es Sinn macht Funktionen zu definieren.

	1. Mehrer hintereinander ausgeführte Anweisungen können unter einem 
	Namen zusammengefasst werden. 
	Es kann also als **Strukturierungselement** angesehen werden,
	das eine Menge von Anweisungen gruppiert. 
	
	2. Ein längeres Programm erhält durch Funktionen eine Struktur,
	welche helfen kann, den Code besser lesen und verstehen zu können.
	
	3. Ein Funktionsname kann dabei helfen zu 
	verstehen, was das Unterprogramm berechnet oder ausführt.
	
	4. Muss eine Codesequenz mehr als einmal ausgeführt werden,
	so braucht man nur den Funktionsnamen aufzurufen 
	(Vermeidung von Codeduplizität).
	
Betrachten wir das folgende Beispiel:

.. literalinclude:: code/einf-funktionen.py
	:linenos:

Es benötigt eine Weile um zu verstehen, was das Programm genau macht.
Bei genauerem Hinsehen sieht man, 
dass die paar Codezeilen aus zwei Hauptteilen besteht:
Zuerst wird eine zufällig, ganzzahlige Liste erstellt 
und danach deren arithmetischen Mittelwert berechnet. 

Lagern wir diese zwei Hauptteile in Funktionen mit geeigneten Namen aus,
so wird das Programm verständlicher zu lesen sein,
ohne sich um programmtechnische Details kümmern zu müssen:

.. literalinclude:: code/einf-funktionen2.py
	:linenos:
	:emphasize-lines: 19-21
	
Das Programm besteht nun wesentlich aus den Zeilen 19-21.
Nur das Lesen dieser 3 Zeilen reicht aus,
um zu verstehen, was das gesamte Programm macht.
Die Anweisungen für das Erstellen einer Zufallsliste 
und die Berechnung des arithmetischen Mittelwertes 
wurden in Funktionen ausgelagert (siehe Zeile 1-17).

Zusätzlich stehen die Möglichkeiten der beiden Funktionen zu jedem 
beliebigen Zeitpunkt später im Programm wieder zur Verfügung.
D.h. alleine durch den Funktionsaufruf 
:py:func:`zufallsliste_erstellen` kann jederzeit im Programm wieder eine
Zufallsliste erstellt werden, ohne die ganzen Anweisungen nochmals
aufschreiben zu müssen.

Betrachten wir nun im Detail, 
wie Funktionen in Python erstellt werden können.


Eine Funktion ohne Rückgabewert definieren
==========================================

Mit dem Keyword :py:keyword:`def` führen wir eine neue Funktion ein. Nach 
der Anweisung :py:keyword:`def` steht der Name der Funktion, gefolgt von 
runden Klammern ``()``. In der Klammer ``()`` werden die *Argumente*, falls 
welche verlangt, aufgelistet. Zum Schluss kommt noch der obligate Doppelpunkt 
``:``. Die darauffolgende Zeilen müssen wie üblich eingerückt sein, ansonsten
gehören sie nicht mehr zur Funktion.

Hier ein Beispiel einer Funktion,
welche eine Zahl als Übergabeparameter erwartet.
Die Funktion selber multipliziert die Eingabe mit 2 
und gibt das Resultat auf der Konsole wieder aus.

.. literalinclude:: code/mit-funktionen.py
   :linenos:
   :emphasize-lines: 1-3

Jedes Mal wenn im Programm die Funktion ``mit_zwei_multiplizieren()`` 
aufgerufen wird, wird der Codeblock bei der Definition der Funktion 
(in unserem Beispiel Zeile 2 und 3) ausgeführt.

Natürlich können der Funktion auch mehr als nur ein *Argument* übergeben werden.

.. literalinclude:: code/flaeche-rechteck.py
   :linenos:

Eine mögliche Ausgabe könnte dann folgendermassen aussehen:

>>> flaeche_rechteck(3,7)
Die Fläche des Rechtecks ist 21.
>>> flaeche_rechteck(2.3,5.1)
Die Fläche des Rechtecks ist 11.729999999999999.

Aufgaben
~~~~~~~~
1. Erstelle eine Funktion, welche einen String als *Argument* erwartet und 
   den ersten und letzten Buchstaben des Strings ausgibt.


2. Schreibe eine Funktion :py:func:`summe()`, welche für die Eingabe einer 
   Zahl :math:`n` folgendes Resultat ausgibt:

   .. math:: \text{summe} := 1 + 2 + \dots + n
   
   Es sollte dann z.B. folgendermassen aussehen:

   >>> summe(4)
   10
   >>> summe(100)
   5050

3. Definiere eine Funktion ``teilermenge(zahl)``, welche die Menge der
   Teiler von ``zahl`` ausgibt. Zum Beispiel:

   >>> teilermenge(24)
   [1, 2, 3, 4, 6, 8, 12, 24]


Eine Funktion mit Rückgabewert definieren
==========================================

Unsere selbst geschriebenen Funktionen von oben haben bisher die Resultate 
lediglich auf der Konsole ausgegeben. Jedoch kann es sein, dass die Ergebnisse 
für den weiteren Programmverlauf gebraucht und weiter verarbeitet werden müssen.
In solchen Fällen macht es Sinn Funktionen zu definieren, welche mir 
ein Ergebnis zurückgeben, wie z.B.

>>> len("Haus")
4

Nehmen wir das gleiche Beispiel von oben: 

.. literalinclude:: code/flaeche-rechteck.py
   :linenos:

Diese Funktion gibt auf der Konsole die Fläche des Rechtecks mit Längen 
``a`` und ``b`` aus. Möchte man das Ergebnis nicht ausgeben, sondern z.B. für
eine Weiterverarbeitung zurückgeben, so kann dies mit der :py:keyword:`return`
Anweisung gemacht werden:

.. literalinclude:: code/flaeche-rechteck-return.py
   :linenos:
   :emphasize-lines: 2

Nun kann das Ergebnis der Funktion :py:func:`flaeche_rechteck()` in 
einer Variable gespeichert und weiter 
verwendet werden.

>>> a = flaeche_rechteck(2,5)
>>> a
10

.. note:: Eine Funktion mit einem :py:keyword:`return` Statement kommt dem 
	  Konzept einer Funktion im Sinne der Mathematik sehr nahe:
	  
	  .. math::  y = f(x) 

	  wobei 

	  .. math::  \begin{array}{ll}  f: &\text{Funktionsname}\\
					x: &\text{Argument}\\
					y: &\text{Rückgabewert}
					\end{array}
 
  
Mehr zum Thema Funktionen findest du in der Dokumentation unter

https://docs.python.org/3.2/tutorial/controlflow.html#defining-functions


Aufgaben
~~~~~~~~

1. In den vorherigen Kapiteln hast du die Fakultät in den Aufgaben
   bereits kennengelernt.

   .. math:: n! := n \cdot (n-1) \cdot(n-2) \cdots 3 \cdot 2 \cdot 1

   a) Definiere eine Funktion ``fakultaet(zahl)``, welche die Fakultät von
      ``zahl`` berechnet und als Ergebnis zurückgibt. 

   b) Schreibe nun ein kleines Programm, welches zwei natürliche Zahlen einliest
      und jeweils deren Fakultät berechnet und ausgibt.

2. Schreibe eine Funktion ``quersumme(zahl)``, welche die Quersumme von 
   ``zahl`` berechnet und zurückgibt.


3. Schaue dir die folgende Funktion an und überlege, was das Ergebnis sein
   könnte.
   
   .. literalinclude:: code/meine-funktion.py
      :linenos:

   Hast du eine Vermutung? Teste sie an einigen Beispielen:

   >>> meine_funktion(12,16)
   >>> meine_funktion(1,16)
   >>> meine_funktion(8,16)
   >>> meine_funktion(8,21)
   >>> meine_funktion(18,21)
   >>> meine_funktion(27,36)


4. Welche der folgenden Definitionen sind zulässig? Welche nicht und wieso?
   Überlege zuerst und tippe es danach zur Kontrolle ein.

   Definition 1:
      
   .. code-block:: python
         
         def print():
	     print("Hallo Welt")

   Definition 2:

   .. code-block:: python
         
         def print1()
	     print("Hallo Welt")
		   
   Definition 3:

   .. code-block:: python
         
         def print1():
	     print("Hallo Welt")

   Definition 4:

   .. code-block:: python
         
         def print1():
	 print("Hallo Welt")


5. Schreibe zwei Funktionen mit folgender Funktionalität:

   a. ``dez_to_bin(dezzahl)``: Die Funktion wandelt die Dezimalzahl ``dezzahl``
      in die entsprechende Binärzahl um. [#]_

   b. ``bin_to_dez(binzahl)``: Die Funktion wandelt die Binärzahl ``binzahl``
      in die entsprechende Dezimalzahl um. 

   c. Teste deine beiden Funktionen indem du sie mit den von Python
      zur Verfügung gestellten Funktionen vergleichst (``bin()`` und ``int()``):
      
      .. code-block:: python

         # Konvertiert eine Dezimalzahl in eine Binärzahl
         >>> bin(24)
      	 '0b11000'
      
         # Konvertiert eine Binärzahl in eine Dezimalzahl
         >>> int('11000',2)
	 24

Mehrere Rückgabewerte
=====================

Bis jetzt haben unsere Funktionen immer nur einen Wert zurückgeben.
Mit Python ist es überhaupt kein Problem, 
auch Funktionen zu definieren, welche mehr als einen Wert zurückgeben.
Hier ein Beispiel dazu:

.. literalinclude:: code/funktionen-rueckgabewerte.py
   :linenos:

Dieses Programm gibt die Summe und das Produkt zweier 
Zahlen (hier ``zahl1`` und ``zahl2``) zurück.
Folgende  Ausgabe erhalten wir auf der Konsole:

.. code-block:: python

	(14, 40) 14 40
	14 40

Wir sehen bei der Zuweisung in Zeile 4, dass 
die mehreren Rückgabewerte als Tupel der einen Variable ``a`` 
übergeben werden. Man kann aber auch jeden Rückgabewert einer einzigen Variablen 
zuweisen, so wie es in Zeile 7 gemacht wurde.


``lambda``-Operator
===================

Der ``lambda``-Operator bietet eine Möglichkeit *anonyme Funktionen*, 
also Funktionen ohne Namen, zu schreiben und zu benutzen. 
Anstelle des Keywords :py:keyword:`def` gebrauchen wir das Keyword
:py:keyword:`lambda`. Sie können, wie *normal definierte Funktionen*,
eine beliebe Anzahl von Parametern haben, führen Befehle aus und können 
einen Rückgabewert liefern. 
Die Syntax sieht folgendermassen aus:

	.. code-block:: python

		lambda [arg1 [,arg2,.....argn]]:expression

Das nächste Beispiel zeigt den Unterschied zwischen einer *normalen Funktion* 
und einer *lambda Funktion*:

>>> def f(x): return x**2
>>> print(f(8))
64
>>> g = lambda x: x**2 
>>> print(g(8))
64

Wir sehen, dass die beiden Funktionen ``f`` und ``g`` genau das gleiche
ausführen und auf die gleiche Weise benutzt werden können.
Sie unterscheiden sich hier lediglich in der Definition.
Wie aber der Name (*anonyme Funktionen*) schon sagt, 
müssen wir einem ``lambda``-Ausdruck
keinen Namen zuweisen, was wir am folgenden Beispiel gut sehen:

>>> (lambda x: x**2)(8)
64

Der ``lambda``-Operator kann dann gut gebraucht werden,
wenn beispielsweise eine Funktion als Argument einer weiteren Funktion
übergeben werden soll
und man diese erste Funktion nachher nicht mehr braucht.
Schauen wir dazu folgendes Beispiel an:

	.. literalinclude:: code/lambda_fkt.py
    	  :linenos:

Diese Programm liefert dann folgenden Output:

	.. code-block:: python

		[42, 43, 44, 45, 46]

Nehmen wir an, dass die Funktion :py:func:`temp_funktion` 
in einem späteren Programmverlauf nie mehr gebraucht wird.
So können wir uns die Namensvergabe sparen und ändern denn Code 
folgendermassen:

	.. literalinclude:: code/lambda_fkt2.py
	    	  :linenos:

Dieses Programm hat den gleichen Output wie das erste, 
jedoch mussten wir nicht eine Funktion definieren, welche wir 
später sowieso nicht gebraucht hätten.

Aufgaben
~~~~~~~~

1. Welche der folgenden Eingaben sind zulässig? Welche nicht und wieso?
   Wie müsste es richtig sein?
   Überlege zuerst und tippe es danach zur Kontrolle ein.

	>>> a = lambda arg1, arg2: arg1 + arg2
	>>> print(a(0,2))

	>>> a = (lambda arg1, arg2: arg1 + arg2)(0,2)
	>>> print(a(0,2))

	>>> a = lambda arg1, arg2: arg1 + arg2
	>>> print(a(2+2))

	>>> a = lambda arg1, arg2: arg1 + arg2
	>>> b = lambda x: a(2, x)
	>>> print(b(3,4))

2. Gegeben ist folgendes Programm:

	.. literalinclude:: code/lambda_aufg.py
	    	  :linenos:

   Schreibe das Programm mit dem ``lambda``-Operator so um, dass
   die Zeilen 1-12 weggelassen werden können, jedoch der gleiche Output
   produziert wird.

.. rubric:: Footnotes
	  
.. [#] Das Binärsystem (auch Dualsystem genannt) ist ein Zahlensystem, welches 
       zur Darstellung von Zahlen nur zwei verschiedene Ziffern (0 und 1)
       benutzt. Jede Zahl kann somit nur mit Hilfe von 0 und 1 dargestellt
       werden. Für mehr Informationen siehe unter 

       http://de.wikipedia.org/wiki/Bin%C3%A4rzahl
