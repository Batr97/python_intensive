import json
json_str = """{
    "name": "jane doe",
    "salary": "9000",
    "skills": "Raspberry_pi  Machine_Learning Web_Development",
    "email": "JaneDoe@pynative.com",
    "projects": "Python Data Mining, Python Data Science"
}
"""
def keyword_callback(word):
    return word.upper()

def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    data = json.loads(json_str)
    for field in required_fields:
        for word in keywords:
            if word in data[field].split(' '):
                print(keyword_callback(word))
            else:
                print(f'no keyword "{word}" for field "{field}"')

parse_json(json_str, keyword_callback, ['skills', 'email'], ['Machine_Learning'])
