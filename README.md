A Python client for [PiCloud](https://github.com/exitcodezero/picloud).


Usage
====================

Using this module requires that you have exported both of the environment variables listed in the section above.


### Publish data for an event

```python
from picloud_client import PubClient


client = PubClient(
    url='http://mypicloudserver.com/publish',
    api_key='secretapikey',
    client_name='Whatever-You-Want')

client.publish(event='temperature', data='76.5 F')
```


### Subscribe to data from an event

```python
from picloud_client import SubClient


client = SubClient(
    url='wss://mypicloudserver.com/subscribe',
    api_key='secretapikey',
    client_name='Whatever-You-Want')

# Subscription callbacks must have one parameter: 'data'
def on_temperature(data):
    # Do something way cooler here
    print(data)

client.subscribe(event='temperature', callback=on_temperature)

# Process incoming event data in a loop...forever
while True:
    client.process_subscriptions()
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
