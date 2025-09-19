# JSON-CSV Converter

A powerful and flexible tool for converting between JSON and CSV formats. This converter supports complex nested JSON structures, customizable field mappings, and various output formatting options.

## Features

- 🔄 **Bidirectional Conversion**: Convert JSON to CSV and CSV to JSON
- 🏗️ **Nested JSON Support**: Handle complex nested objects and arrays
- ⚙️ **Customizable Options**: Configure delimiters, encoding, and field mappings
- 📊 **Flexible Output**: Support for various CSV dialects and JSON formatting
- 🚀 **High Performance**: Optimized for large datasets
- 🛡️ **Error Handling**: Comprehensive validation and error reporting
- 📝 **CLI and API**: Use via command line or integrate into your applications

## Installation

### Using npm (Node.js)
```bash
npm install -g json-csv-converter
```

### Using pip (Python)
```bash
pip install json-csv-converter
```

### From Source
```bash
git clone https://github.com/holly-copilot-pro-plus/test.git
cd test
npm install  # or pip install -r requirements.txt for Python
```

## Quick Start

### Command Line Usage

#### JSON to CSV
```bash
# Basic conversion
json-csv-converter input.json output.csv

# With custom delimiter
json-csv-converter input.json output.csv --delimiter ";"

# Flatten nested objects
json-csv-converter input.json output.csv --flatten
```

#### CSV to JSON
```bash
# Basic conversion
json-csv-converter input.csv output.json

# Create nested structure
json-csv-converter input.csv output.json --nest

# Pretty print JSON
json-csv-converter input.csv output.json --pretty
```

### API Usage

#### JavaScript/Node.js
```javascript
const { JSONToCSV, CSVToJSON } = require('json-csv-converter');

// JSON to CSV
const jsonData = [
  { name: "John", age: 30, city: "New York" },
  { name: "Jane", age: 25, city: "San Francisco" }
];

const csv = JSONToCSV(jsonData);
console.log(csv);
// Output: name,age,city
//         John,30,New York
//         Jane,25,San Francisco

// CSV to JSON
const csvData = `name,age,city
John,30,New York
Jane,25,San Francisco`;

const json = CSVToJSON(csvData);
console.log(json);
// Output: [
//   { name: "John", age: "30", city: "New York" },
//   { name: "Jane", age: "25", city: "San Francisco" }
// ]
```

#### Python
```python
from json_csv_converter import JSONToCSV, CSVToJSON

# JSON to CSV
json_data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "San Francisco"}
]

csv_output = JSONToCSV(json_data)
print(csv_output)

# CSV to JSON
csv_data = """name,age,city
John,30,New York
Jane,25,San Francisco"""

json_output = CSVToJSON(csv_data)
print(json_output)
```

## Advanced Usage

### Handling Nested JSON
```javascript
const nestedData = [
  {
    name: "John",
    address: {
      street: "123 Main St",
      city: "New York",
      coordinates: { lat: 40.7128, lon: -74.0060 }
    },
    hobbies: ["reading", "swimming"]
  }
];

// Flatten nested objects
const csv = JSONToCSV(nestedData, { flatten: true });
// Columns: name, address.street, address.city, address.coordinates.lat, address.coordinates.lon, hobbies
```

### Custom Field Mapping
```javascript
const options = {
  fieldMap: {
    'Full Name': 'name',
    'Years Old': 'age',
    'Location': 'city'
  }
};

const csv = JSONToCSV(jsonData, options);
// Columns: Full Name, Years Old, Location
```

### Configuration Options

#### JSON to CSV Options
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `delimiter` | string | `,` | Field delimiter |
| `quote` | string | `"` | Quote character |
| `escape` | string | `"` | Escape character |
| `header` | boolean | `true` | Include header row |
| `flatten` | boolean | `false` | Flatten nested objects |
| `arrayDelimiter` | string | `;` | Delimiter for array values |
| `fieldMap` | object | `{}` | Custom field name mapping |

#### CSV to JSON Options
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `delimiter` | string | `,` | Field delimiter |
| `quote` | string | `"` | Quote character |
| `escape` | string | `"` | Escape character |
| `header` | boolean | `true` | First row contains headers |
| `nest` | boolean | `false` | Create nested objects from dot notation |
| `autoType` | boolean | `false` | Automatically convert data types |

## Examples

### Example 1: Simple Data
**Input JSON:**
```json
[
  {"id": 1, "name": "Alice", "email": "alice@example.com"},
  {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
```

**Output CSV:**
```csv
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
```

### Example 2: Nested Objects
**Input JSON:**
```json
[
  {
    "user": {
      "id": 1,
      "profile": {
        "name": "Alice",
        "age": 30
      }
    },
    "preferences": ["email", "sms"]
  }
]
```

**Output CSV (flattened):**
```csv
user.id,user.profile.name,user.profile.age,preferences
1,Alice,30,"email;sms"
```

### Example 3: Complex Nested Structure
**Input CSV:**
```csv
user.id,user.name,user.address.city,user.address.country,tags
1,John,New York,USA,"developer;javascript"
2,Jane,London,UK,"designer;css"
```

**Output JSON (nested):**
```json
[
  {
    "user": {
      "id": "1",
      "name": "John",
      "address": {
        "city": "New York",
        "country": "USA"
      }
    },
    "tags": ["developer", "javascript"]
  },
  {
    "user": {
      "id": "2",
      "name": "Jane",
      "address": {
        "city": "London",
        "country": "UK"
      }
    },
    "tags": ["designer", "css"]
  }
]
```

## Error Handling

The converter includes comprehensive error handling:

```javascript
try {
  const result = JSONToCSV(invalidData);
} catch (error) {
  if (error.type === 'ValidationError') {
    console.error('Invalid input data:', error.message);
  } else if (error.type === 'ConversionError') {
    console.error('Conversion failed:', error.message);
  }
}
```

Common error types:
- `ValidationError`: Invalid input format or structure
- `ConversionError`: Failed to convert between formats
- `FileError`: File read/write errors (CLI usage)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/holly-copilot-pro-plus/test.git
cd test
npm install  # or pip install -e .
npm test     # or pytest
```

### Running Tests
```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- tests/json-to-csv.test.js
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📧 **Email**: support@jsoncsv-converter.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/holly-copilot-pro-plus/test/issues)
- 📖 **Documentation**: [Full Documentation](https://docs.jsoncsv-converter.com)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/holly-copilot-pro-plus/test/discussions)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## Roadmap

- [ ] Support for XML conversion
- [ ] Web-based converter interface
- [ ] Streaming support for large files
- [ ] Schema validation
- [ ] Custom transformation functions
- [ ] Database import/export integration

---

**Made with ❤️ by the JSON-CSV Converter Team**
