import json
from datetime import datetime
import os
import shutil
from tweepy.streaming import StreamListener
from util.applogger import getAppLogger

# Set a logger
logger = getAppLogger(__name__)


class TweetsToJSON(StreamListener):
    '''Listenser class extends from StreamListener parent class'''

    def __init__(self, fileDir, fileSize, processedDir):
        self.fileDir = fileDir
        self.fileName = fileDir + "\\twitter_" + datetime.today().strftime("%Y%m%d_%H%M%S") + ".json"
        self.fileSize = fileSize
        self.processedDir = processedDir

    def on_data(self, data):
        try:
            msg = json.loads(data, encoding='utf-8')
            text = ''
            userName = ''
            userLocation = ''

            if "text" in msg:
                #print(msg['text'].encode('utf-8'), msg['truncated'])
                text = msg['text']

            if msg["user"]["location"]:
                # print(msg["user"]["location"].encode('utf-8'))
                userLocation = msg["user"]["location"]

            if msg["user"]["screen_name"]:
                userName = msg["user"]["screen_name"]

            twitterDetails = {
                "userName": userName,
                "userLocation": userLocation,
                "msg": text
            }
            logger.info("Got the tweet details, writing to JSON file")
            self.writeJSONFile(twitterDetails)

        except KeyError:
            logger.warning("Warn - Required fields does not exist")
        except IOError as error:
            logger.exception(f"Error - File operation issue {error}")
        except Exception as error:
            logger.exception(f"Error - {error}")
        else:
            logger.info("Retrieved the data successfully")

    def writeJSONFile(self, twitterDetails):
        '''Writes the message into a JSON file and creates new file when needed'''
        with open(self.fileName, mode='a', encoding="utf-8") as twFile:
            json.dump(twitterDetails, twFile, ensure_ascii=False)
            twFile.write("\n")
        if int(os.path.getsize(self.fileName)) > self.fileSize:
            logger.info(
                f"JSON file {self.fileName} has reached the max file size, hence moving to {self.processedDir}")
            self.moveProcessedJSON()
            self.fileName = self.fileDir + "\\twitter_" + datetime.today().strftime("%Y%m%d_%H%M%S") + ".json"
            logger.info(f"New JSON file is {self.fileName}")

    def moveProcessedJSON(self):
        '''Move the JSON file to processed directory'''
        #os.rename(self.fileName, self.fileDir + "\\processed_files\\twitter.json")
        shutil.move(self.fileName, self.processedDir)

    def on_error(self, status):
        logger.exception(status)
