# Installation  
  
## What You Will Learn  
  
- Install CalagoAPI  
- Check that Python can import the package  
- Keep panel credentials out of example source  
  
## Prerequisites  
  
[00 Introduction](00_Introduction.md). Python 3.9 or newer and a terminal.  
  
## Estimated Time  
  
10 minutes  
  
## Concepts Introduced  
  
- Python package installation  
- Importing a library  
- Environment variables for configuration  
  
## Concept Explanation  
  
CalagoAPI is installed into the same Python environment that runs your script.  
If you use a virtual environment, activate it before installing. The SDK needs  
Python 3.9+ and installs its runtime dependencies through pip.  
  
## API Explanation  
  
The public entry point is `Panel`, imported with `from calagoapi import Panel`.  
Importing the class does not connect to a panel; a connection is created only  
when you instantiate it in the next lesson.  
  
## Install and Verify the Import  
  
```bash  
python -m pip install calagoapi  
python -c "from calagoapi import Panel; print(Panel)"  
```  
  
For a checkout of this repository, `python -m pip install -e .` installs the  
working tree in editable mode.  
  
Run pip through the same interpreter that will run your script. From a  
repository checkout, use `python -m pip install -e .` instead. The import check  
prints `Panel`; it confirms installation only, not connectivity to a panel.  
  
## Common Mistakes  
  
- Installing into one Python environment and running another. Use the same  
  interpreter for pip and your script.  
- Expecting an import to verify panel connectivity. It only verifies that the  
  package is installed and importable.  
  
## What You Learned  
  
- CalagoAPI installs with pip and supports Python 3.9+.  
- `Panel` is the package's main synchronous entry point.  
- Installation and connecting are separate steps.  
  
## Continue Learning  
  
Next: [02 Creating a Panel](02_Creating_A_Panel.md)  
  
## Navigation  
  
Previous: [00 Introduction](00_Introduction.md)  
Next: [02 Creating a Panel](02_Creating_A_Panel.md)  
Reference Docs: [Getting started](../reference/getting-started.md)  
Related Examples: Code examples are embedded in this walkthrough.