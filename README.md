# meme_generator

 The meme generator is a fun python 3 application, with this application we can generate a meme using:
- Command line
- [Flask Application](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

The generated meme is made of:
1. A random image
2. A quote, the quote has
    - Author
    - Body
3. Meme generated sample

## Installation
1. Clone this project or fork it
2. Install [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
```shell
python3 -m pip install --upgrade pip
```

```shell
python3 -m pip install --upgrade Pillow
```
3. Install [Python DOCX](https://python-docx.readthedocs.io/en/latest/user/install.html#install)
```shell
pip install python-docx
```
4. Install [xpdfreader](https://www.xpdfreader.com/download.html)
5. Install [Flask](https://pypi.org/project/Flask/)
```shell
pip install -U Flask
```

### As web app

```
python app.py
```

and open http://127.0.0.1:5000/


## Requirements
* pandas
* flask
* requests
* python-docx
