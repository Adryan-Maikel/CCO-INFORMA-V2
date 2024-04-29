from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build as get_sheet

CREDS = Credentials.from_service_account_file("credentials.json", scopes=[
    "https://www.googleapis.com/auth/spreadsheets"])
SERVICE = get_sheet("sheets", "v4", credentials=CREDS)

SHEETS = {"informations": "1znsSuDR7dkh_c9M-IMjAHrQ2qqc_Qiq5nFow1QBwEw0",
          "cco-informa": ""}


def get_range(_sheet: str, table_name: str, range: str) -> list:
    VALUES = SERVICE.spreadsheets().values()\
        .get(spreadsheetId=_sheet, range=f"{table_name}!{range}")\
        .execute().get("values", [])
    return VALUES


def del_row(_sheet: str, sheet_name: str, row: int):
    SHEETS = SERVICE.spreadsheets().get(spreadsheetId=_sheet).execute()\
        .get("sheets", [])
    for sheet in SHEETS:
        if sheet["properties"]["title"] == sheet_name:
            SHEET_ID = sheet["properties"]["sheetId"]
            break

    if SHEET_ID is None:
        return

    SERVICE.spreadsheets().batchUpdate(spreadsheetId=_sheet, body={
        "requests": [{"deleteDimension": {
            "range": {"sheetId": SHEET_ID, "dimension": "ROWS",
                      "startIndex": row, "endIndex": row + 1}}}]}).execute()


def add_row(_sheet: str, _range: str, values: list[str]):
    SERVICE.spreadsheets().values().append(
        spreadsheetId=_sheet, range=_range, valueInputOption="RAW",
        body={"values": [values]}).execute()


def update_row(_sheet: str, _range: str, values: list[str]):
    SERVICE.spreadsheets().values()\
        .update(spreadsheetId=_sheet, range=_range, valueInputOption="RAW",
                body={"values": [values]}).execute()


OPERATORS = {
    "get": lambda: get_range(SHEETS["informations"], "Operators", "A2:B"),
    "add": lambda vals: add_row(SHEETS["informations"], "Operators!A:B", vals),
    "del": lambda row: del_row(SHEETS["informations"], "Operators", row),
    "update": lambda vals, row: update_row(
        SHEETS["informations"], f"Operators!A{row}:B{row}", vals)
}
"""\

OPERATORS["get"]()

OPERATORS["add"](["Operador", 153])

OPERATORS["del"](9)

OPERATORS["update"]("Adryan", 153, 1)\
"""


def informations(_sheet: str) -> dict[str]:
    """

    OPERATORS["get"]()

    OPERATORS["add"](["Operador", 153])

    OPERATORS["del"](9)

    OPERATORS["update"]("Adryan", 153, 1)
    """

    return {
        "get": lambda: [_row[0] if _row else ""
                        for _row in get_range(SHEETS["informations"], _sheet,
                                              "A2:B")],
        "add": lambda value:
            add_row(SHEETS["informations"], f"{_sheet}!A:B", value),
        "del": lambda row: del_row(SHEETS["informations"], _sheet, row),
        "update": lambda value, i:
            update_row(SHEETS["informations"], f"{_sheet}!A{i}:B{i}", value)
    }


if __name__ == "__main__":
    print(informations("Sentidos")["get"]())
    # for letter in "A", "B", "C":
    # informations(letter)["add"]("CU")
    # pass
    # informations("C")["del"](14)
    # informations("C")["update"]("CU", 2)
    # print(OPERATORS["get"]())
    # OPERATORS["update"]("Adryan", 154, 1)
