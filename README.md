## Temp Polls

![Preview](../assets/preview.png)

Temp Polls is a simple polling web application to create temporary polls anonymously, it uses browser cookies to store user choice for a particular poll.

## Technologies

- Django 2.2
- Python 3.8
- HTML 5
- CSS 3
- JavaScript (ES6+)

## Getting Started

To get a local copy up and running follow these simple steps:

### Prerequisites

- Python 3.

  ```shell
  $ sudo apt install python3.8
  ```

### Installation

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

## Usage

You may use this project to conduct casual temporary polls.

- Create Poll
  ![Create Poll](../assets/create_poll.png)

- Select Choice
  ![Select Choice](../assets/select_choice.png)

- Results
  ![Results](../assets/results.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

- Vivek Gandharkar - *Initial work* - [givek](https://github.com/givek)

## License

This project is licensed under the MIT License - see the [LICENSE.md](../blob/main/LICENSE) file for details
