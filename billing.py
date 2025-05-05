from datetime import datetime
import calendar

def generate_monthly_bill(item_list, target_month):
    target_start = datetime.strptime(target_month, "%Y-%m")
    last_day = calendar.monthrange(target_start.year, target_start.month)[1]
    target_end = datetime(target_start.year, target_start.month, last_day)

    billing_period_str = f"{target_start.strftime('%Y-%m-%d')} to {target_end.strftime('%Y-%m-%d')}"

    bill = {
        "line_items": [],
        "total_revenue": 0.0
    }

    for item in item_list:
        item_start = datetime.strptime(item["start_date"], "%Y-%m-%d")
        item_end = datetime.max if item["end_date"] is None else datetime.strptime(item["end_date"], "%Y-%m-%d")

        if item_start <= target_end and item_end >= target_start:
            rate = item["rate"]
            qty = item["qty"]
            amount = rate * qty

            bill["line_items"].append({
                "item_code": item["item_code"],
                "rate": rate,
                "qty": qty,
                "amount": amount,
                "billing_period": billing_period_str
            })

            bill["total_revenue"] += amount

    return bill
