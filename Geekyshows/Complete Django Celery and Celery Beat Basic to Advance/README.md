- [YouaTube Video Link](https://youtu.be/BGiQJgWukRA?si=nAc761dsYbYwOYNN)

- [Django Package](https://pypi.org/project/Django/)

- [Celery Package](https://pypi.org/project/celery/)

- [Django Celery Results Package](https://pypi.org/project/django-celery-results/)

- [Redis Package](https://pypi.org/project/redis/)

- [Celery Official Doc Link](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)

- [Celery Configuration Doc Link](https://docs.celeryq.dev/en/stable/userguide/configuration.html)

- [Celery Periodic Task Doc Link](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html)

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

- Start Celery Beat for Periodic Task
    ```bash
    celery -A myceleryproject beat -l info 
    ```