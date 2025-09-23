from flask import jsonify

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

