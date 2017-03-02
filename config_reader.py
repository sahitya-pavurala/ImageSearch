import ConfigParser

Config = ConfigParser.RawConfigParser()
configFilePath = 'config.ini'
Config.read(configFilePath)

CLARIFAI_KEY = Config.get('clarifai', 'key')
CLARIFAI_SECRET = Config.get('clarifai', 'secret')
