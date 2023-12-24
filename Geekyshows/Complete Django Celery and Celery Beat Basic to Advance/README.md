- [YouaTube Video Link](https://youtu.be/BGiQJgWukRA?si=nAc761dsYbYwOYNN)

- [Django Package](https://pypi.org/project/Django/)

- [Celery Package](https://pypi.org/project/celery/)

- [Redis Package](https://pypi.org/project/redis/)

- [Celery Official Doc Link](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)

- Install redis on linux -
    ```bash
    sudo snap install redis
    ```

- Start redis server -
    ```bash
    redis-server
    ```

- See all redis keys
    ```bash
    redis-cli
    ```

    ```bash
    keys *
    ```

- Start Celery Worker -
    ```bash
    celery -A myceleryproject worker -l info 
    ```