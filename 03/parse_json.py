import json
# json_str = """{
#     "name": "jane doe",
#     "salary": "9000",
#     "skills": "Raspberry_pi  Machine_Learning Web_Development",
#     "email": "JaneDoe@pynative.com",
#     "projects": "Python Data Mining, Python Data Science"
# }
# """
def keyword_callback(word):
    # print(word.upper())
    return word.upper()

def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    data = json.loads(json_str)
    output = []
    if required_fields:
        for field in required_fields:
            if keywords:
                for word in keywords:
                    if word in data[field].split(' '):
                        # print(keyword_callback(word))
                        final = keyword_callback(word)
                        output.append(final)
                    else:
                        line = f'no keyword "{word}" for field "{field}"'
                        output.append(line)
                        # return f'no keyword "{word}" for field "{field}"'
            else:
                # print('no keywords were provided')
                return 'no keywords were provided'
    else:
        # print('no required fields were provided')
        return 'no required fields were provided'
    return output

# parse_json(json_str, keyword_callback, ['skills', 'email'], ['Machine_Learning'])

