@ECHO OFF
TITLE YTDL
CLS

:MAIN
python GUI.py

REM // Restarting.
echo.
TIMEOUT /T 1 /NOBREAK >NUL
goto MAIN
