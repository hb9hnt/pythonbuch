******************
Boolsche Ausdrücke
******************

Sowohl die :py:keyword:`if` Verzweigung sowie die :py:keyword:`while` Schleife
beötigen eine Bedingung. Im folgenden Kapitel wollen wir etwas genauer
analysieren, wie solche Bedingungen formuliert werden könne.
    
Ein *boolscher Ausdruck* ist ein Ausdruck, der entweder *wahr* oder
*falsch* ist, in Python :py:data:`True` und :py:data:`False`
genannt. Dies sind auch gleich die einfachsten boolschen Ausdrücke.

True:
  Dieser Ausdruck ist immer wahr. 

False:
  Dieser Ausdruck ist immer falsch.


Vergleiche
==========

Wir können zwei Variablen ``var_1`` und ``var_2`` miteinander vergleichen, falls
in beiden derselbe Datentyp gespeichert ist. Wenn verschiedene Datentypen
gespeichert sind, werden die Werte immer als ungleich betrachtet. Es existieren
die folgenden Vergleiche:

==================  ==================================
Vergleich           Bedeutung
------------------  ----------------------------------
``var_1 == var_2``  ``var_1`` gleich ``var_2`` 
``var_1 > var_2``   ``var_1`` grösser als ``var_2``
``var_1 >= var_2``  ``var_1`` grösser gleich ``var_2``  
``var_1 < var_2``   ``var_1`` kleiner als ``var_2``  
``var_1 <= var_2``  ``var_1`` kleiner gleich ``var_2`` 
``var_1 != var_2``  ``var_1`` ungleich ``var_2`` 
==================  ==================================

Boolsche Operatoren
===================

Mit boolschen Operatoren können verschiedene boolsche Ausdrücke verkettet oder
verneint werden. So können komplizierte Bedinungen wie "Ist A gleich B oder B
gleich D" formuliert werden. Es gibt die folgenden Operatoren:

:py:keyword:`not`:
    Kehrt den Wahrheitswert eines Ausdrucks um. Der Operator macht das selbe wie
    das deutsche Wort *nicht*.

:py:keyword:`and`:
    Ist wahr, wenn die Ausdrücke links und rechts des Operators wahr sind. Es
    handelt sich um eine *und* Verknüpfung.

:py:keyword:`or`:
    Ist wahr, wenn der Ausdruck links oder der Ausdruck rechts des Operators wahr
    ist. Es ist auch wahr, wenn beide wahr sind. Es handelt sich um eine *oder*
    Verknüpfung.

*Beispiel:*

>>> 4 == 4 or 4 == 5
True

Dieses Beispiel ist wahr, da 4 entweder gleich 4 oder gleich 5 ist. Hingegen ist
das Ergebnis falsch, wenn man dieselbe Frage mit einem *und* stellt:

>>> 4 == 4 and 4 == 5
False

Denn 4 kann nicht gleich 4 und gleich 5 sein. Da 4 nicht gleich 5 ist, ist aber
die Frage danach, ob *4 nicht gleich 4* sei wahr:

>>> not 4 == 5
True

Aufgaben
~~~~~~~~
1. Entscheide für jede Codezeile, ob der Boolsche Ausdruck wahr oder falsch
   ist, ohne das Beispiel in die Python-Konsole einzugeben. Prüfge deine Antwort
   anschliessend mit der Konsole.

   >>> 3 > 4

   >>> "Hallo Welt" > "Hallo"

   >>> 4 != 5

   >>> "Hallo" == "Hallo Welt"

   >>> "Hallo Welt" > "Hallo" and 3 > 4

   >>> "Hallo Welt" > "Hallo" or 3 > 4

   >>> not "Hallo Welt" >= "Hallo Welt"

   >>> not not 5 == 5

   >>> not 3 >= 4 and not 4 >= 5

2. Das folgende Programm benutzt zwei geschachtelte :py:keyword:`if`
   Verzweigungen. Schreibe das Programm um, so dass es mit einer einzelnen
   Verzweigung auskommt:

   .. literalinclude:: code/bool-and.py
      :linenos:


3. Schreibe ein Programm, welches prüft, ob ein Jahr ein Schaltjahr ist oder
   nicht. Verwende dabei im Gegensatz zum letzten solchen Programm nur genau
   eine :py:keyword:`if` Verzweigung.
