from .use_service_account import get_sheet_dict

sheet = get_sheet_dict()

def add_new_content(content): # content type is List
    last_row = len(sheet.get_all_values())
    sheet.update(f"A{last_row+1}:J{last_row+1}", [content])

def find_cell(keyword):
    cell = sheet.find(keyword)
    return cell

def update_status_content(keyword: str, value: str): # keyword:String, value:String
    if not keyword:
        return

    cell = find_cell(keyword)
    col_for_status = 8
    if cell:
        row_number = cell.row
        sheet.update_cell(row_number, col_for_status, value)

