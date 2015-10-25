picloud-client-python
====================



Environment Variables
====================

* `PICLOUD_URL` - URL for the `picloud` server
* `PICLOUD_API_KEY` - API key for the `picloud` server



Run Tests
====================

After cloning this repo

```
pip install -r requirements.txt
```

```
nosetests -v --with-coverage --cover-erase --cover-package=pycards --cover-html
```


Run Tests with Docker Compose
====================

```
docker-compose run picloud_client nosetests -v --with-coverage --cover-erase --cover-package=picloud_client --cover-html
```
