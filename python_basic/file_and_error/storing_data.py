"""json.dumps 和 json.loads"""

from pathlib import Path
import json

numbers = [2, 3, 5, 8, 13, 21]
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
