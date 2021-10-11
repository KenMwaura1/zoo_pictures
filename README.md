# zoo_pictures
 A Django project this week will be to develop a personal gallery application that you display your photos for others to see.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FKen_Mwaura1)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FKenMwaura1%2Fzoo_pictures)

![logo](static/images/Zoo-Pictures-Logo.png)
## User stories
As a user of the application I should be able to:

- View different photos that interest me. :heavy_check_mark:
- Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page. :heavy_check_mark:
- Search for different categories of photos. (ie. Travel, Food). :heavy_check_mark:
- Copy a link to the photo to share with my friends. :heavy_check_mark:
- View photos based on the location they were taken. :heavy_check_mark:

## Live Site

[link to deployed site](https://zoo-pictures.herokuapp.com/)

## Setup Instructions / Installation

### Getting Started

### Prerequisites

- Python and pip (I am currently using 3.9.6) Any version above 3.7 should work.
* Git installed on your machine
* Code editor/ IDE

### Installation and Running the App

1. Clone GitHub repository

    ```shell
    git clone https://github.com/KenMwaura1/zoo_pictures
    ```

2. Change into the folder

    ```shell
   cd zoo_pictures
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./bin/activate
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv zoo_pictures
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate zoo_pictures
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```

5. Add your credentials to the `.env` file

6. Migrate your database 
    ```shell
    python manage.py migrate
    ```

7. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

8. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```

9. Run the app

    ```shell
   ./run.sh
    ```

   OR
   run with python

    ```shell
   python manage.py runserver
    ```

## Tests

* To run the tests:

    ```shell
  python manage.py test
    ```

## Technologies used

* Python-3.9.6
* Django web framework
* Bootstrap(Material Bootstrap 4)
* HTML5
* CSS3

## Author

[Ken Mwaura](https://github.com/KenMwaura1)

## LICENSE

MIT License

Copyright (c) 2021 Kennedy Ngugi Mwaura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
