.PHONY: up down build logs ps migrate makemigrations createsuperuser shell dbshell reset

# --- Docker ---
up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

ps:
	docker compose ps -a

# --- Django (local) ---
migrate:
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

createsuperuser:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

dbshell:
	python3 manage.py dbshell

# --- Reset DB (cuidado) ---
reset:
	docker compose down -v
	docker compose up -d
