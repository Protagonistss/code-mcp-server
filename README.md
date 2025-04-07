# MCP Server

A Model-Controller-Provider (MCP) architecture based server implementation using FastAPI.

## Project Structure

```
.
├── api/              # API routes and endpoints
│   └── v1/          # API version 1
│       ├── __init__.py
│       └── items.py # Item endpoints
├── controllers/      # Business logic and request handlers
│   └── item_controller.py
├── providers/       # Data access and external service integrations
│   └── item_provider.py
├── models/         # Data models and database schemas
│   └── item.py
├── core/          # Core configurations and utilities
│   ├── config.py  # Application configuration
│   └── database.py # Database configuration
├── main.py        # Application entry point
├── requirements.txt # Project dependencies
├── environment.yml  # Conda environment file
└── README.md      # Project documentation
```

## Features

- **FastAPI-based REST API**: High-performance, easy to use, fast to code
- **MCP Architecture**:
  - Models: Data structures and database schemas
  - Controllers: Business logic and request handling
  - Providers: Data access and external service integration
- **Modern Tech Stack**:
  - SQLAlchemy for ORM
  - Pydantic for data validation
  - FastAPI for API framework
  - SQLite for development database
- **API Features**:
  - Automatic OpenAPI documentation
  - Request validation
  - Response serialization
  - CORS middleware
  - Type checking

## Setup

1. Create a Conda environment:
```bash
# Create a new environment with Python 3.12
conda create -n codeMcpServer python=3.12
# Activate the environment
conda activate codeMcpServer
```

2. Install dependencies:
```bash
# Using the provided environment file (recommended)
conda env create -f environment.yml

# OR using pip 
pip install -r requirements.txt

# OR using conda with conda-forge channel
conda config --add channels conda-forge
conda install --file requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## Dependencies

Key dependencies in this project:
- Python 3.12.9
- FastAPI 0.112.2
- SQLAlchemy 2.0.37
- Pydantic 2.11.2
- Uvicorn 0.32.1
- Python-dotenv 0.21.0

For a complete list, see `environment.yml` or `requirements.txt`.

## Environment Management

### Export Environment
To export your environment for sharing:
```bash
# Export full environment with exact versions (without prefix)
conda env export | grep -v "^prefix: " > environment.yml

# Or export only manually installed packages
conda env export --from-history > environment.yml
```

### Import Environment
To recreate an environment from the exported file:
```bash
conda env create -f environment.yml
```

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Items API (`/api/v1/items`)

- `GET /api/v1/items/`: List all items
- `GET /api/v1/items/{item_id}`: Get a specific item
- `POST /api/v1/items/`: Create a new item
- `PUT /api/v1/items/{item_id}`: Update an item
- `DELETE /api/v1/items/{item_id}`: Delete an item

## Development

### Project Organization

The project follows the MCP (Model-Controller-Provider) pattern:

- **Models**: Define data structures and database schemas
- **Controllers**: Handle business logic and request processing
- **Providers**: Manage data access and external service integration

### Adding New Features

1. Create the model in `models/`
2. Create the provider in `providers/`
3. Create the controller in `controllers/`
4. Create the API endpoints in `api/v1/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the terms of the LICENSE file included in the repository. 