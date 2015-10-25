import unittest
from picloud_client import PiCloud


class PiCloudPublishTestCase(unittest.TestCase):

    def setUp(self):
        super(PiCloudPublishTestCase, self).setUp()

    def test_publish(self):
        subscriber = PiCloud()

        def on_event(data):
            self.assertEqual(data, 'test')

        subscriber.subscribe(event='whatever', callback=on_event)

        publisher = PiCloud()
        publisher.publish(event='whatever', data='test')

        subscriber.process_subscriptions()
