@echo off
echo ========================================
echo   Universal Voice AI (Groq) Build Script
echo ========================================

echo 1. Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

echo 2. Building Universal Voice AI (Groq)...
pyinstaller --onefile --noconsole --name "Universal_Voice_AI" --clean main.py

echo.
echo ========================================
echo   Build Complete!
echo   Check the "dist" folder for EXE.
echo ========================================
pause
