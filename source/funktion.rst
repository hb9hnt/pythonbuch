*****************************
Funktionen als Unterprogramme
*****************************

In den vorherigen Kapiteln haben wir immer wieder auf Funktionen zurückgegriffen,
welche uns von Python zur Verfügung gestellt wurden. Wenn du beispielsweise den 
Befehl ``len("Haus")`` eingibst, bekommen wir von der Funktion 
:py:func:`len()` den *Rückgabewert* ``4`` zurück. Dieser Wert ändert sich 
natürlich, wenn ein anderes *Argument* als ``"Haus"`` der Funktion übergeben
wird.

In diesem Kapitel besprechen wir, wie man selber solche Funktionen definieren 
kann. Dies ist vorallem dann hilfreich, wenn man den gleichen Codeblock mehr
als einmal in einem Programm ausführen möchte. Schauen wir folgendes
Beispiel an:

.. literalinclude:: code/ohne-funktionen.py
   :linenos:
   :emphasize-lines: 3,4,8,9

Wir sehen, dass die zwei Codezeilen 

.. literalinclude:: code/ohne-funktionen.py
   :language: python
   :lines: 3,4

zweimal im Programm auftauchen. Dem können wir Abhilfe schaffen, indem wir eine
Funktion definieren, welche die Ausführung dieses Codeabschnitts übernimmt.


Eine Funktion ohne Rückgabewert definieren
==========================================

Mit dem Keyword :py:keyword:`def` führen wir nun eine neue Funktion ein. Nach 
der Anweisung :py:keyword:`def` steht der Name der Funktion, gefolgt von 
runden Klammern ``()``. In der Klammer ``()`` werden die *Argumente*, falls 
welche verlangt, aufgelistet. Zum Schluss kommt noch der obligate Doppelpunkt 
``:``. Die darauffolgende Zeilen müssen wie üblich eingerückt sein, ansonsten
gehören sie nicht mehr zur Funktion.

Auf unser Beispiel von oben angewendet, sieht unser Programm nun folgendermassen 
aus:

.. literalinclude:: code/mit-funktionen.py
   :linenos:
   :emphasize-lines: 2,3,7,9

Jedes Mal wenn im Programm die Funktion ``mit_zwei_multiplizieren()`` 
aufgerufen wird, wird der Codeblock bei der Definition der Funktion 
(in unserem Beispiel Zeile 2 und 3) ausgeführt.

Natürlich können der Funktion auch mehr als nur ein *Argument* übergeben werden.

.. literalinclude:: code/flaeche-rechteck.py
   :linenos:


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
eine Weiterverarbeitung zurückgeben, so kann dies mit der Anweisung 
:py:keyword:`return` gemacht werden:

.. literalinclude:: code/flaeche-rechteck-return.py
   :linenos:
   :emphasize-lines: 2

Nun kann das Ergebnis der Funktion :py:func:`flaeche_rechteck()` weiter 
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
         
         def print(zahl):
	     print("Hallo Welt")

   Definition 2:

   .. code-block:: python
         
         def print1(zahl)
	     print("Hallo Welt")
		   
   Definition 3:

   .. code-block:: python
         
         def print1(zahl):
	     print("Hallo Welt")

   Definition 4:

   .. code-block:: python
         
         def print(zahl):
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

.. rubric:: Footnotes
	  
.. [#] Das Binärsystem (auch Dualsystem genannt) ist ein Zahlensystem, welches 
       zur Darstellung von Zahlen nur zwei verschiedene Ziffern (0 und 1)
       benutzt. Jede Zahl kann somit nur mit Hilfe von 0 und 1 dargestellt
       werden. Für mehr Informationen siehe unter 

       http://de.wikipedia.org/wiki/Bin%C3%A4rzahl
