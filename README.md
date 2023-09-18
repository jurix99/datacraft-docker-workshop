# DATACRAFT x EKIMETRICS Outbreak Forecasting App

This project provides a simple web application for outbreak forecasting. The application is built using Python and Gradio for the interface. It can be run in a Docker container for ease of deployment.

## Table of Contents

- [DATACRAFT x EKIMETRICS Outbreak Forecasting App](#datacraft-x-ekimetrics-outbreak-forecasting-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Local development](#local-development)
    - [Docker](#docker)
    - [docker-compose](#docker-compose)
  - [Files Descriptions](#files-descriptions)
    - [`Dockerfile`](#dockerfile)
    - [`docker-compose.yml`](#docker-composeyml)
    - [`main.py`](#mainpy)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Clone this repository:

   ``` sh
   git clone https://github.com/yourusername/datacraft-docker-workshop.git
   ```

2. Navigate to the project directory:

   ``` sh
   cd datacraft-docker-workshop
   ```

## Usage

### Local development

We recommend using [Poetry](https://python-poetry.org/) to manage local environment.

Upon installation of Poetry, start the environment and install the dependencies :

``` sh
poetry shell
poetry install
```

To run the app locally :

``` sh
poetry run gradio ./app/datacraft.py
```

Your app should run on <http://localhost:8080/>.

### Docker

Building the app :

``` sh
docker build . -t datacraft
```

Running the app :

``` sh
docker run -dp 8080:8080 datacraft
```
Access the app on your browser using http://localhost:8080/.

### docker-compose

Build the Docker image:

``` sh
docker-compose build
```

Run the Docker container:

``` sh
docker-compose up
```

After starting the container, the Gradio interface will be available at [http://localhost:8080](http://localhost:8080).

## Files Descriptions

### `Dockerfile`

- Sets up the Python environment and installs dependencies
- Copies the necessary files and sets up the application

### `docker-compose.yml`

- Defines the services, networks, and volumes for the Docker container
- Specifies the image, build context, and ports

### `main.py`

- Python script that utilizes Gradio to create a web interface for the outbreak forecasting model
- Defines the inputs and outputs for the Gradio interface

``` sh
├── Dockerfile
├── docker-compose.yml
├── app
│   ├── datacraft.py # Main file that runs the app
│   └── utils
│       └── outbreak.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

MIT
