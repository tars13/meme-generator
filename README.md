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

1. Start web server
```shell
python3 app.py
```
2. Access the application using the next url http://127.0.0.1:5000/ you will see a meme being generated and display
in your browser. The meme is generated randomly, the meme engine will select an image, a quote, and the author randomly
tou can pres F5 and every time a new meme will be generated.

# Overview

The application has the next modules

1. QEngine, this module has all the ingestors, an ingestor will extract quotes from PDF, text files, Docx files and CSV files.
Every ingestor will implement the parse method.
   
2. MemeEngine will use 
   - all the ingestors to create the quotes
   - Pillow library to load, add the text to the image and save the image to the disk
   
3. app.py is the web application and will use QEngine and MemeEngine to provide the web server to create the memes.
4. meme.py is the cli application and will use QEngine and MemeEngine to provide the web server to create the memes, we use
argsparse module to create the optional arguments of the command.

## Requirements
* pandas
* flask
* requests
* python-docx
