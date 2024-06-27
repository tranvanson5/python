import os
import openpyxl

def read_excel(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"File '{file_path}' not found. Please check the file path.")
            return None

        # Load the workbook
        workbook = openpyxl.load_workbook(file_path)

        # Choose the first sheet
        sheet = workbook.active

        # Get all rows from the sheet
        rows = sheet.iter_rows(values_only=True)

        # Extract headers (first row) and data (remaining rows)
        headers = next(rows)  # Assuming the first row contains headers
        data = [dict(zip(headers, row)) for row in rows]

        return data
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
        return None



