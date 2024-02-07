#NotifyHub

Test task for the company "Solution Factory"

## Functionality

Welcome to NotifyHub, a powerful tool for managing and tracking messaging to your customers.
This project provides a flexible and convenient interface for creating, managing and monitoring mailings, as well as interacting with an external message sending service.

- Creating, updating and deleting clients
- Managing mailings with filters
- Obtaining general and detailed statistics of mailings
- Asynchronous sending of messages with statistics collection
- Handling external service errors without affecting stability


## Requirements

- Python 3.8 or higher (Python 3.11 is preferred)
- Docker, Docker-Compose (to run in a container)

## Run locally

1. Download the project
```bash
git clone https://github.com/geoCrock/NotifyHub.git
```

2. Go to the root of the project (create venv if necessary)
```bash
cd NotifyHub
```

```bash
python -m venv venv
```
or

```bash
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the main file `main.py` to start the project
```bash
main.py
```

The project is available at: http://127.0.0.1:8000
   

## Running via Docker

1. Download the project
  ```bash
git clone https://github.com/geoCrock/NotifyHub.git
```

2. Go to the project root
```bash
cd NotifyHub
```

3. Launch the container
```bash
docker-compose up --build
```
The project is available at: http://127.0.0.1:8000
