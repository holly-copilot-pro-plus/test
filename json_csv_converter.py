#!/usr/bin/env python3
"""
JSON-CSV Converter
A simple and efficient tool for converting between JSON and CSV formats.
"""

import json
import csv
import sys
from typing import List, Dict, Any, Union
from pathlib import Path


class JSONCSVConverter:
    """
    A class to handle conversions between JSON and CSV formats.
    
    Supports:
    - JSON array of objects to CSV
    - CSV to JSON array of objects
    - Flat and nested JSON structures (with configurable depth)
    """
    
    def __init__(self, flatten_nested: bool = True, delimiter: str = ','):
        """
        Initialize the converter.
        
        Args:
            flatten_nested: Whether to flatten nested JSON objects (default: True)
            delimiter: CSV delimiter character (default: ',')
        """
        self.flatten_nested = flatten_nested
        self.delimiter = delimiter
    
    def json_to_csv(self, json_data: Union[str, List[Dict], Path], 
                    output_file: Union[str, Path]) -> None:
        """
        Convert JSON data to CSV format.
        
        Args:
            json_data: JSON string, list of dictionaries, or path to JSON file
            output_file: Path to output CSV file
            
        Raises:
            ValueError: If JSON data is not in expected format
            IOError: If file operations fail
        """
        # Load JSON data
        if isinstance(json_data, (str, Path)):
            with open(json_data, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = json_data
        
        if not isinstance(data, list):
            raise ValueError("JSON data must be an array of objects")
        
        if not data:
            raise ValueError("JSON data is empty")
        
        # Validate all items are dictionaries
        for idx, item in enumerate(data):
            if not isinstance(item, dict):
                raise ValueError(f"Item at index {idx} is not a dictionary object")
        
        # Flatten nested structures if enabled
        if self.flatten_nested:
            data = [self._flatten_dict(item) for item in data]
        
        # Get all unique keys across all objects
        fieldnames = set()
        for item in data:
            fieldnames.update(item.keys())
        fieldnames = sorted(list(fieldnames))
        
        # Write to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(data)
    
    def csv_to_json(self, csv_file: Union[str, Path], 
                    output_file: Union[str, Path],
                    unflatten: bool = False) -> None:
        """
        Convert CSV data to JSON format.
        
        Args:
            csv_file: Path to input CSV file
            output_file: Path to output JSON file
            unflatten: Whether to unflatten keys with dots (default: False)
            
        Raises:
            IOError: If file operations fail
        """
        data = []
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=self.delimiter)
            for row in reader:
                if unflatten:
                    row = self._unflatten_dict(row)
                data.append(row)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _flatten_dict(self, d: Dict[str, Any], parent_key: str = '', 
                     sep: str = '.') -> Dict[str, Any]:
        """
        Flatten a nested dictionary.
        
        Args:
            d: Dictionary to flatten
            parent_key: Parent key for recursion
            sep: Separator for nested keys
            
        Returns:
            Flattened dictionary
        """
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Convert lists to JSON strings for CSV compatibility
                items.append((new_key, json.dumps(v)))
            else:
                items.append((new_key, v))
        return dict(items)
    
    def _unflatten_dict(self, d: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
        """
        Unflatten a dictionary with dotted keys.
        
        Args:
            d: Dictionary to unflatten
            sep: Separator used in keys
            
        Returns:
            Unflattened dictionary
        """
        result = {}
        for key, value in d.items():
            parts = key.split(sep)
            current = result
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                elif not isinstance(current[part], dict):
                    # If the current value is not a dict, we can't continue unflattening
                    # Keep the original dotted key instead
                    result[key] = value
                    break
                else:
                    current = current[part]
            else:
                # Try to parse JSON strings back to lists/objects
                if isinstance(value, str) and value.startswith('['):
                    try:
                        value = json.loads(value)
                    except json.JSONDecodeError:
                        pass
                
                current[parts[-1]] = value
        return result


def main():
    """Command-line interface for the JSON-CSV converter."""
    if len(sys.argv) < 4:
        print("Usage: python json_csv_converter.py <command> <input_file> <output_file>")
        print("Commands:")
        print("  json2csv - Convert JSON to CSV")
        print("  csv2json - Convert CSV to JSON")
        print("\nExample:")
        print("  python json_csv_converter.py json2csv data.json data.csv")
        print("  python json_csv_converter.py csv2json data.csv data.json")
        sys.exit(1)
    
    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    converter = JSONCSVConverter()
    
    try:
        if command == "json2csv":
            converter.json_to_csv(input_file, output_file)
            print(f"Successfully converted {input_file} to {output_file}")
        elif command == "csv2json":
            converter.csv_to_json(input_file, output_file)
            print(f"Successfully converted {input_file} to {output_file}")
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
