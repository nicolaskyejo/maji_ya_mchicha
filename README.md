#### About
A REST API (only GET requests) for some purpose...

#### Requirements
##### Strictly required
* Python 3.6+
* Flask

##### Extra
* pytest (for testing)

#### How to Setup
* Install **poetry** ([link](https://python-poetry.org/docs/))
or just simply ``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python``
* Clone the project and setup virtual environment
```
git clone https://github.com/nicolaskyejo/maji_ya_mchicha.git
cd maji_ya_mchicha
poetry install
```
If not interested in running tests, run instead ``poetry install --no-dev``

#### How to run the application
Set up Flask environment variable
* In Linux
```
$ cd maji_ya_mchicha
$ export FLASK_APP=app.py
$ flask run
```
* In Windows
```
PS > cd maji_ya_mchicha
PS > $env:FLASK_APP= "app.py"
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

