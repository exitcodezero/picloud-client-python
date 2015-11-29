A Python client for [PiCloud](https://github.com/exitcodezero/picloud).


Usage
====================

Using this module requires that you have exported both of the environment variables listed in the section above.


### SocketClient usage

```python
from picloud_client import SocketClient

client = SocketClient(
    url='wss://mypicloudserver.com',
    api_key='secretapikey',
    client_name='Whatever-You-Want')

# Publish 'data' for an 'event'
client.publish(event='temperature', data='76.5 F')

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

### HttpClient usage

```python
from picloud_client import HttpClient


client = HttpClient(
    url='http://mypicloudserver.com',
    api_key='secretapikey',
    client_name='Whatever-You-Want')

# Publish 'data' for an 'event'
client.publish(event='temperature', data='76.5 F')
```



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
