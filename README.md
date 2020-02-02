#### About
A REST API (only GET requests) for some purpose...

#### Requirements
##### Strictly required
* Python 3.6+
* Flask

##### Extra
* pytest (for testing)

#### How to Setup
Assumption: **python** points to **python3**

##### Method 1: Using poetry
* Install [poetry](https://python-poetry.org/docs/)
by ``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`` in  Linux/MacOS\

``(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python`` in Windows
* Clone the project and setup virtual environment
* If not interested in running tests and installing additional dev tools, run instead ``poetry install --no-dev`` below
```
git clone https://github.com/nicolaskyejo/maji_ya_mchicha.git
cd maji_ya_mchicha
poetry install
poetry shell
cd flask_app
flask run
```


##### Method 2: Using virtualenv/requirements.txt

```
git clone https://github.com/nicolaskyejo/maji_ya_mchicha.git
cd maji_ya_mchicha
python -m venv backend
```

###### Linux/MacOS
```
$ source backend/bin/activate
$ pip install -r requirements.txt  # requirements-dev.txt if you want to run tests
$ cd flask_app
$ flask run
```

###### In Windows
```
PS > backend\scripts\activate.ps1
PS > pip install -r requirements.txt  # requirements-dev.txt if you want to run tests
PS > cd flask_app
PS > flask run
```

#### How to run tests
Navigate to **tests** directory
```
cd tests
pytest
```

#### Sending requests
Requests are sent to **localhost:5000/restaurants/search**

Parameters:
* q = query string
* lat = latitude
* lon = longitude

You can send requests using [postman](https://www.getpostman.com/), your web browser or cURL

```
curl 'http://127.0.0.1:5000/restaurants/search?q=veg&lat=24.94&lon=60.17'
```

