#03_user_login_count

logins = ["deep","rash","deep", "rash","abc"]
c = {}

for user in logins:
    c[user] = c.get(user, 0) + 1
print(c)


# {'deep': 2, 'rash': 2, 'abc': 1}

    