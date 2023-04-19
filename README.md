# Data-Engineering-Learning-Game
This is a text-based game developed with Python to help users learn data engineering concepts.

## Project Description

This project provides a collection of scenarios for demonstrating the use of various data engineering concepts and tools using Python. All scenarios are run in the same Docker container, allowing for easy installation and setup.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Built With](#built-with)
- [License](#license)

## Getting Started

To get started, clone this repository and navigate to the root directory of the project. Then, build the Docker image using the following command:

    docker build -t data-engineering-learning-game .

After the Docker image is built, run the container using the following command:

    docker run -it data-engineering-learning-game

This will start the game, and you can begin playing and exploring the different scenarios.

## Usage

This project provides a text-based game that allows users to interact with different scenarios and learn data engineering concepts. To use the project, simply run the Docker container using the instructions provided above, and follow the instructions provided in the game.

## Built With

This project was built using Python 3.8 and the following libraries:

- PySpark
- Dask
- Faker

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
