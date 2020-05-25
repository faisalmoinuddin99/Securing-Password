
SECURE = (
    ('s','$'),
    ('and','&'),
    ('a','@'),
    ('o','0'),
    ('i','1'),
    ('I','|')
    )
def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password

password = input("Enter your Password:")
password = securePassword(password)
print(f"Your secure password is {password}")