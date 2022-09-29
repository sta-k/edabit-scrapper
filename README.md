# Edabit Scrapper

# geckodriver

https://github.com/mozilla/geckodriver/releases

download and extract the file and copy it to 
	
	`sudo mv geckodriver /usr/local/bin/`

## install dependencies

	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt

## scrap edabit

to scrap instructions and solutions, update `challenges` list and run:

    python scrap.py all

to scrap ids, run:
	
	python scrap.py ids

## django site

	cd mysite
	./manage.py runserver