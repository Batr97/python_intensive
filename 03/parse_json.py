import json

def keyword_callback(word):
    return word.upper()

def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    data = json.loads(json_str)
    output = []
    if required_fields:
        for field in required_fields:
            if keywords:
                for word in keywords:
                    if word in data[field].split(' '):
                        final = keyword_callback(word)
                        output.append(final)
                    else:
                        line = f'no keyword "{word}" for field "{field}"'
                        output.append(line)
            else:
                return 'no keywords were provided'
    else:
        return 'no required fields were provided'
    return output


