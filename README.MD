# Azure pipeline experiments
Just experimenting with azure pipelines with this very simple app that plots data for a single lap of an F1 season. Can't be asked to do anything fancier than this.

## How to run the app
Using venv:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
.venv/bin/python app.py
```

Using pipenv:
```sh
pipenv sync
source .venv/bin/activate
.venv/bin/python app.py
```

With docker, the source code shoud live outside of the docker image, so you don't have to rebuild it if you change the code or if you don't add any extra libraries to the requirements:
```sh
docker build -t fastf1:latest .
docker run -d -p 8050:8050 fastf1:latest
```