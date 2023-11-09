def equal_string(name: str, value: str):
    default = False
    if len(name) == len(value):
        for v in name:
            for n in value:
                if v == n:
                    default = True
                    break
                else:
                    default = False
    return default


string2 = "Lovei"
string = "evola"
print(equal_string(string2, string))