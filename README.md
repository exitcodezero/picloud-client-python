A Python client for [PiCloud](https://github.com/exitcodezero/picloud).



Environment Variables
====================

* `PICLOUD_URL` - URL for the `picloud` server
* `PICLOUD_API_KEY` - API key for the `picloud` server



Usage
====================

Using this module requires that you have exported both of the environment variables listed in the section above.


### Publish data for an event

```python
from picloud_client import PiCloud


picloud = PiCloud()

picloud.publish(event='temperature', data='76.5 F')
```


### Subscribe to data from an event

```python
from picloud_client import PiCloud


picloud = PiCloud()

# Subscription callbacks must have one parameter: 'data'
def on_temperature(data):
    # Do something way cooler here
    print(data)

picloud.subscribe(event='temperature', callback=on_temperature)

# Process incoming event data in a loop...forever
while True:
    picloud.process_subscriptions()
```

Multiple callbacks can be subscribed to an `event`. They are executed in the order they were added from the `subscribe` method.



Run Tests
====================

After cloning this repo

```
pip install -r requirements.txt
```

```
nosetests -v --with-coverage --cover-erase --cover-package=picloud_client --cover-html
```


Run Tests with Docker Compose
====================

```
docker-compose run picloud_client nosetests -v --with-coverage --cover-erase --cover-package=picloud_client --cover-html
```
