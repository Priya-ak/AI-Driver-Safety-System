@echo off

echo Starting AI Driver Safety System...

echo Creating virtual environment...
python -m venv venv

echo Activating environment...
call venv\Scripts\activate

echo Installing packages...
pip install -r requirements.txt

echo Starting server...

uvicorn server:app --reload --port 9777

pause