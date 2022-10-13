# Wine-master

## Website - business card of the store

## Installing required dependencies

- Place new product images in the `images` folder

- Add a line with a new product to `catalog.xlsx`

- You can create your own product database, for this, take the `catalog.xlsx` file as an example

### Requirements
* Jinja2==3.1.2
* openpyxl==3.0.10
* pandas==1.4.3


     
Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```		
## Application launch

### Open project directory from cmd

```
$ python main.py -p <PATH>
```
<PATH> - path to database `.xlsx`, default it's `catalog.xlsx` 

Open in browser http://127.0.0.1:8000/index.html


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
