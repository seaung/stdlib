import json
from typing import Any

def json_loads(file: str) -> Any:
    return json.loads(s=open(file=file, mode='r').read())


def json_dumps(o: Any) -> Any:
    return json.loads(o)

