export 'DB_ENGINE=' \
    'DB_NAME=' \
    'DB_USER=' \
    'DB_PASSWORD=' \
    'DB_HOST=' \
    'DB_PORT=' \
    'STRYPE_API_KEY=' \
    'SECRET_KEY=' \
    'DOMEN='

python manage.py collectstatic && \
python manage.py runserver --insecure
