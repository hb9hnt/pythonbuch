************************
Programmablauf-Steuerung
************************

Wie wir im vorangehenden Kapitel gelernt haben, wird ein Programm zeilenweise
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

Wie schon erwähnt, ist die :py:keyword:`for` Schleife ein Spezialfall der
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

Wenn du in PyCharm den Doppelpunkt am Ende der Zeile nach der Liste nicht
vergisst, rückt PyCharm die nächste Zeile automatisch ein. Andernfalls kannst du
dies mit der <TAB>-Taste selbst machen. Achte darauf, dass wirklich alle Zeilen,
welche zum gleichen Block gehören, gleich stark eingerückt sind. Schon nur ein
Leerzeichen unterschied wird zu einer Fehlermeldung führen. [#]_

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
  berechnet. Dies wird in der Mathematik als *Fakultät von 5* bezeichnet.

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

2. Schreibe ein Programm, welches vom Benutzer 10 Zahlen einliest und diese in
   einer Liste speichert. Anschliessend soll das Minimum und das Maximum der
   Zahlen aus der liste bestimmt und ausgegeben werden.

3. Ob ein Jahr im Gregorianischen Kalender ein Schaltjahr ist, kann nach den
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

Die :py:keyword:`while` Schleife wird solange ausfeführt wie eine Bedinung wahr
ist. Sie hat die folgende Struktur::

  while Bedingung:
      Befehl 1
      Befehl 2 

   Befehl 3

Dabei werden die Befehle 1 und 2 solange ausgeführt, wie die Bedingung wahr
(also :py:keyword:`true`) ist. Sobald die Bedinung falsche (:py:keyword:`false`)
wird, springt Python zur nächsten nicht eingerückten Zeile, also Befehl 3. Zur
Formulierung der Bedingung können dieselben Formen wie bei der :py:keyword:`if`
Abfrage benutzt werden.
  
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

4. Der Wert einer Immobilie steigt jedes Jahr um :math:`p` Prozent an. Schreibe
   ein Programm, welche den Zeitwert dieser Immobilie so lange berechnet, bis
   der Zeitwert (mehr als) doppelt so gross ist wie der heutige
   Anfangswert. Frag den Benutzer nach dem Prozentsatz.

5. Eine Firma kauft eine Maschine (der Einkaufspreis ist einzugeben), welche
   innert einiger Jahre (die Anzahl Jahre ist einzugeben) linear abgeschrieben
   wird.

   *Beispieleingabe*::
     20000 (Fr. Einkaufspreis), 5 (Jahre)

   *Beispielausgabe*::
     Jahr 1: 16000.00
     Jahr 2: 12000.00
     Jahr 3: 8000.00
     Jahr 4: 4000.00
     Jahr 5: 0.00

6. Herr Spar legt sich jedes Jahr einen festen Betrag (z.B. 800.00 Fr.) auf sein
   Konto, welches beispielsweise :math:`2.5%` Zins trägt. Er tut dies so lange,
   bis er einen bestimmten Betrag überschreitet. Dieser Betrag ist auch
   einzugeben, z.B. 5000.00. Schreibe dazu ein Programm.

7. Ein Gegenstand hat den Wert :math:`k` (dieser Wert ist Ein gabe). Erstelle
   ein Programm, welche für die nächsten Jahre (die Anzahl Jahre ist Eingab
   ewert) den Zeitwert dieses Gegenstands berechnet, wenn jedes Jahr :math:`p`
   Prozent des Wert s abgeschrieben werden.  (Der Abschreibungssatz :math:`p`
   ist auch einzugeben.)  Diese Art Abschreibung heisst degressive Abschreibung.

8. Wie lange muss man einen Würfel werfen, bis (zum ersten Mal) eine 6
   erscheint? Schreibe ein Programm, welches so lange würfelt, :math:`b` is eine 6
   erschienen ist.

   *Eingabe*: keine

   *Ausgabe*: alle geworfenen Zahlen und die Anzahl Würfe.
 
9. Ein Würfel wird so lange geworfen, bis die Summe aller Würfe 100 oder mehr
   beträgt. Zum simulieren eines Würfels kannst du die Funktion
   :py:func:`randrange` aus dem Modul :py:module:`random` benutzen.

   a) Bestimme mit einem Programm, wie viele Würfe dazu nötig sind.

   b) Schreibe ein Programm, welches mit Hilfe einer Liste zählt, wie oft welche
      Augenzahl geworfen wurde. Am Ende soll die Liste mit :py:func:`print`
      ausgegeben werden.

   c) Ändere das Programm so ab, dass so lange gewürfelt wird, bis zum ersten
      Mal eine Zahl 50 Mal geworfen wurde. Gib an, wie oft die anderen Zahlen
      geworfen wurden.

