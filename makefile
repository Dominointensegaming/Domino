install: 
	pip install -r requirements.txt
run: install
	fastapi dev backend/app/main.py

