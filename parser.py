def parse_inventory(text):
    result = {}

    lines = text.split("\n")

    for line in lines:
        parts = line.strip().rsplit(" ", 1)

        if len(parts) != 2:
            continue

        name = parts[0].strip()
        try:
            qty = int(parts[1])
        except:
            continue

        result[name.lower()] = qty

    return result
