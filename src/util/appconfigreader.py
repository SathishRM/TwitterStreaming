from configparser import ConfigParser
import os


class AppConfigReader():
    '''Loads the config file values'''

    def __init__(self):
        self.config = ConfigParser()
        # Get the config file path from environmental variable PY_APP_CONFIG
        cfgDir = os.environ.get('PY_APP_CONFIG')
        if cfgDir:
            cfgFile = cfgDir + "\\tweetsToJSON.properties"
        else:
            cfgFile = "E:\\Python\\github\\conf\\tweetsToJSON.properties"

        # Load the CFG file
        self.config.read(cfgFile)
