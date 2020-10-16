from typing import Any, Dict
import json
import requests


def post(url: str, data: Dict[str, Any]) -> Dict[str, Any]:
    res = requests.post(
        url=url,
        data=json.dumps(data))
    return json.loads(res.text)
