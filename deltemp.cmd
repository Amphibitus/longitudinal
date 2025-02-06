set laufwerk=%~d0
set pfad=%~p0
%laufwerk%%pfad%

del %laufwerk%%pfad%\*.pyc /S/f/q
rmdir %laufwerk%%pfad%__pycache__  /S/q
pause
