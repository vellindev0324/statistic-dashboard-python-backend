from flask import jsonify
import re

def add_new_content(content, sheet): # content type is List
    last_row = len(sheet.get_all_values())
    sheet.update(f"A{last_row+1}:J{last_row+1}", [content])

def find_cell(keyword, sheet):
    cell = sheet.find(keyword)
    return cell

def update_status_content(keyword: str, value: str, sheet): # keyword:String, value:String
    if not keyword:
        return

    cell = sheet.find(keyword)
    col_for_status = 8

    if cell and keyword:
        row_number = cell.row
        sheet.update_cell(row_number, col_for_status, value)
        return jsonify({"status": "true", "row": row_number, "updated_value": value})
    else:
        return jsonify({"status": "false", "message": "Keyword not found or empty"}), 400

def record_daily_data(date, sheet, content):# content type is List
    # Create a regex pattern that matches today's date, allowing for missing leading zeros
    # Example: For September 24, 2025, the pattern would account for "9/24/2025" and "09/24/2025"
    month_pattern = f"0?{date.month}"  # The '0?' means zero or one occurrence of '0'
    day_pattern = f"0?{date.day}"
    regex_pattern = re.compile(f"{month_pattern}/{day_pattern}/{date.year}")
    matching_cells = sheet.findall(regex_pattern)
    if not date:
        return
    print(matching_cells)
    if not matching_cells:
        last_row = len(sheet.get_all_values())
        sheet.update(f"A{last_row+1}:E{last_row+1}", [content])
    else:
        row_number = matching_cells[0].row
        sheet.update(f"A{row_number}:E{row_number}", [content])

