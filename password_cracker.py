# We need these three error types so we can "catch" them when a password fails.
import zipfile
import zlib

# Step 1: Read every password from the file into a list.
with open("Ashley-Madison.txt", encoding="utf-8", errors="ignore") as f:
    passwords = f.readlines()

# Step 2: Try each password on the zip, one at a time.
for count, password in enumerate(passwords):
    password = password.strip()  # remove the trailing newline from each line

    # Progress check: print where we are every 10,000 tries.
    if count % 10000 == 0:
        print(f"Tried {count} passwords... currently at: {password}")

    try:
        # The risky part: try to open the zip with this password.
        with zipfile.ZipFile("whitehouse_secrets.zip") as zf:
            zf.extractall(pwd=password.encode())  # zip passwords must be bytes, so .encode()
        # If we get here with NO error, the password worked!
        print(f"SUCCESS! The password is: {password}")
        break  # stop the loop so we don't overwrite the file with later guesses

    except (RuntimeError, zipfile.BadZipFile, zlib.error):
        # Wrong password → one of these errors fires → we catch it and move on.
        continue


