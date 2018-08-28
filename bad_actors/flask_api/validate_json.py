from __future__ import print_function
import sys
import jsonschema
from jsonschema import validate


def validate_json(json, schema):
    try:
        validate(json, schema)
        sys.stdout.write("Record OK\n")
        return True
    except jsonschema.exceptions.ValidationError as ve:
        sys.stderr.write("Record ERROR\n")
        sys.stderr.write(str(ve) + "\n")
        return False


