import argparse
from tweepy import OAuthHandler, Stream
from util.appconfigreader import AppConfigReader
from util.applogger import getAppLogger
from tweetstoJSON import TweetsToJSON

if __name__ == '__main__':
    logger = getAppLogger(__name__)

    # Read TWITTER account detaild from CFG file
    appConfigReader = AppConfigReader()
    if 'TWITTER_ACC' in appConfigReader.config:
        twitterCfg = appConfigReader.config['TWITTER_ACC']
        consumerKey = twitterCfg['CONSUMER_KEY']
        consumerSecret = twitterCfg['CONSUMER_SECRET']
        accessToken = twitterCfg['ACCESS_TOKEN']
        accessSecret = twitterCfg['ACCESS_SECRET']
    else:
        logger.error("Error - Twitter account details are not configured yet")
        raise SystemExit(1)

    if 'APP' in appConfigReader.config:
        appCfg = appConfigReader.config['APP']
        defaultWord = appCfg['DEFAULT_WORD']
        jsonDir = appCfg['JSON_DIR']
        processedDir = appCfg['PROCESSED_FILES']
        jsonMaxSize = int(appCfg['JSON_MAX_SIZE'])
    else:
        logger.error("Error - Application config are missing")
        raise SystemExit(1)

    # Get the words list to search in tweets
    argParser = argparse.ArgumentParser("List of search words")
    argParser.add_argument("-s", "--searchWords",
                           help="search words with space separated", default=defaultWord)
    # argParser.add_argument()
    args = argParser.parse_args()
    logger.info(f"Going to look for the words {args.searchWords}...")

    auth = OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    tweetListener = TweetsToJSON(jsonDir, jsonMaxSize, processedDir)
    tweetStreaming = Stream(auth, tweetListener)
    tweetStreaming.filter(track=[args.searchWords])
