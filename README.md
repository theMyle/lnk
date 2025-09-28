# lnk

A simple Windows CLI utility for creating shortcuts (.lnk files).

## Features

- Create shortcuts to files or directories
- Custom shortcut names
- Simple command-line interface
- Windows-only (uses Windows COM objects)

## Installation

**Recommended:** Using [uv](https://github.com/astral-sh/uv) for global installation

```bash
uv tool install git+https://github.com/theMyle/lnk.git
```

This installs `lnk` as a global command available from anywhere.

**Alternative:** Using pip

```bash
pip install git+https://github.com/theMyle/lnk.git
```

## Usage

### Basic Usage

```bash
lnk <source> <destination>
```

### Examples

```bash
# Create shortcut to a file
lnk C:\path\to\file.txt C:\Desktop\
# Results in: C:\Desktop\file.lnk

# Create shortcut to a folder  
lnk C:\MyFolder C:\Desktop\
# Results in: C:\Desktop\MyFolder.lnk

# Create shortcut with custom name
lnk C:\path\to\file.txt C:\Desktop\ --output "My Custom Shortcut"
# Results in: C:\Desktop\My Custom Shortcut.lnk
```

### Options

- `source` - Path to the file or directory to create a shortcut for
- `destination` - Directory where the shortcut will be created  
- `--output` - Custom name for the shortcut (optional)

## Requirements

- Windows (Windows 10/11 recommended)
- Python 3.12+

## Development

```bash
# Clone the repository
git clone https://github.com/theMyle/lnk.git
cd lnk

# Install in development mode
uv pip install -e .

# Run locally
uv run lnk --help
```

## License

MIT License