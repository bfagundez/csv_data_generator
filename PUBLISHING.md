## How to publish this package

Using twine:
```
twine upload --verbose -r <testpypi|pypi> dist/*
```

Credentials are loaded automatically from `~/.pypirc`
File structure for that file is as follows:
```
[pypi]
username = __token__
password = <API TOKEN FROM pypi>
[testpypi]
username = __token__
password = <API TOKEN FROM testpypi>
```

