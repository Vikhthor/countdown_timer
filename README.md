## Countdown Timer

A Django Coutdown Timer Web App

The app is currently on AWS and you can reach it via http://ec2-54-146-231-154.compute-1.amazonaws.com/

#### Installation

Clone the app from Github

```
git clone https://github.com/Vikhthor/countdown_timer.git
```

Change directory to the cloned app directory

```
cd countdown_timer
```

It is recommended that you setup and activate a virtual python environment

```
sudo apt-get update
sudo apt install python3.12-venv
python3 -m venv env
source env/bin/activate
```

Install dependency Python packages

```
python install -r requirements.txt
```

Start the web server

```
python manage.py runserver 
```

Once the web server is running, you can reach it on the web browser via localhost and port 8000 e.g 127.0.0.1:8000