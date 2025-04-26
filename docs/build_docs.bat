call ..\.venv\Scripts\activate
set GENERATING_DOCS=1
call .\make.bat clean
call .\make.bat html
pause