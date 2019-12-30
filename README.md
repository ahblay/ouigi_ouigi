# Ouigi Ouigi (sic) Website

A very simple website. The idea behind this project was to write and deploy a website in one night. The premise is to crowdsource writing, letter by letter. Visitors of the site have 60 seconds to select a letter from A to Z. After the 60 seconds, the letter with the most votes is printed to the screen. The website is located [here](https://ouigi-ouigi.herokuapp.com/). Load times may vary since the website is hosted using the free tier of Heroku.

## Getting Started

Feel free to pull this project and add to/play with it if you feel inclined.

### Prerequisites

The packages you'll need to run this project can be found in requirements.txt. Once you set up your virtual environment (see below), run the following command to install all packages:

```
pip install -r requirements.txt
```

Make sure that you are in the main project directory when you type this command, or include the filepath to requirements.txt.

### Installing

You can set up a virtual environment in the terminal with the command:

```
virtualenv [environment_name]
source [environment_name]/bin/activate
```

All of the packages that are not available natively in python are downloadable using [pip](https://pip.pypa.io/en/stable/).
After setting up your virtual environment, install all the project requirements using the command shown above, or manually with pip:

```
pip install [package_name]
```

## Configuring the Database

This project uses a postgres database. You'll need to manually create a database in postgres with two tables: "letters" and "strings." Letters contains 28 columns: id (integer), datetime (datetime), a (integer), b (integer), c, ..., z. Strings contains 3 columns: id (integer), string (string), datetime (datetime). Once your database is properly configured, navigate to your project directory and export the database URL with the command:

```
export DATABASE_URL=[database_url]
```

## Running

To run the website locally, navigate to the project directory and type:

```
export FLASK_APP=app.py
flask run
```

## Authors

* **Abel Romer** - *Initial work* - [ahblay](https://github.com/ahblay)
