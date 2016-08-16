************************
Programmablauf-Steuerung
************************

Wie wir im vorangehenden Kapitel gelernt haben, wird ein Programm zweilenweise
von oben nach unten abgearbeitet. Nun gibt es Fälle, wo wir einen Programmblock
nur unter einer Bedingung ausführen oder einige Anweisung mehrmals
wiederholen wollen.

Es ist oft notwendig, einen ganzen Programmblock für jedes Element einer Liste
zu wiederholen. Dies ist eine Form der Iteration. Wir sprechen von einer
*Iteration über den Elementen einer Liste*. In Python wird dies mit einer
:py:keyword:`for` Schleife gemacht. [#]_ Wir werden in diesem Zusammenhang auch
lernen, wie in Python ein Programmblock gekennzeichnet wird.

In anderen Fällen ist es notwendig, zu entscheiden, ob ein Programmblock
ausgeführt werden soll oder nicht. Hier handelt es sich um eine Selektion. Dafür
müssen wir zuerst lernen, wie in Python Bedingungen formuliert
werden. Anschliessend betrachten wir die :py:keyword:`if` Verzweigung, welche
uns das bedingte Ausführen eines Programmblocks ermöglicht.

Teilweise reicht diese sehr spezielle Form der Wiederholung nicht. Es kann auch
notwendig sein, einen Block zu wiederholen, bis eine Bedingung nicht mehr wahr
ist. Dies nennen wir eine *bedingte Iteration*.

Die :py:keyword:`for` Schleife
==============================

Wie schon erwähnt, ist die :py:keyword:`for` Schleife ein Sezialfall der
Iteration, nämlich eine Iteration über einer Liste. Man kann alle Probleme,
welche mit :py:keyword:`for` gelöst werden können, auch mit der später
besprochenen, allgemeineren :py:keyword:`while` Schleife lösen. Das Iterieren
über einer Liste ist aber eine so häufige Form der Iteration, dass
:py:keyword:`for` häufiger vorkommt als :py:keyword:`while`.

Wir wollen ein erstes Beispiel einer solchen Schleife in Python betrachten:

.. literalinclude:: code/for.py
   :linenos:
  

Hier nimmt die Variable ``zahl`` jeden Wert aus der Liste einmal an und
durchläuft alle Anweisungen innerhalb der Iteration. Sobald Python beim letzten
Element in der Liste angelangt ist, bricht die Schleife ab und es wird bei der
ersten Anweisung nach der Schleife weitergefahren.

In diesem Fall gehörten zwei Anweisungen zum Programmblock, welcher wiederholt
wird, nämlich die Berechnung der Variable ``summe`` sowie die Ausgabe mit
:py:func:`print()`. Diese Anweisung wurde nach innen gerückt, um Python
mitzuteilen, dass sie zu der Schleife gehört.

Wenn du in IDLE den Doppelpunkt am Ende der Zeile nach der Liste nicht vergisst,
rückt IDLE die nächste Zeile automatisch ein. Andernfalls kannst du dies mit der
<TAB>-Taste selbst machen. Achte darauf, dass wirklich alle Zeilen, welche zum
gleichen Block gehören, gleich stark eingerückt sind. Schon nur ein Leerzeichen
unterschied wird zu einer Fehlermeldung führen. [#]_

Möchte man nun zum Beispiel etwas für die Zahlen von 1 bis 100 ausführen, wird
es mühsam, die Liste von Hand wie oben einzutippen. Dafür gibt es in Python den
Befehl :py:func:`range()`. So enthält ``range(100)`` alle Zahlen von 0
bis 99 (also insgesamt 100 Zahlen) und ``range(1, 101)`` alle Zahlen von 1
bis 100.

.. note:: Die letzte Zahl, welche wir dem :py:func:`range` Befehl übergeben,
	  wird aus dem Bereich ausgeschlossen. Will man alle Zahlen bis 100,
	  muss man als Ende des Bereichs 101 angeben. Der Anfang ist jedoch
	  enthalten. Gibt man 1 als Anfang an, so ist auch die 1 noch im Bereich
	  enthalten.

Mit :py:func:`list` kannst du solche Bereiche in wirkliche Listen konvertieren,
um an der Python-Konsole zu betrachten, wie sie aussehen:

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Einen Bereich können wir nun wie folgt benutzen, um zum Beispiel alle Zahlen von
0 bis 99 aufzulisten.

.. literalinclude:: code/for-range.py
   :linenos:

Aufgaben
~~~~~~~~

1. Gegeben ist der folgende Anfang eines Programms::

     animals = ["tiger", "mouse", "bird", "python", "elephant", "monkey"]
     # ...

   Ergänze das Programm so, dass für jedes Tier aus der Liste ``animals`` der
   Satz "... ist ein Tier" in der Konsole ausgegeben wird. Benutze dafür die
   :py:func:`print` Funktion.

2. Mit :py:meth:`append` kannst du einer Liste ein Element hinten anfügen.
   Schreibe ein Programm, welches den Benutzer mit :py:func:`input` fünf mal
   nach einem Wort fragt und alle diese Worte in einer Liste
   abspeichert. Anschliessend werden alle Worte aus der Liste mit
   :py:func:`print` zurückgegeben.

    *Erweiterung*: Frage den Benutzer zuerst, wie viele Worte er eingeben will
    und frage dann genau so viel mal nach einem Wort.

    
3. In der Mathematik gibt es die Schreibweise
  
   .. math:: n! := n \cdot (n-1) \cdot(n-2) \cdots 3 \cdot 2 \cdot 1

  So wird zum Beispiel :math:`5!` durch :math:`5\cdot 4\cdot3\cdot2\cdot1 = 120`
  berechnet. Dies wird in der Mathematik als *Fakult�t von 5* bezeichnet.

  Schreibe ein Programm welches :math:`n!` für ein vom Benutzer vorgegebenes
  :math:`n` berechnet. Benutze dafür eine :py:keyword:`for` Schleife.


4. Schreibe ein Programm, welches die folgende Ausgabe bis zu einer vom Benutzer
   gewählten Zahl fortsetzt::
  
     1*
     2**
     3***
     4****
     5*****
     6******
     7*******
     ...


   *Zusatz*: Passe das Programm so an, dass es einen Weihnachtsbaum aus Sternchen
   zeichnet, dessen Höhe vom Benutzer gewählt werden kann.

5. Passe das in einer früheren Aufgabe erweiterte Notenprogramm so an,dass
   der Benutzer wählen kann, wie viele Noten er eingeben möchte. 


Die :py:keyword:`if` Verzweigung
================================

Wie oben erklärt, kommt es vor, dass wir einen Programmblock nur unter einer
Bedingung ausführen wollen. Falls die Bedingung nicht erfüllt ist, führen wir
entweder nichts oder einen anderen Block aus.

.. literalinclude:: code/if-else.py
   :linenos:
   :emphasize-lines: 3,5
      
Mit dem Wort :py:keyword:`if` wird eine Bedingung abgefragt. In diesem Fall ist
dies die Frage, ob die als ``antwort`` gespeicherte Zeichenkette in der Liste
enthalten ist oder nicht. (Dieses Enthalten-Sein wird mit dem Wort
:py:keyword:`in` überprüft.)

Der Programmblock, welcher nach dem Wort :py:keyword:`else` folgt, wird
ausgeführt, falls die Bedingung oben falsch ist. Die wichtigen Zeilen sind also
die Zeilen

.. literalinclude:: code/if-else.py
   :language: python
   :lines: 3

und
	   
.. literalinclude:: code/if-else.py
   :language: python
   :lines: 5

Achte auch hier darauf, wie die :py:func:`print` Befehle eingerückt wurden, um
Python mitzuteilen, welche Zeilen zu den Blöcken gehören, welche nur bedingt
ausgeführt werden sollen.
	   
Aufgaben
~~~~~~~~

1. Für Vergleiche, ob etwas grösser oder kleiner ist, können die in der
   Mathematik üblichen Zeichen ``<`` und ``>`` benutzt werden. Schreibe ein
   Programm, welches die folgenden Schritte ausführt:

   i)   Es wird vom Benutzer per :py:func:`input` eine Zahl eingelesen.
   ii)	Es wird geprüft, ob die Zahl grösser oder kleiner als 10 ist.
   iii) Mit dem Befehl :py:func:`print` wird entsprechend entweder "Die Zahl
	ist grösser als 10" oder "Die Zahl ist kleiner als 10" ausgegeben.

