@echo off
echo Building AI Directory Manager Executable (Simple Method)...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

REM Build the executable using PyInstaller directly
pyinstaller --onefile --windowed --name "AI Directory Manager" --add-data "gui/styles.qss;gui" --add-data "backend;backend" gui/main.py

echo.
echo Build completed!
echo.
echo The executable is located in the 'dist' folder.
echo You can run 'AI Directory Manager.exe' directly.
echo.
pause
