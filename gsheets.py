from google.oauth2.service_account import Credentials
from gspread import authorize

CLIENT = authorize(
    Credentials.from_service_account_file("credentials.json", scopes=[
        "https://www.googleapis.com/auth/spreadsheets"]))

SS_DADOS = CLIENT.open_by_key("101ykzDT_qWUN_CzQ4uVyR25hTe6KERvVVOkzSGtbDNk")
WS_DADOS = SS_DADOS.worksheet("Dados")


def get_last_row(col: str) -> int:
    last_row = len(WS_DADOS.col_values("ABCDE".index(col) + 1)) + 1
    if last_row > WS_DADOS.row_count:
        WS_DADOS.add_rows(1)
    return last_row


def add_operator(operator: str, cracha: str) -> None:
    """Função utilizada para adicionar um operador ou um cracha.

    :param operator: str - Operador a ser adicionado na ultima linha.
    :param cracha: str - Cracha a ser adicionado na ultima linha.
    """
    if operator and cracha and cracha.isnumeric():
        operator = operator.strip().title()
        cracha = int(cracha.strip())
        WS_DADOS.update_acell(f"D{get_last_row('D')}", operator)
        WS_DADOS.update_acell(f"E{get_last_row('E')}", cracha)


def update_operator(row: int, operator: str, cracha: str) -> None:
    if operator:
        operator = operator.strip().title()
        WS_DADOS.update_acell(f"D{row}", operator)

    if cracha and cracha.isnumeric():
        cracha = int(cracha.strip())
        WS_DADOS.update_acell(f"E{row}", cracha)


INFORMATIONS = {}
INTERVALS = [["ocorrencias", "A"], ["problemas", "B"], ["sentidos", "C"]]
for name, col in INTERVALS:
    print(name, col)
    INFORMATIONS[name] = {
        "get": lambda _=name, col=col:
            [row[0] for row in WS_DADOS.get_values(f"{col}2:{col}")],
        "add": lambda value, col=col:
            WS_DADOS.update_acell(f"{col}{get_last_row(col)}", value),
        "del": lambda row, col=col:
            WS_DADOS.cut_range(f"{col}{row+1}:{col}", f"{col}{row}: {col}"),
        "upd": lambda row, value, col=col:
            WS_DADOS.update_acell(f"{col}{row}", value)
    }

INFORMATIONS["operadores"] = {
    "get": lambda: WS_DADOS.get_values("D2:E"),
    "add": lambda operator="", cracha="": add_operator(operator, cracha),
    "del": lambda row:
        WS_DADOS.cut_range(f"D{row+1}:E{row+1}", f"D{row}:E{row}"),
    "upd": lambda row, operator, cracha: update_operator(row, operator, cracha)
}


if __name__ == "__main__":
    print(INFORMATIONS["problemas"]["get"]())
    # print(WS_DADOS.get_values("B2:B"))
    pass
