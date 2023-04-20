import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

print(config.sections())
print(config.options('Super Secret Settings'))
print(config.get('Super Secret Settings','password'))