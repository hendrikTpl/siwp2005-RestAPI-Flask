# siwp2005-RestAPI-Flask

# [SIWP2005]_PBO_Building REST API with Flask

## Requirements
1. Python 3.x
2. PIP
3. Flask
4. VsCode

## Installation

- check apakah pip sudah terinstall atau belum 

```
#Linux/MacOS
python3 -m pip --version
## Windows
py -m pip --version
```
- install pip
```
## Linux/MacOS
python3 -m pip install --upgrade pip setuptools wheel
## Windows
py -m pip install --upgrade pip setuptools wheel
```
- upgrade pip to the latest version
```
python -m pip install --upgrade pip
```
- install Flask
```
python3 -m pip install Flask
```
> Refer to https://pypi.org/project/Flask/

- check flask installation
```
pip list
```

![image](https://hackmd.io/_uploads/SyIG0toQA.png)

## My First Flask

- hello world example. 

    Create a new file named app.py and add the following code:

```
##app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

```

- **Import Flask:** Import the Flask class from the **flask** module.
- **Create an Instance:** Create an instance of the Flask class. This instance will be your WSGI application.
- **Define a Route:** Use the ***@app.route*** decorator to bind the URL **'/'** to the **hello_world** function. When someone visits the root URL of your application, the hello_world function will be called, and its return value will be displayed in the browser.
- **Run the Application:** The if __name__ == '__main__': block ensures that the development server runs only if the script is executed directly (not imported as a module). The **app.run(debug=True)** line starts the development server with debug mode enabled, which is helpful during development.

- then run the flask application with

```
## Linux/MacOS
python3 app.py

## Windows
py -m app.py
```
if it is successfully running, you should see similar to this
![image](https://hackmd.io/_uploads/rk7hfciQ0.png)

- Now, you can open your browser, got 'http://127.0.0.1:5000'. You should be able to see the message `hello, world`

![image](https://hackmd.io/_uploads/BkaOS9oQ0.png)

> Note: by default Flask running on port `5000` In case you want to have customize port and open the ip to public, you can bind the `port` as `any valid port` and `host` as `0.0.0.0`

for example, go back to `app.py` code, then modify this line:
```
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5002,  debug=True)

```

run it again. you should be able to see similar result.

## 
## *Congrats! you just did it the very basic flask example*