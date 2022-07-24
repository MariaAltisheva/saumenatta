import json
from utils import get_questions_data_by_requests

readable_file = 'readable_k.json'
with open(readable_file, 'w') as f:
    json.dump(get_questions_data_by_requests(), f, indent=4)