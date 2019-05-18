# Calculus-Zombies
Memorize derivatives and integrals quickly through this game of survival against zombies!
<br> Work in progress!
<br> Follow this project to keep updated. Will add visuals and fun soon. ;)
<br> <br>
I need help figuring out how to convert my game into a .exe. So far I figured out how to edit the .spec and then turn into .exe file using https://stackoverflow.com/questions/38977929/pyinstaller-creating-exe-runtimeerror-maximum-recursion-depth-exceeded-while-ca . But when run, it was missing python36.dll so I downloaded from https://wikidll.com/python-software-foundation/python36-dll and unzipped it in the same file location (I'm using Python 3.6, 32 bit, on Windows). It worked better, but now says missing "encodings" module. I believe problem now is something to do with Python PATH and HOME environment variables, but I am not allowed to change these on the current computer without being an "advanced user" or "administrator". Basically, I risk ruining the whole computer due to my lack of experience. So now I'm trying this on another laptop (which my parents say are okay to mess up on) but it's even worse; it has Python 3.7 installed. More errors. I'm trying my best to figure this out...
Currently using for help: https://stackoverflow.com/questions/38132755/importerror-no-module-named-encodings
Alternative to editing environment variables is just copying and pasting the whole python lib into CalcZom game folder, but it looks messy and is not effifcient. Managed to get rid of "No module names 'x'" error, but no throws a different error.
<br>
<br> <br>
# INSTRUCTIONS
My current game so far (5-16-19): https://drive.google.com/drive/folders/1opm-mpPOUyF7GuO_jQIfRz_qJ7vWR5WS?usp=sharing
<br> Feel free to download. <br>
It will work if you have Python 3, pygame, sympy installed. You can download these by following instructions as follows:
https://www.python.org/downloads/ <br>
https://www.pygame.org/wiki/GettingStarted <br>
https://github.com/sympy/sympy/wiki/release-notes-for-1.4 <br>
<br>
It's best to install pygame and sympy modules via your command prompt.
<br>
If pip is not recognized, use https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command for help OR try py -m pip install -U symp. <br>

![Progress 5-13-19 Title Screen](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Pretty.gif)

![Progress 5-13-19 Lesson](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Class.gif)

![Progress 5-13-19 Calculator](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-13-19/5-13-19%20Calc.gif)

<br><br><br><br>

![Progress 5-8-19 Losing](https://github.com/QueenChristina/Calculus-Zombies/blob/master/5-8-19/5-8-10%20Fail.gif)
