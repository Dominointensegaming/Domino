install: 
	pip install -r requirements.txt
run: install
	fastapi dev main.py

