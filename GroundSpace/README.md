# GroundSpace

Tiny program to fill your harddrive with characters of your choice.  
Initially some terminal-script, but I got the idea to play a bit around with PyQt for a pretty ui.  
And yes, it is usable. Learnt a lot.  
Qt for C++ is nice, but PyQt is really easy and fast to develop. :thumbsup:

## Prerequisites aka Pip

$ pip install PyQt5

## How to use?
* run the script
* this is how the ui looks:  
![screenshot of the current UI state](ui_currentState.png)
* set parameters for pattern, repetitions and click "Run"
* watch the progressbar moving to 100% :'D
* if the "repeat"-checkbox is checked, then the file-writing will be repeated (until unchecked or the disk is full)

## contact the author
mail@marcelpetrick.it

## planned ideas
* display the current writing-speed
* fix the bug that the run-button is not disabled after starting the process (multiple runs happens ..)
