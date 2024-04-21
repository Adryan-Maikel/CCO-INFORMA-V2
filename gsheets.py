from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build as get_sheet

CREDS = Credentials.from_service_account_file("credentials.json", scopes=[
    "https://www.googleapis.com/auth/spreadsheets"])
SERVICE = get_sheet("sheets", "v4", credentials=CREDS)
SHEETID = "1ZqJfSMkqz2ywSmNjw_r_bTgr9QxP6IgiilMdyIim8II"


def get_data():
    range_name = "teste!A:B"

    sheet = SERVICE.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEETID, range=range_name)\
        .execute()
    return result.get("values", [])


def add_peaple(name, id_cracha):
    request = SERVICE.spreadsheets().values().append(
        spreadsheetId=SHEETID, range="teste!A:B", valueInputOption="RAW",
        body={"values": [[name, id_cracha]]})
    # copy(name)
    request.execute()


def del_peaple(row_id: int):
    sheets = SERVICE.spreadsheets().get(spreadsheetId=SHEETID).execute()\
        .get('sheets', [])
    for sheet in sheets:
        if sheet["properties"]["title"] == "teste":
            sheet_id = sheet['properties']['sheetId']
            break

    if sheet_id is None:
        return

    request_body = {"requests": [{"deleteDimension": {"range": {
        "sheetId": sheet_id, "dimension": "ROWS",
        "startIndex": row_id, "endIndex": row_id + 1}}}]}
    SERVICE.spreadsheets().batchUpdate(spreadsheetId=SHEETID,
                                       body=request_body).execute()


if __name__ == "__main__":
    print(get_data())
    add_peaple("teste", 0)
