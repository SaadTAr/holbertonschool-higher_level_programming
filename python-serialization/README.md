# Python - Serialization

This project demonstrates basic serialization and deserialization in Python using the built-in `json` module.

## Task 0 - Basic Serialization

The file `task_00_basic_serialization.py` provides two functions:

- `serialize_and_save_to_file(data, filename)`
  - Serializes a Python dictionary into JSON format.
  - Saves the JSON data to a file.

- `load_and_deserialize(filename)`
  - Reads a JSON file.
  - Deserializes the JSON content.
  - Returns the corresponding Python dictionary.

## Requirements

- Python 3
- Uses only the standard `json` module.
- UTF-8 file encoding.

## Example

```python
from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize,
)

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data, "data.json")

loaded = load_and_deserialize("data.json")
print(loaded)
```

Output:

```python
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```
