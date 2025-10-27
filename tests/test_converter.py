#!/usr/bin/env python3
"""
Simple tests for JSON-CSV Converter
These tests verify basic functionality of the converter.
"""

import json
import csv
import os
import sys
from pathlib import Path

# Add parent directory to path to import the converter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from json_csv_converter import JSONCSVConverter


def test_json_to_csv():
    """Test JSON to CSV conversion"""
    print("Testing JSON to CSV conversion...")
    
    # Create test data
    test_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    
    # Write test JSON
    test_json = "/tmp/test_input.json"
    test_csv = "/tmp/test_output.csv"
    
    with open(test_json, 'w') as f:
        json.dump(test_data, f)
    
    # Convert
    converter = JSONCSVConverter()
    converter.json_to_csv(test_json, test_csv)
    
    # Verify output
    with open(test_csv, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 2, "Expected 2 rows"
        assert rows[0]['name'] == 'Alice', "First row name mismatch"
        assert rows[1]['name'] == 'Bob', "Second row name mismatch"
    
    print("✓ JSON to CSV conversion passed")
    
    # Cleanup
    os.remove(test_json)
    os.remove(test_csv)


def test_csv_to_json():
    """Test CSV to JSON conversion"""
    print("Testing CSV to JSON conversion...")
    
    # Create test CSV
    test_csv = "/tmp/test_input.csv"
    test_json = "/tmp/test_output.json"
    
    with open(test_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'name', 'age'])
        writer.writeheader()
        writer.writerow({'id': '1', 'name': 'Alice', 'age': '30'})
        writer.writerow({'id': '2', 'name': 'Bob', 'age': '25'})
    
    # Convert
    converter = JSONCSVConverter()
    converter.csv_to_json(test_csv, test_json)
    
    # Verify output
    with open(test_json, 'r') as f:
        data = json.load(f)
        assert len(data) == 2, "Expected 2 objects"
        assert data[0]['name'] == 'Alice', "First object name mismatch"
        assert data[1]['name'] == 'Bob', "Second object name mismatch"
    
    print("✓ CSV to JSON conversion passed")
    
    # Cleanup
    os.remove(test_csv)
    os.remove(test_json)


def test_nested_json():
    """Test nested JSON flattening"""
    print("Testing nested JSON flattening...")
    
    # Create nested test data
    test_data = [
        {
            "id": 1,
            "name": "Alice",
            "address": {
                "city": "NYC",
                "country": "USA"
            }
        }
    ]
    
    test_json = "/tmp/test_nested.json"
    test_csv = "/tmp/test_nested.csv"
    
    with open(test_json, 'w') as f:
        json.dump(test_data, f)
    
    # Convert with flattening
    converter = JSONCSVConverter(flatten_nested=True)
    converter.json_to_csv(test_json, test_csv)
    
    # Verify flattened output
    with open(test_csv, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert 'address.city' in rows[0], "Expected flattened key 'address.city'"
        assert rows[0]['address.city'] == 'NYC', "City value mismatch"
    
    print("✓ Nested JSON flattening passed")
    
    # Cleanup
    os.remove(test_json)
    os.remove(test_csv)


def test_custom_delimiter():
    """Test custom delimiter"""
    print("Testing custom delimiter...")
    
    test_data = [{"id": 1, "name": "Alice"}]
    test_json = "/tmp/test_delim.json"
    test_csv = "/tmp/test_delim.csv"
    
    with open(test_json, 'w') as f:
        json.dump(test_data, f)
    
    # Convert with semicolon delimiter
    converter = JSONCSVConverter(delimiter=';')
    converter.json_to_csv(test_json, test_csv)
    
    # Verify delimiter in output
    with open(test_csv, 'r') as f:
        content = f.read()
        assert ';' in content, "Expected semicolon delimiter"
    
    print("✓ Custom delimiter passed")
    
    # Cleanup
    os.remove(test_json)
    os.remove(test_csv)


def main():
    """Run all tests"""
    print("Running JSON-CSV Converter Tests\n")
    print("=" * 50)
    
    try:
        test_json_to_csv()
        test_csv_to_json()
        test_nested_json()
        test_custom_delimiter()
        
        print("=" * 50)
        print("\n✓ All tests passed!")
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ Error running tests: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
