@echo off
setlocal
set "TARGET=%~dp0Pasta principal\trabalho\Painel.pyw"
cd /d "%~dp0Pasta principal\trabalho"

if exist "%~dp0Pasta principal\.venv\Scripts\python.exe" (
    "%~dp0Pasta principal\.venv\Scripts\python.exe" -c "import sys, tkinter; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>&1
    if not errorlevel 1 (
        if exist "%~dp0Pasta principal\.venv\Scripts\pythonw.exe" (
            start "" "%~dp0Pasta principal\.venv\Scripts\pythonw.exe" "%TARGET%"
        ) else (
            start "" "%~dp0Pasta principal\.venv\Scripts\python.exe" "%TARGET%"
        )
        exit /b
    )
)

where py.exe >nul 2>&1
if not errorlevel 1 (
    py.exe -3 -c "import sys, tkinter; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>&1
    if not errorlevel 1 (
        where pyw.exe >nul 2>&1
        if not errorlevel 1 (
            start "" pyw.exe -3 "%TARGET%"
        ) else (
            start "" py.exe -3 "%TARGET%"
        )
        exit /b
    )
)

where python.exe >nul 2>&1
if not errorlevel 1 (
    python.exe -c "import sys, tkinter; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>&1
    if not errorlevel 1 (
        where pythonw.exe >nul 2>&1
        if not errorlevel 1 (
            start "" pythonw.exe "%TARGET%"
        ) else (
            start "" python.exe "%TARGET%"
        )
        exit /b
    )
)

for /d %%D in ("%LocalAppData%\Programs\Python\Python3*") do (
    if exist "%%~fD\python.exe" (
        "%%~fD\python.exe" -c "import sys, tkinter; sys.exit(0 if sys.version_info >= (3,10) else 1)" >nul 2>&1
        if not errorlevel 1 (
            if exist "%%~fD\pythonw.exe" (
                start "" "%%~fD\pythonw.exe" "%TARGET%"
            ) else (
                start "" "%%~fD\python.exe" "%TARGET%"
            )
            exit /b
        )
    )
)

echo.
echo Python 3.10+ com Tkinter nao foi encontrado neste PC.
echo Instale o Python em https://www.python.org/downloads/ (marque "Add python.exe to PATH" e "tcl/tk").
echo.
pause
