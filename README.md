# JSON-CSV Converter

A powerful, flexible, and easy-to-use Python utility for converting between JSON and CSV formats. This tool handles complex nested JSON structures, supports custom delimiters, and provides both command-line and programmatic interfaces.

## 🌟 Features

- **Bidirectional Conversion**: Seamlessly convert between JSON and CSV formats
- **Nested JSON Support**: Automatically flattens nested JSON objects for CSV compatibility
- **Flexible Configuration**: Customize delimiters and flattening behavior
- **Command-Line Interface**: Simple CLI for quick conversions
- **Python API**: Integrate into your Python projects with ease
- **Robust Error Handling**: Clear error messages for debugging
- **UTF-8 Support**: Full Unicode support for international data
- **Zero Dependencies**: Uses only Python standard library

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Command Line](#command-line)
  - [Python API](#python-api)
- [Examples](#examples)
- [API Documentation](#api-documentation)
- [Advanced Features](#advanced-features)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/holly-copilot-pro-plus/test.git
cd test
```

2. Make the script executable (optional):
```bash
chmod +x json_csv_converter.py
```

That's it! The converter uses only Python standard library, so no additional dependencies are required.

## ⚡ Quick Start

### Convert JSON to CSV

```bash
python3 json_csv_converter.py json2csv input.json output.csv
```

### Convert CSV to JSON

```bash
python3 json_csv_converter.py csv2json input.csv output.json
```

## 📖 Usage

### Command Line

The converter provides a simple command-line interface for quick conversions.

#### Syntax

```bash
python3 json_csv_converter.py <command> <input_file> <output_file>
```

#### Commands

- `json2csv` - Convert JSON to CSV format
- `csv2json` - Convert CSV to JSON format

#### Examples

```bash
# Convert JSON array to CSV
python3 json_csv_converter.py json2csv data.json data.csv

# Convert CSV to JSON array
python3 json_csv_converter.py csv2json data.csv data.json
```

### Python API

Import and use the converter in your Python code for more control and flexibility.

#### Basic Usage

```python
from json_csv_converter import JSONCSVConverter

# Create converter instance
converter = JSONCSVConverter()

# Convert JSON to CSV
converter.json_to_csv('input.json', 'output.csv')

# Convert CSV to JSON
converter.csv_to_json('input.csv', 'output.json')
```

#### Advanced Configuration

```python
from json_csv_converter import JSONCSVConverter

# Customize converter behavior
converter = JSONCSVConverter(
    flatten_nested=True,    # Flatten nested JSON objects
    delimiter=';'           # Use semicolon as delimiter
)

# Convert with custom settings
converter.json_to_csv('data.json', 'data.csv')
```

#### Working with Data Structures

```python
from json_csv_converter import JSONCSVConverter

# Convert from Python data structure
data = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'}
]

converter = JSONCSVConverter()
converter.json_to_csv(data, 'output.csv')
```

## 💡 Examples

### Example 1: Simple JSON Array

**Input JSON** (`people.json`):
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 28
  }
]
```

**Command:**
```bash
python3 json_csv_converter.py json2csv people.json people.csv
```

**Output CSV** (`people.csv`):
```csv
age,email,id,name
30,john@example.com,1,John Doe
28,jane@example.com,2,Jane Smith
```

### Example 2: Nested JSON Objects

**Input JSON** (`users.json`):
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "address": {
      "street": "123 Main St",
      "city": "New York",
      "country": "USA"
    }
  }
]
```

**Command:**
```bash
python3 json_csv_converter.py json2csv users.json users.csv
```

**Output CSV** (`users.csv`):
```csv
address.city,address.country,address.street,id,name
New York,USA,123 Main St,1,John Doe
```

### Example 3: Custom Delimiter

```python
from json_csv_converter import JSONCSVConverter

# Use tab as delimiter
converter = JSONCSVConverter(delimiter='\t')
converter.json_to_csv('data.json', 'data.tsv')
```

### Example 4: Round-trip Conversion

```python
from json_csv_converter import JSONCSVConverter

converter = JSONCSVConverter()

# JSON → CSV → JSON
converter.json_to_csv('original.json', 'temp.csv')
converter.csv_to_json('temp.csv', 'restored.json', unflatten=True)
```

## 📚 API Documentation

### JSONCSVConverter Class

#### Constructor

```python
JSONCSVConverter(flatten_nested=True, delimiter=',')
```

**Parameters:**
- `flatten_nested` (bool): Whether to flatten nested JSON objects. Default: `True`
- `delimiter` (str): CSV delimiter character. Default: `','`

#### Methods

##### json_to_csv()

```python
json_to_csv(json_data, output_file)
```

Convert JSON data to CSV format.

**Parameters:**
- `json_data`: Can be:
  - String path to JSON file
  - `Path` object to JSON file
  - Python list of dictionaries
- `output_file`: String path or `Path` object for output CSV file

**Raises:**
- `ValueError`: If JSON data is not an array of objects or is empty
- `IOError`: If file operations fail

**Example:**
```python
converter = JSONCSVConverter()
converter.json_to_csv('input.json', 'output.csv')
```

##### csv_to_json()

```python
csv_to_json(csv_file, output_file, unflatten=False)
```

Convert CSV data to JSON format.

**Parameters:**
- `csv_file`: String path or `Path` object to input CSV file
- `output_file`: String path or `Path` object for output JSON file
- `unflatten` (bool): Whether to unflatten dotted keys. Default: `False`

**Raises:**
- `IOError`: If file operations fail

**Example:**
```python
converter = JSONCSVConverter()
converter.csv_to_json('input.csv', 'output.json', unflatten=True)
```

## 🔧 Advanced Features

### Handling Nested Structures

The converter automatically flattens nested JSON objects using dot notation:

```json
{
  "user": {
    "profile": {
      "name": "John"
    }
  }
}
```

Becomes:
```csv
user.profile.name
John
```

### Array Handling

JSON arrays are converted to JSON strings in CSV format to maintain data integrity:

```json
{
  "name": "John",
  "hobbies": ["reading", "gaming"]
}
```

Becomes:
```csv
name,hobbies
John,"[""reading"", ""gaming""]"
```

### Unflattening Data

When converting back from CSV to JSON, you can unflatten dotted keys:

```python
converter = JSONCSVConverter()
converter.csv_to_json('data.csv', 'data.json', unflatten=True)
```

This converts `user.profile.name` back to `{"user": {"profile": {"name": "..."}}}`

### Custom Delimiters

Support for custom delimiters (e.g., tab-separated values):

```python
# Tab-separated values
converter = JSONCSVConverter(delimiter='\t')

# Semicolon-separated values (common in Europe)
converter = JSONCSVConverter(delimiter=';')

# Pipe-separated values
converter = JSONCSVConverter(delimiter='|')
```

## ⚠️ Error Handling

The converter provides clear error messages for common issues:

### Invalid JSON Format

```python
# Error: JSON data must be an array of objects
# Ensure your JSON starts with [ and contains objects {...}
```

### Empty Data

```python
# Error: JSON data is empty
# Check that your JSON file contains data
```

### File Not Found

```python
# Error: [Errno 2] No such file or directory: 'file.json'
# Verify the file path is correct
```

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| JSON file not an array | Wrap objects in `[...]` |
| Nested objects not flattening | Ensure `flatten_nested=True` (default) |
| Special characters in CSV | Data is automatically quoted when needed |
| Large files processing slowly | Consider processing in chunks for very large datasets |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/holly-copilot-pro-plus/test/issues)
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Sample data (if applicable)

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its use case
3. Provide examples if possible

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to your fork: `git push origin feature/amazing-feature`
8. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions and classes
- Include type hints where appropriate
- Write clear commit messages
- Update documentation for new features

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 JSON-CSV Converter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🔗 Links

- **Repository**: [https://github.com/holly-copilot-pro-plus/test](https://github.com/holly-copilot-pro-plus/test)
- **Issues**: [https://github.com/holly-copilot-pro-plus/test/issues](https://github.com/holly-copilot-pro-plus/test/issues)
- **Changelog**: See commit history for recent changes

## 📞 Support

If you encounter any issues or have questions:

1. Check the [documentation](#table-of-contents) above
2. Search [existing issues](https://github.com/holly-copilot-pro-plus/test/issues)
3. Open a new issue with details about your problem

## 🙏 Acknowledgments

- Built with Python's robust standard library
- Inspired by the need for simple, reliable data format conversion
- Thanks to all contributors and users of this tool

---

**Made with ❤️ by the JSON-CSV Converter team**
