@echo off
echo ========================================
echo Hope-iatry AI Coaching Platform
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo ERROR: .env file not found!
    echo.
    echo Please follow these steps:
    echo 1. Copy .env.example to .env
    echo 2. Add your ANTHROPIC_API_KEY to .env
    echo.
    pause
    exit
)

echo Starting server...
echo.
echo The app will be available at:
echo   - Local: http://localhost:5000
echo   - Network: http://YOUR_IP:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python backend.py

pause
