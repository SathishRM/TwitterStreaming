### Using Tweepy look for the tweets with a list of words and capture it in a JSON file.

JSON files will be created upto the size mentioned in properties file. Once it reaches threshold, the file will be moved and a new file will created.

Look at the file **requirements.txt** for any external library required by the script. Make sure those are installed first.

The search words are passed as agrument to the script. It is an optional argument. If nothing passed, the script will look for the tweets with the default word configured in the properties file.

#### Arguments allowed: ####
  * -h, --help     show this help message and exit
  
  * -s SEARCHWORDS, --searchWords SEARCHWORDS     search words with space separated
  
*Command to run the script:*
**twitterstreamclient.py -s python,tweepy**

**Update the config file with the settings as per the environment.**
