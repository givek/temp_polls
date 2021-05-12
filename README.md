## Temp Polls

Temp Polls is a polling web application to create temporary polls

## Technologies

- Django 2.2
- Python 3.8
- HTML 5
- CSS 3
- JavaScript (ES6+)

## Installation

1. Create a local copy of this git repository with `git clone` command.

   ```shell
   $ git clone https://github.com/givek/temp_polls.git
   ```

2. Create a Virtual Enviornment with the `venv` module.

   ```shell
   $ python3 -m venv venv
   ```

3. Once you’ve created a virtual environment, you may activate it.

   ```shell
   $ source venv/bin/activate
   ```

4. Now, install the requirements from the `requirements.txt` file.

   ```shell
   $ pip install -r requirements.txt
   ```

5. Now, apply the migrations with the management command.

   ```shell
   $ python manage.py migrate
   ```

6. Finally, start the developement server with the management commnad.

   ```shell
   $ python manage.py runserver
   ```

## **Authors**

- Vivek Gandharkar - *Initial work* - [givek](https://github.com/givek)

## **License**

This project is licensed under the MIT License - see the [LICENSE.md](../blob/main/LICENSE) file for details
