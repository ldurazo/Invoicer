This is a personal tool to automate the process of invoice making. Software comes with no guarantees of any kind.

### Installation guide:

Preferably initiate a virtual env in the root folder
```
python3 -m venv env && source env/bin/activate
```

Install dependencies
```
pip3 install -r requirements.txt
```

Copy the contents of `configuration.example.py` into a file named `configuration.py`

Run with
```
python3 main.py
```

PDF should be inside a directory called `out`