10. Der Computer "würfelt" eine Zufallszahl zwischen 1 und 6 (Grenzen inklusive).
    Der Spieler versucht nun, die gewürfelte Zahl zu erraten. Bestimme mit einem
    Programm, wie viele Versuche dazu nötig sind.
   
  
11. Schreibe ein Programm, welches mit :py:func:`input` zwei Zahlen vom Benutzer
    einliest und den grössten gemeinsamen Teiler der beiden Zahlen mit
    :py:func:`print` ausgibt.

    Dazu kannst du den Euklidischen Algorithmus benutzen, welchen du entweder aus
    dem Mathematikunterricht kennst oder sonst sicher im Internet findest.

.. rubric:: Footnotes

.. [#] Falls du schon andere Programmiersprachen kennst, kann es sein, dass dich
       die :py:keyword:`for` Schleife in Python zuerst verwirrt. Sie ist nicht
       gleich aufgebaut wie etwa in C++ oder Java.
   
.. [#] Dies ist einer der Nachteile von Python. Andere Sprachen benutzen
       geschweifte Klammern { und } um zusammengehörende Blöcke zu
       kennzeichnen. 

Kombinieren von Kontrollstrukturen
==================================

Wie du sicherlich schon festgestellt hast, kommt man nie mit einer einzelnen
Kontrollstruktur aus, die meisten Problemstellungen benötigen ein geschicktes
Kombinieren von :py:keyword:`if`, :py:keyword:`for` und
:py:keyword:`while`. Dazu kommt meistens noch die Wahl einer Datenstruktur:
Macht es Sinn, einzelne Variablen zu benutzen oder ist etwa eine Liste
geeigneter? Halte dich beim Programmieren an folgende Grundsätze:

* Nummeriere keine Variablen. Wenn du in deinem Programm etwa Variablen-Namen
  ``x_wert_1``, ``x_wert_2`` und ``x_wert_3`` hast, ist dies ein Hinweis darauf, dass
  du vermutlich besser eine Liste verwenden würdest.

* Benutze wenn immer möglich ein :py:keyword:`elif`, wenn du mehrere
  :py:keyword:`if`-Abfragen hintereinander ausführst.
 
* Natürlich gilt weiterhin: Schreibe am besten zuerst die Kommentare für dein
  Programm und dann den Programmcode. Falls du dies lieber nicht machst, achte
  auf jeden Fall darauf, dass du jeden logisch zusammenhängenden Programmblock
  mit einem oder mehreren `#`-Kommentarzeilen erklärst.

Löse die folgenden Aufgaben unter Beachtung der genannten Grundsätze.

Aufgaben
~~~~~~~~

#. Schreibe ein Programm, welches den Benutzer mit Hilfe von :py:func:`input`
   nach einem Satz fragt. 


   a) Das Programm soll anschliessend die Anzahl Worte im Satz sowie die Anzahl
      Buchstaben ausgeben.

   b) Erweitere das Programm so, dass es auch angibt, wie viele Buchstaben davon
      Grossbuchstaben sind.

