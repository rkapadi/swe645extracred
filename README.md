First, create and activate a virtual environment using the following commands:

```
python3 -m venv venv
source venv/bin/activate
```


Install dependencies with this command:
```
pip install -r requirements.txt
```


Run the application using the following command:
```
uvicorn app.main:app --reload
```

Access the application with this link: http://localhost:8000/api/surveys/
OR to see the FastAPI Documentation, use this link: http://127.0.0.1:8000/docs 