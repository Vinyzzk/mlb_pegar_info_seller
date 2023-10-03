import pandas as pd
# import openpyxl
import requests
# import os
import time


def get_info():
    time_control = 0

    df = pd.read_excel("mlbs.xlsx")
    column = df["MLB"]
    mlbs = column.values

    mlbs_quantity = len(mlbs)

    data = []

    for mlb in mlbs:
        url = f"https://api.mercadolibre.com/items/{mlb}"
        response = requests.get(url)
        response = response.json()
        seller_id = response["seller_id"]

        url = f"https://api.mercadolibre.com/users/{seller_id}"
        response = requests.get(url)
        response = response.json()
        seller_nickname = response["nickname"]
        seller_permalink = response["permalink"]
        power_seller_status = response["seller_reputation"]["power_seller_status"]

        data.append({"Seller ID": seller_id, "Seller": seller_nickname, "Reputacao": power_seller_status, "Level": "ainda n fiz", "Permalink": seller_permalink})

        time_control += 1

        if time_control % 10 == 0:
            time.sleep(0.5)

    df = pd.DataFrame(data)
    excel_name = "Sellers"
    df.to_excel(f"{excel_name}.xlsx", index=False, engine="openpyxl")
    print(f"[+] Planilha \"{excel_name}\" gerada")
    print("[+] Pressione ENTER para sair")


if __name__ == "__main__":
    get_info()