#. Schreibe ein Programm, welches den Benutzer nach einer Zahl fragt und
   anschliessend prüft, ob diese Zahl eine Primzahl ist. 

#. Schreibe ein Programm, welches alle Primzahlen zwischen 1 und einer vom
   Benutzer gewählten oberen Grenze ausgibt.

   *Zusatzaufgabe*: Versuche im Internet herauszufinden, wie man dieses Problem
   möglichst effizient (d.h. so, dass es wenig Zeit braucht) löst und schreibe
   dein Programm um, damit es schneller wird.  

#. Im Zahlenlotto werden sechs Zahlen aus 49 zufällig ausgewählt, wobei keine
   doppelt vorkommen darf. Schreibe ein Programm, welches 6 Zahlen aus 49
   zufällig wählt. Verwende dafür wiederum Funktionen aus dem
   :py:module:`random` Modul.

   a) Benutze ausschliesslich die :py:func:`randrange` Funktion, um dies zu
      erreichen.

   b) Lies die Dokumentation des :py:module:`random` Moduls und versuche jene
      Funktion zu finden, mit welcher du die Aufgabe am einfachsten lösten
      kannst. (Das heisst mit möglichst wenig Programmcode)

#. Das Collatz-Problem gehört zu den ungelösten Problemen der Mathematik. _[#]
   Es besagt, dass jede Abfolge von Zahlen, welche nach der folgenden Regel
   gebildet wird, irgendwann bei der Zahl 1 landet:

   * Die Folge beginnt bei einer beliebigen Zahl.
   
   * Ist die momentane Zahl :math:`n` gerade, so ist die nächste Zahl die Hälfte von
     dieser, also :math:`\frac{n}{2}`.

   * Ist die momentane Zahl :math:`n` ungerade, so ist die nächste Zahl um eins grösser
     als das dreifache der Zahl, also :math:`3n+1`.

   Bilden wir beispielsweise für die Zahl :math:`23` diese Folge, so lautet sie:

   .. math:: 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

   Schreibe ein Programm, welches diese Folge für eine vom Benutzer gewählte
   Zahl ausgibt und mit der Berechnung stoppt, sobald 1 erreicht wurde.

#. Schreibe ein Programm, welches eine Liste von Zahlen sortiert und gib das
   Ergebnis in der Konsole aus. Für die Liste ``[1,4,3,3,5,7,2]`` sollte das
   Ergebnis die Liste ``[1,2,3,3,4,5,7]`` sein.

   a) Speichere die Liste in der ersten Zeile als Variable ab und sortiere sie
      anschliessend.

   b) Frage den Benutzer nach der Liste von Zahlen. Überlege dir, wie du es am
      besten lösen kannst, dass der Benutzer eine vorher nicht bekannte Anzahl
      Zahlen eingeben kann.
   
#. |star| Schreibe ein Programm, welches eine Liste von vom Benutzer
   eingegebenen Worten alphabetisch sortiert. Der Benutzer gibt etwa die
   Worte *Zweck*, *schneiden*, *Granit*, *Gewinn*, *Schubkarre* und *entflammen*
   ein und dein Programm gibt folgendes aus::

     entflammen
     Gewinn
     Granit
     schneiden
     Schubkarre
     Zweck

#. |star| Schreibe ein Programm, welches den Benutzer nach einem oder mehreren
   deutschen Sätzen fragt. Anschliessend verändert das Programm den Text so, dass
   bei jedem Wort der erste und der letzte Buchstabe stehen gelassen werden und
   alle Buchstaben dazwischen jeweils wie Jasskarten gemischt werden. Das
   heisst, dass keine Buchstaben dazu kommen und auch keine entfernt werden,
   jedoch die Reihenfolge verändert wird. Gib anschliessend den so entstandenen
   Text aus. Was stellst du fest?


.. |star| unicode:: 0x2605


.. rubric:: Footnotes

.. [#] https://de.wikipedia.org/wiki/Collatz-Problem
