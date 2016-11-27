web:python app.py runserver
web: gunicorn nsbabrahapp.wsgi --log-file -
heroku ps:scale web=1