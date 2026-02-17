def parse_message(text: str):
    if not text:
        return None

    parts = [p.strip() for p in text.split("-")]

    if len(parts) != 3:
        return None

    name, category, raw_amount = parts

    try:
        amount = float(raw_amount.replace(",", "."))
    except ValueError:
        return None

    return {
        "name": name,
        "category": category,
        "amount": amount,
    }
