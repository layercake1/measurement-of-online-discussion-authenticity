import jsonschema
import logging.config
import json
from jsonschema import validate
from configuration.config_class import getConfig



#setup
config = getConfig()
json_file = config.get('Schema', 'json_file')
with open(json_file, 'r') as f:
    json_config = json.load(f)
schema = json_config['schema']
logging.config.fileConfig(getConfig().get("DEFAULT", "Logger_conf_file"))


def validate_json(json_):
    try:
        validate(json_, schema)
        logging.info("Record OK\n")
        return True
    except jsonschema.exceptions.ValidationError as ve:
        logging.warn("Record ERROR\n")
        logging.warn(str(ve) + "\n")
        return False
