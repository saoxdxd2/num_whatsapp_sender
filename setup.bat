@echo off
:: Check for admin rights
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command ^
        "Start-Process cmd -ArgumentList '/c \"set ADMIN_ELEVATED=1 && call \"%~f0\"\"' -Verb RunAs"
    exit /b
)

:: Prevent infinite re-entry
if "%ADMIN_ELEVATED%"=="1" (
    set ADMIN_ELEVATED=
)

:: Running with administrative privileges here
echo Running with administrative privileges...

:: Check if Chocolatey is installed
choco -v >nul 2>&1
if %errorLevel% neq 0 (
    echo Installing Chocolatey...
    powershell -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command ^
    "Set-ExecutionPolicy Bypass -Scope Process -Force; ^
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; ^
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
) else (
    echo Chocolatey already installed.
)

:: Refresh environment variables
refreshenv >nul

:: Install Git and Python using Chocolatey
choco install git python -y --ignore-checksums

:: Wait for install to finish
timeout /t 5

:: Run the Python setup script
echo Running Python setup.py script...
python setup.py

echo.
echo Setup complete. Press any key to exit.
pause >nul
