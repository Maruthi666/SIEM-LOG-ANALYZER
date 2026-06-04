logs = [
    "User admin failed login",
    "User root failed login",
    "User admin failed login",
    "User admin success login"
]

fail_count = {}

for log in logs:
    if "failed login" in log:
        user = log.split()[1]
        fail_count[user] = fail_count.get(user, 0) + 1

print("Suspicious activity:")
for user, count in fail_count.items():
    if count >= 2:
        print(user, "-> Possible brute force attack")