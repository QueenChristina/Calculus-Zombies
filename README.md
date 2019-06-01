# Calculus-Zombies
Memorize derivatives and integrals quickly through this game of survival against zombies!
<br> Light review of calculus and motivation included! ;)
Watch the demo here: https://youtu.be/Qs85VhzvFdc
(No sound in game because I don't know how to make game sounds).
<br>
[![Watch the video by clicking](https://media.giphy.com/media/ehD18hACYhlruHKVqN/giphy.gif)](https://youtu.be/Qs85VhzvFdc)
<br>
All visuals and code except for "InputText.py" is made by me.
"InputText.py" is Copyright 2017, by Silas Gyger, silasgyger@gmail.com, All rights reserved.
Borrowed from https://github.com/Nearoo/pygame-text-input under the MIT license.

# Download
Download here: https://drive.google.com/drive/folders/10hjFlAXVXCrB8waCYXZwyMx4AA_lFjn7?usp=sharing
Or download the folder "Calculus Zombie".
Double click on "CalcZom" to play. Do not move the folders/files around; relative paths need to stay the same.

# Notes
I need help figuring out how to convert my game into a .exe. So far I figured out how to edit the .spec and then turn into .exe file using https://stackoverflow.com/questions/38977929/pyinstaller-creating-exe-runtimeerror-maximum-recursion-depth-exceeded-while-ca . But when run, it was missing python36.dll so I downloaded from https://wikidll.com/python-software-foundation/python36-dll and unzipped it in the same file location (I'm using Python 3.6, 32 bit, on Windows). It worked better, but now says missing "encodings" module. I believe problem now is something to do with Python PATH and HOME environment variables, but I am not allowed to change these on the current computer without being an "advanced user" or "administrator". Basically, I risk ruining the whole computer due to my lack of experience. So now I'm trying this on another laptop (which my parents say are okay to mess up on) but it's even worse; it has Python 3.7 installed. More errors. I'm trying my best to figure this out...
Currently using for help: https://stackoverflow.com/questions/38132755/importerror-no-module-named-encodings
Alternative to editing environment variables is just copying and pasting the whole python lib into CalcZom game folder, but it looks messy and is not effifcient. Managed to get rid of "No module names 'x'" error, but now throws a different error. Worse, doing this confuses my game's python files location and causes it to crash.
<br>
<br> <br>

# INSTRUCTIONS
My current game (as of 5-28-19): https://drive.google.com/drive/folders/10hjFlAXVXCrB8waCYXZwyMx4AA_lFjn7?usp=sharing
<br> Feel free to download. <br>
It will work if you have Python 3, pygame, sympy installed. You can download these by following instructions as follows:
https://www.python.org/downloads/ <br>
https://www.pygame.org/wiki/GettingStarted <br>
https://github.com/sympy/sympy/wiki/release-notes-for-1.4 <br>
<br>
It's best to install pygame and sympy modules via your command prompt.
<br>
If pip is not recognized, make sure pip has been downloaded: https://pip.pypa.io/en/stable/installing/ or https://phoenixnap.com/kb/install-pip-windows but it should be included automatically if you have python version 3.4 or up. It can be updated via: python -m pip install -U pip OR py -m pip install -U pip on windows.
<br> Please note, you may have python downloaded under python OR py. <br>
Use https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command for help.
For me, these worked: <br> py -m pip install -U sympy <br>
py -m pip install -U pygame  <br>
<br> and to test if this works: py -m pygame.examples.aliens <br>

![Progress 5-13-19 Title Screen](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Pretty.gif)

![Progress 5-13-19 Lesson](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Class.gif)

![Progress 5-13-19 Calculator](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Calc.gif)

<br><br><br><br>

![Progress 5-8-19 Losing](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-8-19/5-8-10%20Fail.gif)