2. Ob ein Jahr im Gregorianischen Kalender ein Schaltjahr ist, kann nach den
   folgenden Regeln entschieden werden:

   * Jahre sind Schaltjahre, falls ihre Jahrzahl durch 400 teilbar ist.
   * Jahre sind Schaltjahre, falls ihre Jahrzahl durch 4 teilbar ist, ausser die
     Jahrzahl ist durch 100 teilbar.  

   Schreibe ein Programm, welches den Benutzer nach einer Jahreszahl fragt und
   anschliessend prüft, ob es sich um ein Schaltjahr handelt.

Die :py:keyword:`while`-Schleife
================================

Es gibt Fälle, wo eine :py:keyword:`for` Schleife nicht ausreicht, weil wir
keine Liste von Elementen haben und auch nicht zu Beginn wissen, wie oft etwas
ausgeführt werden soll.

Man könnte sich zum Beispiel vorstellen, dass wir in einem Programm dem Benutzer
eine Frage gestellt haben, welche mit "Ja" oder "Nein" zu beantworten ist. Wenn
der Benutzer nicht entweder ``J`` für Ja oder ``N`` für Nein eingibt, ist die
Eingabe ungültig und wir müssen nochmals nachfragen. Dies würde in Python wie
folgt umgesetzt:

.. literalinclude:: code/while.py
   :linenos:
   :emphasize-lines: 4-5

