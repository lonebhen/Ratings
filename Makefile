
.PHONY: runserver
runserver:
	python manage.py runserver

.PHONY: migrations
migrations:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: superuser
superuser:
	python manage.py createsuperuser
