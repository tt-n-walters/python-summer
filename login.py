print("Welcome to the login system. It's amazing.")
for attempt in range(3):
  print()
  print("Enter username:")
  username = input()
  print("Enter password:")
  password = input()
  if password == "tt123":
    print("Access granted to " + username)
    break
  if not password == "tt123":
    print("Access denied to " + username)

  if attempt == 2:
    print("Out of attempts. System blocked.")

print("Program finished. ")
