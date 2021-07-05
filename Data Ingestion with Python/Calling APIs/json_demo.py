"""Example of custom JSON decoder"""

import json
from datetime import datetime


# b in front means this is a bits object.
#This shows a transaction from a party to another party.
data = b'''
{
    "from": "While. E. Coyote",
    "to": "ACME",
    "amount": 103.7,
    "time": "2019-08-07T12:28:39.781551"
}
'''

def fix_time(pair):
    key, value = pair
    if key != 'time':
        return pair
    return (key, datetime.fromisoformat(value))


def object_pairs_hook(pairs):
    return dict(fix_time(pair) for pair in pairs)

#json.loads and dumps to work with bits or strings
#json.load or dump to work with file like objects opensfiles or http responses
obj = json.loads(data, object_pairs_hook=object_pairs_hook)
print(obj)
