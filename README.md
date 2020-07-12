### Look for tweets with a list of words using Tweepy and capture it either in a JSON file or a topic in KAFKA.

Toggle between Kafka and JSON file by calling the respective class in the client program.
Tweets are appended to a JSON file upto the size mentioned in the application properties. Once it reaches threshold, the file will be moved and a new file will be created.

Look at the file **requirements.txt** for any external library required by the script. Make sure those are installed first.

The search words are passed as agrument to the script. It is an optional argument. If nothing passed, the script will look for the tweets with the default word configured in the properties file.

#### Arguments allowed: ####
  * -h, --help     show this help message and exit
  
  * -s SEARCHWORDS, --searchWords SEARCHWORDS     search words with space separated
  
*Command to run the script:*
**twitterstreamclient.py -s python,tweepy**

**Update the config file with the settings as per the environment.**