Der markierte Codeblock wird so lange wiederholt, wie die Bedingung ``antwort
not in ['j', 'J', 'n', 'N']`` wahr ist. Das heisst, so lange die Antwort nicht
in der Liste mit gültigen Antworten enthalten ist.

Aufgaben
~~~~~~~~

1. Schreibe ein Programm, welches alle Zahlen von 1 bis 100 auf den Bildschirm
   schreibt, ohne dafür eine :py:keyword:`for` Schleife zu verwenden.

2. Aus dem Kapitel über die :py:keyword:`for` Schleife kennst du das folgende
   Beispielprogramm:

   .. literalinclude:: code/for.py
      :linenos:

   Schreibe das Programm so um, dass es eine :py:keyword:`while` Schleife
   anstelle der :py:keyword:`for` Schleife benutzt.

3. Die Folge aus Fibonacci-Zahlen wird wie folgt gebildet:

   * Das erste und das zweite Element sind 0 und 1.
   * Jedes folgende Element wird gebildet, in dem die letzten zwei Elemente
     addiert werden. 

   Das heisst, die Folge sieht so aus: :math:`0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
   \cdots`

   Schreibe ein Programm, welches die Fibonacci-Zahlen bis zu einer vom Benutzer
   gewählten Zahl ausgibt.

4. Schreibe ein Programm, welches mit :py:func:`input` zwei Zahlen vom Benutzer
   einliest und den grössten gemeinsamen Teiler der beiden Zahlen mit
   :py:func:`print` ausgibt.

   Dazu kannst du den Euklidschen Algorithmus benutzen, welchen du entweder aus
   dem Mathematikunterricht kennst oder sonst sicher im Internet findest.

.. rubric:: Footnotes

.. [#] Falls du schon andere Programmiersprachen kennst, kann es sein, dass dich
       die :py:keyword:`for` Schleife in Python zuerst verwirrt. Sie ist nicht
       gleich aufgebaut wie etwa in C++ oder Java.
   
.. [#] Dies ist einer der Nachteile von Python. Andere Sprachen benutzen
       geschweifte Klammern { und } um zusammengehörende Blöcke zu
       kennzeichnen. 
