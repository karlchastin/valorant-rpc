@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    
	echo Building valorant-rpc...
	echo.
	
	REM Try to update requirements.txt with pipreqs (optional, can skip if it fails)
	echo Updating requirements.txt...
	python -m pip install pipreqs --quiet 2>nul
	python -m pipreqs . --force --no-pin 2>nul
	if errorlevel 1 (
		echo Warning: pipreqs failed, using existing requirements.txt
	)
	
	echo Installing dependencies...
	python -m pip install -r requirements.txt
	if errorlevel 1 (
		echo ERROR: pip install failed!
		pause
		exit /b 1
	)
	
	python -m pip install -r requirements.txt --upgrade
	if errorlevel 1 (
		echo ERROR: pip upgrade failed!
		pause
		exit /b 1
	)
	
	echo.
	echo Running PyInstaller...
	python -m PyInstaller valorant-rpc.spec
	if errorlevel 1 (
		echo.
		echo ERROR: PyInstaller failed!
		echo Check the error message above.
		pause
		exit /b 1
	)
	
	echo.
	echo Build completed successfully!
	echo The executable should be in the 'dist' folder.
	pause

