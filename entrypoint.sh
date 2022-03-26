# update database based on django model definition
python manage.py migrate
# it just for experiment. so using django itself's runtime
# when it comes to deploying to the production considering wsgi or unicorn is better
python manage.py runserver 0.0.0.0:8000
