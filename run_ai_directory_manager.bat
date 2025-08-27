@echo off
echo Starting AI Directory Manager...
echo.

REM Check if executable exists
if not exist "dist\AI Directory Manager.exe" (
    echo Error: Executable not found!
    echo Please run build_simple.bat first to build the application.
    pause
    exit /b 1
)

REM Launch the application
start "" "dist\AI Directory Manager.exe"

echo AI Directory Manager launched successfully!
echo.
pause
