from __future__ import print_function
import sys
import jsonschema
from jsonschema import validate

# Create the schema, as a nested Python dict
schema = {
    "type": "object",
    "required": [
              "text",
              "date",
           #   "retweets",
              "author",
              "url"
            ],
    "properties": {
        "text": {"type": "string"},
        "date": {"type": "string", "format": "int32"},
        "author": {"type": "string"},
        "url": {"type": "string"},
        "retweets": {
            "type": "array",
            "items": {
              "$ref": "#/retweets"
            },}
    },
    "retweets": {
        "type": "object",
        "required": [
          "date",
          "text",
          "author",
          "url"
        ],
        "properties": {
          "text": {"type": "string"},
          "date": {
            "type": "string",
            "format": "int32"
          },
          "author": {"type": "string"},
          "url": {"type": "string"}
        }
    }
}


# test data to be validated:
data = \
[
    {
        "url": "http://test.twitter.com",
        "author": "Pink-Hat",
        "date": "1999-01-11",
        "text": 'Testing, testing, 1,2,3',
        "retweets": [{"url": "http://test.twitter.co.uk", "author": "layerCake", "date": "01/09/2017", "text": "hello world"}]
    },
    {"url": "http://test.twitter.co.uk", "author": 9865, "date": "01/09/2017", "text": 'hello world'},
    {"url": "http://test.twitter.com", "author": "Slardybardfast", "text": 'We hate python'}
]


for idx, item in enumerate(data):
    try:
        validate(item, schema)
        sys.stdout.write("Record #{}: OK\n".format(idx))
    except jsonschema.exceptions.ValidationError as ve:
        pass
        sys.stderr.write("Record #{}: ERROR\n".format(idx))
        sys.stderr.write(str(ve) + "\n")
