install:
	uv sync

dev:
	python manage.py runserver

#PORT ?= 8000
#start:
#	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) hexlet_django_blog:app

#render-start:
#	gunicorn -w 5 -b 0.0.0.0:$(PORT) hexlet_django_blog:app

#build:
#	./build.sh

build-requirements:
	uv pip compile pyproject.toml -o requirements.txt

test:
	uv run pytest

lint:
	uv run flake8 page_analyzer
