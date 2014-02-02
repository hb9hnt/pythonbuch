**********************
Erste Programmelemente
**********************

Kommentare
==========

Kommentarzeilen in Programmen sind Zeilen, welche vom Computer nicht beachtet
werden. In allen Programmiersprachen beginnen diese Zeilen mit einem bestimmten
Zeichen. Zeilen, welche mit dem Zeichen ``#``, werden von Python als Kommentare
betrachtet und ignoriert. Steht das Zeichen ``#`` nicht am Anfang einer Zeile,
wird nur der Teil auf der Zeile ignoriert, welcher nach dem Zeichen kommt.

**Beispiel:**

.. code-block:: python
   :linenos:
  
   # Dies ist eine Kommentarzeile, welche ignoriert wird

   print("Hallo!") # Die Zeile wird erst ab hier ignoriert.


Nun fragt man sich was denn der Sinn hinter Zeilen ist, welche von Python gar
nicht beachtet werden. Diese erfüllen sehr wichtige Funktionen

* Sie dienen dazu, dass andere Personen deine Programme einfacher lesen und
  verstehen können.
* Sie helfen dir, ein Programm oder einen Programmabschnitt zu planen.

Wenn du zum Beispiel ein Programm schreiben möchtest, welches den Benutzer nach
zwei Zahlen fragt, diese addiert und dann die Summe auf dem Bildschirm ausgibt,
kannst du dieses Programm schon planen ohne eine Ahnung zu haben, wie die
einzelnen Schritte funktionieren.

Dazu schreibst du das folgende Programm:

.. code-block:: python
   :linenos:
   
   ###########################################
   ##                                       ##
   ## Programm zur Addition von zwei Zahlen ##
   ##                                       ##
   ###########################################
   
   # Benutzer nach zwei Zahlen einlesen
   
   # Die erhaltenen Zahlen addieren

   # Die Summe auf dem Bildschirm ausgeben

Wenn du Python dieses Programm ausführen lässt, passiert natürlich erst einmal
gar nichts. Es besteht ja nur aus Zeilen, welche von Python nicht beachtet
werden. Doch du hast nun eine ziemlich genaue Vorstellung, was du in welcher
Reihenfolge du das Programm schreiben willst. Sobald du gelernt hast, wie man
dies tut, kannst du die entsprechenden Blöcke zwischen die Kommentare
programmieren.

Beachte zum schreiben von Kommentaren folgende Regeln:

* Schreibe am *Anfang* des Programms einen ausführlicheren Kommentar
  darüber, was das Programm tut.

* Schreibe zu jedem *logisch zusammengehörenden* Block einen Kommentar, der
  erklärt, was dieser Programmblock tut. Fällt dir keine passende beschreibung
  dazu ein, besteht die Möglichkeit, dass der Block nicht tut, was du möchtest
  oder er gar überflüssig ist.

* Schreibe zu jeder *Variable* kurze Erklärung, wozu sie benutzt wird. Fällt dir
  keine gute Erklärung ein brauchst du die entsprechende Variable vermutlich
  nicht. (Was Variablen sind lernst du gleich im nächsten Abschnitt)


Variablen
=========

Variablen in Python werden genau wie in jeder anderen Programmiersprache zum
Abspeichern oder Zwischenspeichern von Werten (Zahlen, Text, Listen usw.)
benutzt.

In Python stellt man sich Variablen jedoch besser als Namensschilder vor, welche
man einem Objekt gibt. Wenn du zum Beispiel eine Zwischenergebnis einer Rechnung
hast, gibst du ihm einen Namen, welcher erklärt, um was es sich handelt. In
diesem Fall ist vermutlich der Name ``Zwischenergebnis`` angebracht.

Die Anhängen eines Namensschildes wird in Python mit ``=`` ausgedrückt. Auf der
linken Seite des Gleichzeichens steht der neue Name und auf der rechten Seite
das Objekt, welches den Namen erhalten soll. Probiere foldenden Code in der
Python Konsole aus:

>>> zwischenergebnis = 3.14111222
>>> zwischenergebnis
3.13111222

Wie du siehst steht der Name ``zwischenergebnis`` jetzt für die Zahl
``3.1411222``.

Die Wahl des Zeichens ``=`` ist aus Mathematischer Sicht ungünstig. In der
Mathematik hat das Zeichen eine andere Bedeutung. Es sagt einfach, dass zwei
Sachen gleich sind. Dabei spielt es aber keine Rolle, was links und was rechts
des Gleichzeichens steht.

Mathematisch gesehen ist der folgende Ausdruck eine Gleichung ohne Lösung:

.. math:: x = x + 1

In Python macht es aber durchaus Sinn, die Befehlsabfolge

>>> x = 4
>>> x = x + 1
>>> x
5

auszuführen. Es wir nämlich einfach der Wert der Variable um eins erhöht.


Aufgaben
========

1. Im folgenden werden einige Zeilen Programmcode ausprobiert. Überlege dir, was
   nach dem Ausführen der Zeilen in den Variabeln ``erste_zahl``,
   ``zweite_zahl`` und ``temp`` gespeichert ist. Wozu dient der kurze
   Programm-Ausschnitt?

   >>> erste_zahl = 7
   >>> zweite_zahl = 9
   >>> temp = erste_zahl
   >>> erste_zahl = zweite_zahl
   >>> zweite_zahl = temp


2. a) Probiere im Befehlsprompt die folgenden Variablennamen aus, in dem du eine
      beliebige Zahl abspeicherst: ``zahl2``, ``Zahl2``, ``Zahl 2``, ``2zahl``,
      ``zahl.2``, ``Zahl_2``, ``2_Zahl``, ``_Zahl2``, ``2_Zahl``. Welche
      Variablennamen sind zulässig. 
   b) Finde an Hand der obigen Beispielen und der Python-Dokumentation heraus,
      wie die Regeln für zulässige Variablennamen lauten.

