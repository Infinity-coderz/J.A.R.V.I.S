@echo off
:: Check if running as administrator by using net session
net session >nul 2>&1
if %errorLevel% == 0 (
    :: If already running as administrator, proceed
    echo Running with administrator privileges...
) else (
    :: If not running as administrator, restart the script with elevated permissions
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

pip install -r requirements.txt
echo Now running as administrator. 
exit
