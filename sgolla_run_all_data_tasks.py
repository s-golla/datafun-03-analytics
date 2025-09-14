"""
sgolla_run_all_data_tasks.py

This script calls all 'get' and 'process' functions from the project modules.
"""

from sgolla_get_csv import main as get_csv_main
from sgolla_get_excel import main as get_excel_main
from sgolla_get_json import main as get_json_main
from sgolla_get_text import main as get_text_main
from sgolla_process_csv import main as process_csv_main
from sgolla_process_excel import main as process_excel_main
from sgolla_process_json import main as process_json_main
from sgolla_process_text import main as process_text_main


def run_all():
    print("Running all 'get' functions...")
    get_csv_main()
    get_excel_main()
    get_json_main()
    get_text_main()

    print("\nRunning all 'process' functions...")
    process_csv_main()
    process_excel_main()
    process_json_main()
    process_text_main()


if __name__ == "__main__":
    run_all()
