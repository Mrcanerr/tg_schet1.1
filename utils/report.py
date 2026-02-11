from openpyxl import Workbook
from datetime import datetime

def create_report(rows):
    wb = Workbook()
    ws = wb.active
    ws.title = "Отчет"

    ws.append(["Товар", "Пришло", "В базе", "Разница"])

    for r in rows:
        ws.append([
            r["name"],
            r["new"],
            r["old"],
            r["diff"]
        ])

    now = datetime.now()
    filename = f"uchet_tovara_{now.strftime('%d.%m.%Y_%Hh%Mm')}.xlsx"

    wb.save(filename)
    return filename
