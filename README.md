# DATACRAFT x EKIMETRICS Outbreak Forecasting App

This project provides a simple web application for outbreak forecasting. The application is built using Python and Gradio for the interface. It can be run in a Docker container for ease of deployment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/datacraft-docker-workshop.git
   ```
   
2. Navigate to the project directory:
   ```
   cd datacraft-docker-workshop
   ```

3. Build the Docker image:
   ```
   docker-compose build
   ```

## Usage

Run the Docker container:
```
docker-compose up
```

After starting the container, the Gradio interface will be available at [http://localhost:8080](http://localhost:8080).

## File Descriptions

### `Dockerfile`

- Sets up the Python environment and installs dependencies
- Copies the necessary files and sets up the application

### `docker-compose.yml`

- Defines the services, networks, and volumes for the Docker container
- Specifies the image, build context, and ports

### `main.py`

- Python script that utilizes Gradio to create a web interface for the outbreak forecasting model
- Defines the inputs and outputs for the Gradio interface

```
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