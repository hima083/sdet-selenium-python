

Simple API test suite using pytest and requests against the public JSONPlaceholder API.

## How to run
1. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run tests
   ```bash
   pytest --html=reports_api.html
   ```
