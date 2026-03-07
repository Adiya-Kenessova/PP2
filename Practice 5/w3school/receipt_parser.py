import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
#18.04.2019 11:13:58
datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

payment_match = re.search(r"(Банковская карта|Наличные):\s*([\d\s]+,\d{2})", text)
payment_method = payment_match.group(1) if payment_match else "Не указан"

total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", text)  #ИТОГО: 18 009,00
total_str = total_match.group(1) if total_match else "0,00"

product_pattern = re.findall(
    r"(\d+)\.\s*\n(.*?)\n(\d+,\d{3})\s*x\s*([\d\s]+,\d{2})\n([\d\s]+,\d{2})",
    text,
    re.DOTALL
)

products = []
all_prices = []
calculated_total = 0.0

for p_id, name, quantity, unit_price, item_total in product_pattern:
    q_val = float(quantity.replace(",", "."))
    u_val = float(unit_price.replace(" ", "").replace(",", "."))
    t_val = float(item_total.replace(" ", "").replace(",", "."))

    products.append({
        "id": p_id,
        "name": " ".join(name.split()),
        "quantity": q_val,
        "unit_price": u_val,
        "total_price": t_val
    })
    
    all_prices.append(t_val)
    calculated_total += t_val

receipt_data = {
    "metadata": {
        "date": date,
        "time": time,
        "payment_method": payment_method
    },
    "products": products,
    "total_info": {
        "raw_total": total_str,
        "calculated_total": round(calculated_total, 2)
    },
    "all_item_prices": all_prices
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))
