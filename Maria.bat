rem lanza un program python
echo off
chcp 65001
c:
cd "C:\Datos\OneDrive\Proyectos_python\Maria - web"

set directorio="./" 
set programa="app.py"

echo %directorio%  %programa%
cd %directorio%

:inicio
if exist ./temp/%~n0_%today%.temp goto fin:
	call conda activate trabajo
	call python %programa%
	echo  %time% > ./temp/%~n0_%today%.temp
:fin
goto inicio
pause
