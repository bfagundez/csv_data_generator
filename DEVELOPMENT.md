To run the project locally:

Create a virtualenv:
```
virtualenv venv
```
Activate
```
source venv/bin/activate
```

Install all packages:
```
pip install -r requirements.txt
```

Run tests:

Install test requirements with
```
pip install -e ".[test]"
```

Then 
```
pytest
```

Install the CLI app to test it manually:
```
pip install -e .
```

This allows you to just run the cli command:
```
csv-data-gen
```
