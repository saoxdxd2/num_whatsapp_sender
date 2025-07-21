@echo off
:: Check if script is running elevated
if "%1"=="--elevated" goto elevated

:: Not elevated - relaunch as admin with --elevated argument and keep window open
echo Requesting administrative privileges...
powershell -Command "Start-Process -FilePath 'cmd.exe' -ArgumentList '/k \"%~f0\" --elevated' -Verb RunAs"
exit /b

:elevated
echo Running with administrative privileges...

:: Check if Chocolatey is installed
choco -v >nul 2>&1
if %errorLevel% neq 0 (
    echo Installing Chocolatey...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"

    :: Now run refreshenv to reload env vars
    echo Refreshing environment variables...
    call "%ALLUSERSPROFILE%\chocolatey\bin\refreshenv.cmd"
) else (
    echo Chocolatey already installed.
)

:: Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Python not detected. Installing Python...
    choco install python -y --ignore-checksums
) else (
    echo Python is already installed.
)

:: Check if Git is installed
git --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Git not detected. Installing Git...
    choco install git -y --ignore-checksums
) else (
    echo Git is already installed.
)

echo Waiting for installations to finish...
timeout /t 5 /nobreak >nul

:: Change directory to the batch file's location before running setup.py
cd /d "%~dp0"

echo Running Python setup.py script...
python setup.py

echo.
echo Setup complete. Press any key to exit.
pause >nul

exit /b
