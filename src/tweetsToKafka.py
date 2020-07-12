from tweepy.streaming import StreamListener
from util.applogger import getAppLogger
from kafka import KafkaProducer
import json

# Set a logger
logger = getAppLogger(__name__)

class TweetsToKafka(StreamListener):
    '''Listenser class extends from StreamListener parent class,
    writes tweets into kafka'''

    def __init__(self, serverName, topic):
        logger.info(f"Creating Kafka producer for the topic {topic}")
        self.producer = KafkaProducer(bootstrap_servers=serverName)
        self.topic = topic

    def on_data(self,data):
        try:
            createTime = ''
            tweet = ''
            userName = ''
            userLocation = ''
            userID = ''
            msg = json.loads(data, encoding='utf-8')
            if bool(msg['truncated']):
                tweet = msg['extended_tweet']['full_text']
            else:
                tweet = msg['text']

            if msg['user']['location']:
                # print(msg["user"]["location"].encode('utf-8'))
                userLocation = msg['user']['location']

            if msg['user']['screen_name']:
                userName = msg['user']['screen_name']

            if msg['created_at']:
                createTime = msg['created_at']

            if msg['user']['id']:
                userID = msg['user']['id']

            tweetDetails = {'user': userName, 'place': userLocation, 'msg': tweet, 'creationTime': createTime }

            # logger.info(f'{tweetDetails}')
            self.producer.send(self.topic, value=json.dumps(tweetDetails).encode('utf-8'), key=bytes(str(userID), 'utf-8'), headers=None, partition=None, timestamp_ms=None)
            return True
        except Exception as error:
            logger.exception(f"Error - {error}")
        else:
            logger.info("Retrieved the data successfully")

    def on_error(self, status):
        logger.exception(status)
