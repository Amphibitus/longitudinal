@echo off
c:
SET OSGEO4W_ROOT=C:\OSGeo4W
SET QGISNAME=qgis
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

@echo on
call "%OSGEO4W_ROOT%\apps\Python312\Scripts\pyrcc5" -o resources.py resources.qrc


del /s /q __pycache__\*.*
rmdir /s /q __pycache__

del /s /q PyPDF2\PyPDF2\__pycache__\*.*
rmdir /s /q PyPDF2\PyPDF2\__pycache__
rem pause