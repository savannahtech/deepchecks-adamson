# DeepChecks Backend Developer Assignment
This project is a FastAPI application for handling interactions and alerts. It includes endpoints for creating interactions, uploading CSV files to create multiple interactions, and retrieving alerts.
## Project Structure
```
deepchecks/
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── alert_controller.py
│   │   ├── interaction_controller.py
│   │   ├── metrics_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── alert.py
│   │   ├── interaction.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── alert_routes.py
│   │   ├── interaction_routes.py
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
└── tests/
    ├── __init__.py
    ├── test_alerts.py
    ├── test_interactions.py
```

## Installation
### Using Docker
1. Clone the repository:
    ```
    git clone https://github.com/BryanAdamson/deepchecks.git
    cd deepchecks
    ```
2. Build the Docker image:
    ```
    docker build -t deepchecks_app .
    ```
3. Run the Docker container:
    ```
    docker run -d -p 8000:8000 deepchecks_app
    ```
   
### Using Docker Compose (Optional)
1. Ensure docker-compose.yml is in the root of your project directory.
2. Build and start the services:
    ```
    docker-compose up --build
    ```
 The application will be available at http://127.0.0.1:8000.

### Without Docker
1. Clone the repository:
    ```
    git clone https://github.com/BryanAdamson/deepchecks.git
    cd deepchecks
    ```
2. Create a virtual environment and activate it:
    ```
    python -m venv env
    source env/bin/activate
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Start the FastAPI application:
    ```
    uvicorn app.main:app --reload
    ```
The application will be available at http://127.0.0.1:8000.

## Endpoints

### Interactions
- #### POST api/interactions/bulk<br>
  Accepts a CSV file containing interactions data, processes each row to calculate metrics, stores them in the database, and creates alerts based on predefined conditions.
  #### Request Body:
    ```
    Form-data with a single file field named `csv_file` containing the CSV file.
    ```
  #### Response:
    ```
    {
        "success": true,
        "data": null,
        "message": "Processing..."
    }
    ```
  
- #### POST api/interactions<br>
  Creates a new interaction and calculates the metrics.<br>
  #### Request Body:
    ```
    {
        "input_text": "string",
        "output_text": "string"
    }
    ```
  #### Response:
    ```
    {
        "success": true,
        "data": null,
        "message": "Processing..."
    }
    ```
  
### Alerts
- #### GET api/alerts<br>
  Gets all the alerts in the system.<br>
 
  #### Response:
    ```
    {
        "success": true,
        "data": [
            {
                "id": 1,
                "interaction_id": 1,
                "element": "input" | "output",
                "metric_value": float,
                "alert_type": "threshold" | "outlier"
            }
        ],
        "message: "Action Successful"
    }
    ```
- #### GET api/alerts?interaction_id=2<br>
  Gets all the alerts for a specific interaction.<br>
 
  #### Response:
    ```
    {
        "success": true,
        "data": [
            {
                "id": 1,
                "interaction_id": 2,
                "element": "input" | "output",
                "metric_value": float,
                "alert_type": "threshold" | "outlier"
            }
        ],
        "message: "Action Successful"
    }
    ```
  
## Tests
To run the tests, use:
    ```
    pytest
    ```

## File Descriptions
- **requirements.txt**: List of dependencies required for the project.
- **app/**: Directory containing the main application code.
  - **controllers/**: Directory containing the controller logic for handling requests.
    - **init.py**: Initializes the controllers module.
    - **alert_controller.py**: Logic for retrieving alerts.
    - **interaction_controller.py**: Logic for creating interactions and processing CSV files.
    - **metrics_controller.py**: Logic for calculating metrics.
  - **models/**: Directory containing the SQLAlchemy models.
    - **init.py**: Initializes the models module.
    - **alert.py**: Defines the Alert model.
    - **interaction.py**: Defines the Interaction model.
  - **routes/**: Directory containing the API route definitions.
    - **init.py**: Initializes the routes module.
    - **alert_routes.py**: Defines the API routes for alerts.
    - **interaction_routes.py**: Defines the API routes for interactions.
  - **init.py**: Initializes the app module.
  - **database.py**: Sets up the database connection and session.
  - **main.py**: Entry point for the FastAPI application.

- **tests/**: Directory containing test cases.
  - **init.py**: Initializes the tests module.
  - **test_alerts.py**: Tests for the alert logic.
  - **test_interactions.py**: Tests for the interaction logic.

