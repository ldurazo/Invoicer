This is a personal tool to automate the process of invoice making.

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

Change values to your heart's content. Be aware that start and end dates do not count weekends, and the configuration is inclusive of start but not end.

e.g. the following configuration will calculate all business days up to March 15, without counting March 16.
```
INVOICE_START_DATE = "2000/3/1"
INVOICE_END_DATE = "2000/3/16"
```

Run with
```
python3 main.py
```

PDF should be inside a directory called `out`

![Screen Shot 2022-03-14 at 12 27 55](https://user-images.githubusercontent.com/7563640/158246554-d37e9c28-50ee-4f33-8988-a411c588388f.png)
