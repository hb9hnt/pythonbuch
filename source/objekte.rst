*******************
Objekte und Klassen
*******************

Je grösser ein Programm wird, desto wichtiger ist es Ordnung zu halten.
Eine Konzept, um die Übersicht besser zu behalten, ist die *Modularisierung*. 
Das heisst, dass wir unser Programm in einzelne, kleinere Komponenten 
aufteilen. Im Kapitel zu `Funktionen <./funktion.html>`_ haben wir bereits eine 
mögliche Variante der *Modularisierung* gesehen, indem die Ausführung 
von gewissen Codezeilen einer Funktion übergeben wurde.

In diesem Kapitel beschäftigen wir uns mit Objekten und Klassen [#]_. Die Idee 
dahinter ist, dass unsere Welt aus Objekten besteht, wie z.B. Personen, Autos,
Bäume, Häuser, Länder, Werkzeuge und Schuhe. Jedes dieser Objekte hat
bestimmte Charakteristiken und kann andere Objekte beeinflussen.
Dies ist eine sehr intuitive Beschreibung des Konzepts der obejektorientierten 
Programmierung. Im folgenden sehen wir anhand einiger Beispiele  eine konkrete 
Umsetzung in unserer Programmiersprache.


Klassen definieren und Objekte erstellen
========================================
Gehen wir von einem Programm aus, welches Informationen über Personen verwaltet.
Jede einzelne Person kann im Programm durch ein *Objekt* repräsentiert werden. 
Ein solches Objekt kann somit eine vereinfachte 
Kopie einer Person aus der realen Welt darstellen. 
Mit dem Keyword :py:keyword:`class` kann nun eine Klasse
definiert werden, welche mir Objekte von dieser Klasse generieren.
Die einfachste Weise dies zu machen, sieht folgendermassen aus:

.. literalinclude:: code/oop/einf_klasse_pass.py
   :linenos:

Nun können Objekte (Instanzen) der Klasse :py:class:`Person` erstellt werden.

>>> p1 = Person()
>>> p1
<__main__.Person object at 0x33c9210>

Man sieht das ``p1`` nun eine Instanz der Klasse :py:func:`Person` ist. 
Es könnten theoretisch noch viele weitere Instanzen unserer Klasse
:py:func:`Person` erstellt werden.


Instanzvariablen
================

Jede Person ist auf seine Art einzigartig und besitzt
gewisse Eigenschaften (z.B. Name, Vorname, Geburtsdatum und Körpergewicht).
Diese Variablen, welche wir nur innerhalb der Person ``p1`` definieren
wollen, können wir auf folgende Art erstellen:

>>> p1.name = "Müller"
>>> p1.vorname = "Kurt"
>>> p1.geb_datum = "03.02.01"
>>> p1.gewicht = "73.5 kg"

Variblen welche zu einem Objekt gehören, werden **Instanzvariablen** genannt.
Möchte man nun z.B. den ``namen`` und den ``vornamen`` der Person ``p1`` wissen,
so kann dieser mittels ``p1.name`` (bzw. ``p1.vorname``) abgefragt werden.

>>> print(p1.name, p1.vorname)
Müller Kurt

Eine Eingabe in der Konsole wie z.B.

>>> print(name, vorname)

wird nicht den Namen "Müller Kurt" unserer gewünschten Person ``p1``  ausgeben,
da diese nur im Namensbereich unseres Objektes  ``p1`` existieren.

Einer Instanz kann man beliebige Variablenamen zuordnen. 
Jedoch sollten sie schon irgendwie Sinn machen, weil es sonst 
im weiteren Programmverlauf nur
zur Verwirrung führt.

.. note:: Die Instanzvariablen, welche wir hier erstellt haben
          ( ``name``, ``vorname``, ``geb_datum`` und ``gewicht``)
	  charakterisieren die Instanz ``p1`` der Klasse :py:class:`Person`.
	  Diese helfen verschiedene Instanzen der gleichen Klasse zu
	  unterscheiden.
	  Später werden wir auch noch **Klassenvariablen** sehen, 
          welche nicht ein Objekt, sondern die Klasse selbst beschreibt.


Die :py:func:`__init__()` Methode
=================================
Von oben ist eigentlich klar, dass es vielleicht keinen Sinn macht,
Personen ohne Identität (sprich ohne Instanzvariablen) herzustellen. 
Es wäre also nur logisch, 
wenn man bei der Herstellung eines ``Objekts``, die Instanzvariablen,
welche man auf sicher haben möchte, von Anfang 
an definieren könnte. 
In unserem Beispiel würde das heissen, dass wir der Person
gleich bei der Herstellung eine Identität geben.
Dies kann man machen, wenn in der Klasse die Funktion :py:func:`__init__()` 
existiert. Die Funktion :py:func:`__init__()` wird immer dann aufgerufen,
wenn neue Objekte der Klasse instanziert werden 
(z.B. ``per = Person(...)``). [#]_
Die gewünschte Belegung der Instanzvariblen können 
der Funktion :py:func:`__init__()` einfach als Argumente übergeben werden. 
Auf unser Beispiel von oben angewandt, sieht es dann so aus:

.. literalinclude:: code/oop/einf_klasse_init.py
   :linenos:
   :lines: 1-9

Auf diese Weise kann keine Person ohne Identität erstellt werden und
man kann sicherstellen, dass die geforderten Instanzvariablen (hier
``name``, ``vorname``, ``geb_datum`` und ``gewicht``) auch sicher existieren.
Erstellen wir nun eine neue Person: 

>>> p2 = Person("Smith", "John", "04.04.04", "83 kg")
>>> print(p2.name, p2.vorname, p2.geb_datum, p2.gewicht)
Smith John 04.04.04 83 kg

Die Person ``p2`` wurde instanziert und die geforderten Instanzvariablen 
sind garantiert belegt.

.. note:: Das erste Argument ``self`` bei :py:func:`__init__()`
          steht als Vertreter für das Objekt.
	  Auf diese Weise ist z.B. die Zuordnung in der Klasse :py:class:`Person` 
		
	  .. literalinclude:: code/oop/einf_klasse_init.py
   	     :lines: 6

	  unmissverständlich. Das heisst ``self.name`` steht für die 
	  Instanzvariable des Objekts, welches erstellt wird und ``name`` 
	  steht für das Argument welches der Funktion :py:func:`__init__()`
	  übergeben wird. Natürlich kann man die Argumente auch anders
	  benennen. Jedoch sollte klar ersichtlich sein, welches Argument 
          zu welcher Instanzvariable gehört.


Klassenmethoden
================
Menschen sind nicht nur Träger von Merkmalen (Name, Vorname etc.), sondern 
besitzen auch ein Verhalten (z.B. "sich Vorstellen" oder "Gewicht abnehmen").
Solche Verhaltensweisen können in Methoden/Funktionen innerhalb der Klasse 
definiert werden. Von oben haben wir gesehen, dass wir mit 


>>> print(p2.name, p2.vorname, p2.geb_datum, p2.gewicht)
Smith John 04.04.04 83 kg


auf die Instanzvariablen des Objekts zugreifen können. Jetzt möchte man aber 
nicht immer einen solch langen ``print``-Befehl eingeben, 
sondern das Objekt (hier eine Person) soll sich gleich selber vorstellen.
Dies kann auf folgende Weise innerhalb der Klasse :py:class:`Person`
realisiert werden:


	.. literalinclude:: code/oop/einf_klasse_init.py
   	   :linenos:
	   :lines: 1-18


Mit dieser Methode bekommen wir, ohne viel Tipparbeit, gleich die Informationen
der jeweiligen Personen, indem sie sich selber vorstellt.
Wenden wir die Methode :py:func:`vorstellen` auf die beiden Personen 
``p1`` und ``p2`` von oben an:


>>> p1.vorstellen()
Hallo.
Ich heisse Kurt Müller, wiege 73.5 kg und habe am 03.02.01 Geburtstag.
Nice to meet you.
>>> p2.vorstellen()
Hallo.
Ich heisse John Smith, wiege 83 kg und habe am 04.04.04 Geburtstag.
Nice to meet you.


Hier sehen wir, dass die Funktion :py:func:`vorstellen`, je nach Objekt
auf welches es angewandt wird, eine andere Ausgabe in der Konsolo produziert.
Das ist auch wünschenswert, denn jedes Objekt (hier jede Person) hat andere
Eigenschaften (z.B. Name und Gewicht) 
und stellt sich dementsprechend auch anders vor.

Nun kann eine Person sich nicht nur vorstellen, sondern sie kann auch 
Gewicht verlieren, z.B. wenn sie Sport getrieben hat.
Ein solches Verhalten können wir ebenfalls in der Klasse mit einer Funktion
:py:func:`abnehmen` simulieren:

	.. literalinclude:: code/oop/einf_klasse_init.py
   	   :linenos:

Anders als die Funktion :py:func:`vorstellen` (welche nur Informationen 
auswirft) verändert die Funktion
:py:func:`abnehmen` das Objekt, indem es die Instanzvariable ``gewicht``
des Objektes anpasst.
Dessen muss man sich immer Bewusst sein. 
Ist die gewünschte Änderung des Objektes wirklich im Sinne meines Programms?

>>> p1.gewicht
'73.5 kg'
>>> p1.abnehmen(3)
Altes Gewicht: 73.5 kg
Neues Gewicht: 70.5 kg
>>> p1.gewicht
'70.5 kg'

Das obige Beispiel zeigt, dass das Objekt (hier die Person ``p1``),
nach dem Aufruf der Funktion :py:func:`abnehmen`, verändert wurde.


.. note:: Die Instanzvariablen der Klasse :py:class:`Person` 
          (``name``, ``vorname``, ``geb_datum`` und ``gewicht``) 
          sowie die Klassenmethoden 
	  (:py:func:`vorstellen` und  :py:func:`abnehmen`) sind nur Objekten
	  derselben Klasse vorbehalten.
	  Eine Eingabe wie
		
 	  >>> a = 1
	  >>> a.vorstellen()
          
	  wird eine Fehlermeldung produzieren, da ``a`` hier ein Integer ist
	  und somit die Funktion :py:func:`vorstellen` als Integer nicht kennt.


.. rubric:: Footnotes
	  
.. [#] Die Verwendung von Objekten und Klassen wird *objektorientierte 
       Programmierung* (kurz *OOP*) genannt. Für eine umfassende Beschreibung
       siehe unter http://openbook.galileocomputing.de/oop/ nach.

.. [#] Diejenigen die vielleicht mal in Java programmiert haben, 
       könnten meinen, dass es sich bei :py:func:`__init__()` um einen
       Konstruktor handelt. Jedoch ist die Sache in Python etwas anders.
       Der eigentliche Konstruktor wird implizit von Python gestartet 
       und :py:func:`__init__()` dient, 
       wie der Name andeutet der Initialisierung der Attribute. 
       Die :py:func:`__init__()`-Methode wird jedoch unmittelbar 
       nach dem eigentlichen Konstruktor gestartet 
       und dadurch entsteht der Eindruck, 
       als handele es sich um einen Konstruktor.
