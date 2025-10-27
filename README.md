# The Tome of JSON-CSV Transmutation

*"A wizard is never late with his data conversions, nor is he early. He converts precisely when he means to."*

Hail, weary traveler! You have discovered an ancient artifact of great power - a mystical Python incantation capable of transforming JSON scrolls into CSV tablets, and back again! Like the bridge of Khazad-dûm, this tool serves as a passage between two realms of data.

## ✨ The Powers Bestowed Upon This Staff

- **The Gift of Bidirectional Passage**: Much like the Grey Havens, data may flow both ways - from JSON to CSV and back again, as easily as the turning of seasons
- **The Wisdom of Nested Realms**: Flattens the deepest JSON caverns into orderly CSV meadows, bringing hidden treasures to light
- **The Freedom of Configuration**: Bend the delimiters to your will! Choose your path as one chooses between the High Pass or the Mines of Moria
- **The Command of Voices**: Summon its power through mystical command-line incantations or weave it into your Python spellbooks
- **The Strength Against Darkness**: Robust safeguards against corrupted data, with error messages as clear as Galadriel's mirror
- **The Universal Tongue**: Supports all manner of script and symbol with UTF-8, from the Common Speech to the Elvish runes
- **The Blessing of Simplicity**: Requires naught but the Python standard library - no dependencies from distant lands!

## 📜 The Map of This Grimoire

