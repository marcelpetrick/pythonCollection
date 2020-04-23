# Marcel's Game of Life

Of course, this will be just an implementation of Conway's Game of Life.
I have to say, I never implemented in my whole life this cellular automat fully. Some tries were done in Java, but never finished.
So, let's use the current situation (#covid19) and just do a SW-based project. Afar from Euler and ESP32.

Description [ https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life ]


Rules: [ https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens ]

Die von Conway zu Anfang verwendeten Regeln sind:

* Eine tote Zelle mit genau drei lebenden Nachbarn wird in der Folgegeneration neu geboren.
* Lebende Zellen mit weniger als zwei lebenden Nachbarn sterben in der Folgegeneration an Einsamkeit.
* Eine lebende Zelle mit zwei oder drei lebenden Nachbarn bleibt in der Folgegeneration am Leben.
* Lebende Zellen mit mehr als drei lebenden Nachbarn sterben in der Folgegeneration an Überbevölkerung.
	