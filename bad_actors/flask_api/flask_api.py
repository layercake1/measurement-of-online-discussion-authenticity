from flask import Flask, jsonify, abort, make_response, request
import sys
import json
from flask_sqlalchemy import SQLAlchemy

sys.path.append("C:\Users\leahk\Desktop\measurement-of-online-discussion-authenticity\\bad_actors")
from configuration.config_class import getConfig
from validate_json import validate_json


# config
app = Flask(__name__)
#config = getConfig()
#json_file = config.get('Schema', 'json_file')
json_file = 'configuration/config_api.json'
with open(json_file, 'r') as f:
    json_config = json.load(f)

schema = json_config['schema']
print schema
test_data = [item for item in json_config['test_data']]

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:Aa12345@localhost/campaigns'
# db = SQLAlchemy(app)

# test-data
campaigns = [
    {'campaign_id': 100, 'keywords': ['test', 'testing'], 'status': 'finished prediction', 'fake_news_score': 0.5},
    {'campaign_id': 101, 'keywords': ['hello world'], 'status': 'finished prediction', 'fake_news_score': 0.9}
]


# add campaign to database
@app.route('/api/v1/campaigns/add', methods=['POST'])
def add_campaign():
    if not request.json:
        abort(400)
    if not validate_json(request.json, schema):
        abort(400)
    campaign = {
        'campaign_id': campaigns[-1]['campaign_id'] + 1,
        'url': request.json['url']
    }
    campaigns.append(campaign)
    return jsonify({'campaign_id': campaign['campaign_id'], 'url': campaign['url']})


# check campaign status
@app.route('/api/v1/campaigns/<int:campaign_id>/status', methods=['GET'])
def check_status(campaign_id):
    campaign = [campaign for campaign in campaigns if campaign['campaign_id'] == campaign_id]
    if len(campaign) == 0:
        abort(404)
    return jsonify({'status': campaign[0]['status'], 'fake_news_score': campaign[0]['fake_news_score']})


# error handlers
@app.errorhandler(400)
def invalid_input(error):
    return make_response(jsonify({'error': 'Invalid input, object invalid'}))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(409)
def object_exists(error):
    return make_response(jsonify({'error': 'Item already exists'}))


@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal error'}), 500)


if __name__ == '__main__':
    print sys.path
    app.run(debug=True)
