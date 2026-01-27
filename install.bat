@echo off
echo ========================================
echo Installation des dependances pour valorant-rpc
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Python n'est pas installe ou n'est pas dans le PATH
    echo Veuillez installer Python depuis https://www.python.org/
    pause
    exit /b 1
)

echo Mise a jour de pip...
python -m pip install --upgrade pip

echo.
echo Installation des dependances depuis requirements.txt...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERREUR: L'installation a echoue
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation terminee avec succes!
echo ========================================
echo.
pause
