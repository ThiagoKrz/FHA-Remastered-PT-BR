@echo off
setlocal
cd /d "%~dp0"
where pythonw.exe >nul 2>&1
if not errorlevel 1 (
    start "" pythonw.exe "%~dp0Painel.pyw"
    exit /b
)
where python.exe >nul 2>&1
if not errorlevel 1 (
    start "" python.exe "%~dp0Painel.pyw"
    exit /b
)
echo Python com Tkinter nao foi encontrado. Instale Python 3.10 ou superior.
pause
