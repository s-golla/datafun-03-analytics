
# datafun-03-analytics

A Python analytics project using a virtual environment (`venv`).

## Project Setup

1. **Create and activate the virtual environment:**
	```powershell
	python -m venv venv
	.\venv\Scripts\Activate
	```
2. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```


## Project Structure
- `venv/` — Virtual environment directory
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
- `sgolla_get_csv.py`, `sgolla_get_excel.py`, `sgolla_get_json.py`, `sgolla_get_text.py` — Scripts to fetch data in various formats
- `sgolla_process_csv.py`, `sgolla_process_excel.py`, `sgolla_process_json.py`, `sgolla_process_text.py` — Scripts to process data in various formats
- `sgolla_run_all_data_tasks.py` — Script to run all get and process functions in sequence
- `utils_logger.py` — Logging utility
- `get_data/` — Folder for fetched data
- `logs/` — Log files


## Usage

### Run All Data Tasks

To fetch and process all data in one step, run:

```powershell
python sgolla_run_all_data_tasks.py
```

This script will sequentially call all "get" and "process" functions for CSV, Excel, JSON, and text data.

### Individual Scripts

You can also run each script individually, for example:

```powershell
python sgolla_get_csv.py
python sgolla_process_csv.py
```

Update `requirements.txt` as you add dependencies.


