**************************
Vektorgeometrie mit Python
**************************
:Python: |*| |*| |o| |o| |o|
:Informatik: |*| |*| |o| |o| |o|
:Mathematik: |*| |*| |*| |*| |o| 

:Python-Module: :py:mod:`math` ,  :py:mod:`Matplotlib`

.. :py:mod:`numpy`, :py:mod:`scipy`,

Im folgenden Projekt ist das Ziel, möglichst viele Funktionen des im Unterricht
benutzten grossen Taschenrechners durch Python zu ersetzen. Dabei wirst du dich
hauptsächlich (aber nicht ausschliesslich) mit Vektorgeometrie beschäftigen. Ziel
ist es, die folgenden Fragen ausgiebig zu untersuchen:

* Wie können Vektorrechnungen mit Python durchgeführt werden?

* Wie kann das Vektor- und das Skalarprodukt mit Python berechnet werden?

* Wie können mit Python Funktionsgraphen und Graphiken für die Vektorgeometrie
  dargestellt werden?

		
Aufträge
========

1. Erstelle eine kurzes Dokument, welches erklärt, wie man mit Python
   die Funktionen eines einfachen Taschenrechners benutzen kann. Halte
   dich dabei an die von dir oft benutzten Funktionen des
   TI-30. Benutze wo n"otig Funktionen aus dem :py:mod:`math` Packet.

2. In diesem Punkt geht es darum, die Hilfsmittel zu erstellen, welche
   du f"ur das Arbeiten mit Vektoren brauchst. Du hast zwei
   M"oglichkeiten, dies zu tun. W"hle die zweite, falls du mit Klassen und Objekten
   umgehen kannst.

   * Vektorem kannst du in Python als Listen mit zwei oder drei
     Fliesskomma-Zahlen abspeichern. Schreibe Funktionen, welche f"ur
     Vektoren die L"ange, die Addition, die Skalarmultiplikation sowie
     das Skalar- und das Vektorprodukt berechnen. Der folgende Code
     sollte mit Hilfe deiner Funktionen ausf"uhrbar sein:

     >>> vnorm([3,-3,7])
     TODO

     >>> vmultiplikation(-3, [1,2,-3])
     [-3, -6, 9]

     >>> vaddition( [1, -3, 2], [2, 3, -5] )
     [3, 0, -3]


     >>> vdotp( [1, -3, 2], [2, 3, -5])
     -17

     >>> vcrossp( [1, 5, 4], [2, -3, 0] )
     [12, 8, 7] 

   * F"ur Bonuspunkte kannst du eine Klasse ``Vektor`` schreiben,
     welche Funktionen f"ur die im ersten Punkt erw"hnten
     Vektoroperationen als Methoden besitzt. Der folgende Code sollte
     mit deiner Klassendefinition funktionieren:

     >>> v1 = vektor( 3, -3, 7 )
     >>> v2 = vektor( 2, -1, 3 )
     >>> v1.norm()
     TODO
     >>> v1.add(v2)
     TODO
     >>> v2.multiply(3)
     ( 6, -3, 9 ) 
     >>> v1.dotp(v2)
     TODO
     >>> v1.crossp(v2)
     TODO

     Als erweiterung k"onntest du deine Klasse so ausbauen, dass auch
     die folgenden Operationen unterst"utzt werden:

     >>> v1 + v1
     TODO
     >>> 3 * v1
     TODO


.. 2. Erstelle eine Dokumentation, welche beschreibt, wie du die folgenden
   Vektoroperationen mit Hilfe von :py:mod:`numpy` durchführst:

   * Zusammenhängen von Vektoren: Addition
   * Verlängern und verkürzen von Vektoren: Skalarmultiplikation
   * Die Länge eines Vektors berechnen und Normieren eines Vektors
   * Skalar- und Vektorprodukt

3. Wähle aus den Vektorgeometrie-Aufgaben einige, möglichst unterschiedliche aus
   und löse sie mit Python.
     
4. Erstelle eine Dokumentation für das Erstellen von Funktionsgraphen und
   vektorgeometrischen Sachverhalten mit Hilfe von :py:mod:`Matplotlib`.

Dokumente
=========

Die folgenden Dokumente sollten am Ende der Arbeit am Projekt abgegeben werden:

* Arbeitsjournal
* Auflistung der Befehle eines TI-30 in Python.
* Gut kommentierter Quellcode von deinen Vektor-Funktionen oder deiner
  Vektor-Klasse.
* Musterlösungen von Vektorgeometrie-Aufgaben in Python, wo du deine
  eigene Klasse benutzt.
* Dokumentation zum Erstellen von Funktionsgraphen.


Dokumentations-Links
====================

.. http://www.numpy.org/

http://matplotlib.org/

.. http://www.scipy.org/


	     
.. |*| image:: /images/star-full.png
.. |o| image:: /images/star-empty.png
			      
