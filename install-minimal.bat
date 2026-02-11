@echo off
REM Simple Installation Script - Minimal Version
REM This installs only the core dependencies to get the app running quickly

echo ================================================
echo Contract Language Simplifier - Quick Install
echo ================================================
echo.
echo This will install minimal dependencies first.
echo AI models can be added later.
echo.

REM Check if venv exists
if exist venv (
    echo Virtual environment found.
) else (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo.
echo Installing minimal dependencies...
venv\Scripts\pip.exe install textstat==0.7.3
if errorlevel 1 (
    echo WARNING: textstat installation failed
)

echo.
echo Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Created .env file
) else (
    echo .env file already exists
)

echo.
echo ================================================
echo Installation Complete!
echo ================================================
echo.
echo The basic application is ready to run.
echo.
echo To start the application:
echo   venv\Scripts\python.exe app.py
echo.
echo Note: AI simplification features require additional setup.
echo See INSTALL_AI.md for instructions.
echo.
pause
