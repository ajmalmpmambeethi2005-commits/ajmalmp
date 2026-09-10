def is_valid_ipv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


print(is_valid_ipv4("1.2.3.4"))
print(is_valid_ipv4("123.45.67.89"))
print(is_valid_ipv4("1.2.3"))
print(is_valid_ipv4("1.2.3.4.5"))
print(is_valid_ipv4("123.456.78.90"))