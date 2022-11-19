# Python to-remember sheet

This is kind of like a cheat sheet, but it doesn't include everything; just what I personally need to remember/keep handy.

## Commands

#### Creating a virtual environment

```bash
python3 -m venv <directory>
```

#### Activating virtual environment

```bash
source bin/activate
```

#### Installing 

```bash
pip install <library>

# or 

pip install -r requirements.txt
```

#### Save installed libraries to `requirements.txt`

```bash
pip freeze > requirements.txt
```

## Language

#### Importing

```python
from library import *
from library import someVariable, someMethod, someClass
```

**Exporting**: No need to do anything special

#### File I/O

**Reading everything**:

```python
from pathlib import Path

Path('folder/filename.txt').read_text()
```

**Writing to file**:

```python
with open('readme.txt', 'w') as f:
    f.write('readme')
```

#### Convert HTML to markdown

```python
from markdown import markdown

content_md = "# Some content\n### In MD"
content_html = markdown(content_md, extensions=['fenced_code'])
````
















