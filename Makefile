all: main

main: src/main.py
	python3 -m PyInstaller --onefile --clean src/main.py

clean:
	rm -rf build dist main