- [Preparing Your Journey](#preparing-your-journey)
- [Your First Incantation](#your-first-incantation)
- [The Art of Transmutation](#the-art-of-transmutation)
  - [Command-Line Sorcery](#command-line-sorcery)
  - [Python Wizardry](#python-wizardry)
- [Tales from the Archives](#tales-from-the-archives)
- [The Ancient Texts (API Scrolls)](#the-ancient-texts-api-scrolls)
- [Advanced Magicks](#advanced-magicks)
- [When Darkness Falls (Error Handling)](#when-darkness-falls-error-handling)
- [Join the Fellowship](#join-the-fellowship)
- [The Covenant](#the-covenant)

## 🗡️ Preparing Your Journey

### What You Must Possess

- Python 3.6 or higher (the basic tools of any wandering wizard)

### The Ritual of Beginning

1. First, summon the repository from the ethereal realm:
```bash
git clone https://github.com/holly-copilot-pro-plus/test.git
cd test
```

2. If you wish, make the scroll executable (optional, like choosing to bring rope):
```bash
chmod +x json_csv_converter.py
```

And lo! Your preparation is complete. This spell requires only the standard Python library - no exotic ingredients from far-off bazaars!

## ⚡ Your First Incantation

### To Transform JSON into CSV

Speak these words of power:

```bash
python3 json_csv_converter.py json2csv input.json output.csv
```

### To Return CSV to JSON

Reverse the transmutation thus:

```bash
python3 json_csv_converter.py csv2json input.csv output.json
```

*"Even the smallest scroll can change the course of the future!"*

## 🧙 The Art of Transmutation

### Command-Line Sorcery

The converter responds to spoken commands, much like the gates of Moria respond to the word "Mellon."

#### The Sacred Formula

```bash
python3 json_csv_converter.py <command> <input_file> <output_file>
```

#### The Words of Power

- `json2csv` - Transforms JSON scrolls into CSV tablets
- `csv2json` - Returns CSV tablets to their JSON form

#### Demonstrations of the Craft

```bash
# Transform a JSON array into the CSV realm
python3 json_csv_converter.py json2csv data.json data.csv

# Restore CSV to its JSON origins
python3 json_csv_converter.py csv2json data.csv data.json
```

### Python Wizardry

For those who wish to weave this magic into their own spellbooks, the converter may be summoned directly in your Python incantations.

#### The Basic Conjuration

```python
from json_csv_converter import JSONCSVConverter

# Summon a converter spirit
converter = JSONCSVConverter()

# Transform JSON to CSV
converter.json_to_csv('input.json', 'output.csv')

# Transform CSV to JSON
converter.csv_to_json('input.csv', 'output.json')
```

#### Advanced Enchantments

```python
from json_csv_converter import JSONCSVConverter

# Customize the converter's behavior, as one might forge a special blade
converter = JSONCSVConverter(
    flatten_nested=True,    # Flatten the nested halls of JSON
    delimiter=';'           # Use the semicolon rune instead of the comma
)

# Apply your custom transmutation
converter.json_to_csv('data.json', 'data.csv')
```

#### Working with the Living Data

```python
from json_csv_converter import JSONCSVConverter

# Convert data that dwells in the realm of memory itself
data = [
    {'name': 'Frodo', 'age': 50, 'homeland': 'The Shire'},
    {'name': 'Aragorn', 'age': 87, 'homeland': 'Gondor'}
]

converter = JSONCSVConverter()
converter.json_to_csv(data, 'fellowship.csv')
```

## 📖 Tales from the Archives

### Chronicle the First: A Simple Array of Objects

**The JSON Scroll** (`people.json`):
```json
[
  {
    "id": 1,
    "name": "Bilbo Baggins",
    "email": "bilbo@shire.me",
    "age": 111
  },
  {
    "id": 2,
    "name": "Gandalf",
    "email": "gandalf@istari.org",
    "age": 2019
  }
]
```

**The Incantation:**
```bash
python3 json_csv_converter.py json2csv people.json people.csv
```

**The Resulting CSV Tablet** (`people.csv`):
```csv
age,email,id,name
111,bilbo@shire.me,1,Bilbo Baggins
2019,gandalf@istari.org,2,Gandalf
```

### Chronicle the Second: Nested Realms Within Realms

**The Layered JSON Scroll** (`users.json`):
```json
[
  {
    "id": 1,
    "name": "Aragorn",
    "dwelling": {
      "street": "Citadel Heights",
      "city": "Minas Tirith",
      "realm": "Gondor"
    }
  }
]
```

**The Transformation Command:**
```bash
python3 json_csv_converter.py json2csv users.json users.csv
```

**The Flattened CSV Tablet** (`users.csv`):
```csv
dwelling.city,dwelling.realm,dwelling.street,id,name
Minas Tirith,Gondor,Citadel Heights,1,Aragorn
```

*See how the nested chambers are brought forth into the light!*

### Chronicle the Third: The Custom Rune Delimiter

```python
from json_csv_converter import JSONCSVConverter

# Employ the tab character, favored in ancient manuscripts
converter = JSONCSVConverter(delimiter='\t')
converter.json_to_csv('data.json', 'data.tsv')
```

### Chronicle the Fourth: The Journey There and Back Again

```python
from json_csv_converter import JSONCSVConverter

converter = JSONCSVConverter()

# Journey from JSON to CSV
converter.json_to_csv('original.json', 'waypoint.csv')

# Return from CSV to JSON, restoring the nested realms
converter.csv_to_json('waypoint.csv', 'restored.json', unflatten=True)
```

## 📚 The Ancient Texts (API Scrolls)

### The JSONCSVConverter Class

*"All we have to decide is what to do with the data that is given to us."*

#### The Summoning Ritual

```python
JSONCSVConverter(flatten_nested=True, delimiter=',')
```

**Sacred Parameters:**
- `flatten_nested` (bool): Whether to flatten nested JSON caverns into the surface realm. Default: `True`
- `delimiter` (str): The rune used to separate fields in CSV. Default: `','`

#### The Methods of Power

##### json_to_csv()

```python
json_to_csv(json_data, output_file)
```

Transforms JSON into the CSV realm.

**Parameters:**
- `json_data`: May be:
  - A path-string to a JSON scroll
  - A `Path` object pointing to JSON
  - A living Python list of dictionaries
- `output_file`: String path or `Path` object for the resulting CSV tablet

**When the Magic Fails:**
- `ValueError`: If the JSON is not an array of objects, or the array is empty as the Desolation of Smaug
- `IOError`: If the scrolls cannot be read or written

**Example Invocation:**
```python
converter = JSONCSVConverter()
converter.json_to_csv('input.json', 'output.csv')
```

##### csv_to_json()

```python
csv_to_json(csv_file, output_file, unflatten=False)
```

Returns CSV data to its JSON origins.

**Parameters:**
- `csv_file`: String path or `Path` object to the CSV tablet
- `output_file`: String path or `Path` object for the restored JSON scroll
- `unflatten` (bool): Whether to rebuild the nested chambers from dotted paths. Default: `False`

**When the Magic Fails:**
- `IOError`: If scrolls cannot be accessed

**Example Invocation:**
```python
converter = JSONCSVConverter()
converter.csv_to_json('input.csv', 'output.json', unflatten=True)
```

## 🔮 Advanced Magicks

### Navigating the Nested Labyrinths

This converter possesses the ancient knowledge to flatten nested JSON structures, much like mapping the many levels of Moria:

```json
{
  "hero": {
    "lineage": {
      "name": "Isildur's Heir"
    }
  }
}
```

Becomes a clear path:
```csv
hero.lineage.name
Isildur's Heir
```

### The Treatment of Arrays

JSON arrays are preserved as mystical JSON strings within CSV, maintaining their essence:

```json
{
  "name": "Legolas",
  "skills": ["archery", "tree-walking", "oliphant-counting"]
}
```

Transforms into:
```csv
name,skills
Legolas,"[""archery"", ""tree-walking"", ""oliphant-counting""]"
```

### Restoring the Ancient Structures

When journeying back from CSV to JSON, you may choose to restore the nested halls:

```python
converter = JSONCSVConverter()
converter.csv_to_json('data.csv', 'data.json', unflatten=True)
```

This transmutes `hero.lineage.name` back into `{"hero": {"lineage": {"name": "..."}}}`

### The Freedom of Delimiters

The converter bends to different runes of separation:

```python
# The Tab rune (favored in ancient tomes)
converter = JSONCSVConverter(delimiter='\t')

# The Semicolon mark (used in the Western lands)
converter = JSONCSVConverter(delimiter=';')

# The Pipe symbol (rare but powerful)
converter = JSONCSVConverter(delimiter='|')
```

## ⚠️ When Darkness Falls (Error Handling)

*"Even the very wise cannot see all ends."*

The converter provides clear portents when troubles arise:

### Invalid JSON Sorcery

```python
# Error: JSON data must be an array of objects
# Your JSON must begin with [ and contain objects within {...}
```

### The Empty Void

```python
# Error: JSON data is empty
# Verify that your scroll contains actual data, not merely blank parchment
```

### The Missing Scroll

```python
# Error: [Errno 2] No such file or directory: 'file.json'
# The path you seek does not exist in this realm
```

### Common Trials and Their Solutions

| The Predicament | The Path Forward |
|-----------------|------------------|
| JSON file is not an array | Wrap your objects in square brackets `[...]` |
| Nested objects won't flatten | Ensure `flatten_nested=True` (the default path) |
| Strange runes in CSV | Fear not, data is automatically quoted when needed |
| Large tomes process slowly | For truly massive scrolls, consider processing in smaller portions |

## 🤝 Join the Fellowship

*"It is no bad thing to celebrate a simple life."* - Yet improvements are always welcome!

### Reporting Dark Omens (Bugs)

1. First, check if the omen has been reported in the [Hall of Issues](https://github.com/holly-copilot-pro-plus/test/issues)
2. If not, inscribe a new issue with:
   - A clear title that names the shadow
   - Steps to summon the problem
   - What you expected vs what actually occurred
   - Sample scrolls (if applicable)

### Proposing New Enchantments (Features)

1. Open an issue bearing the `enhancement` banner
2. Describe the enchantment and its purpose in the realm
3. Provide examples if the vision is clear

### Submitting Your Own Magic (Pull Requests)

1. Fork this repository to your own domain
2. Create a feature branch: `git checkout -b feature/your-amazing-enchantment`
3. Weave your changes
4. Add tests for new powers
5. Ensure all tests pass (let none fail!)
6. Commit your changes: `git commit -m 'Add amazing enchantment'`
7. Push to your fork: `git push origin feature/your-amazing-enchantment`
8. Open a Pull Request back to the main repository

### Guidelines for the Craft

- Follow the PEP 8 style guidelines (the ancient coding laws)
- Add docstrings to new functions and classes
- Include type hints where the path is clear
- Write commit messages that tell the tale
- Update documentation for new features

## 📜 The Covenant

This artifact is bound by the MIT License - a generous covenant indeed:

```
MIT License

Copyright (c) 2025 The Keepers of JSON-CSV Transmutation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this grimoire and associated scrolls (the "Software"), to deal
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

## 🔗 Paths Through Middle-earth

- **The Repository**: [https://github.com/holly-copilot-pro-plus/test](https://github.com/holly-copilot-pro-plus/test)
- **The Hall of Issues**: [https://github.com/holly-copilot-pro-plus/test/issues](https://github.com/holly-copilot-pro-plus/test/issues)
- **The Chronicles**: See the commit history for tales of recent changes

## 🆘 Seeking Wisdom

Should you find yourself lost in the wilderness:

1. Consult the [documentation](#the-map-of-this-grimoire) above
2. Search the [Hall of Issues](https://github.com/holly-copilot-pro-plus/test/issues) for similar troubles
3. Open a new issue describing your predicament in detail

## 🌟 Acknowledgments

- Forged with Python's robust standard library
- Inspired by the eternal need to bridge different realms of data
- Thanks to all wanderers and wizards who have used and improved this tool
- *"The road goes ever on and on..."*

---

**Crafted with wisdom and pipeweed by the Keepers of Data Transmutation**

*"Fly, you data! Fly between formats with grace and speed!"* ✨🧙‍♂️
