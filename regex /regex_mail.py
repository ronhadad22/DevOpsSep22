import re


def check_email(email):
    # Define the regular expression pattern for a valid email address
    # pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.0-9]+$"
    pattern = r"[\w._%+-]{1,3}@[\w-]+\.[a-zA-Z]{2,4}\.[a-zA-Z]{3,4}"

    # Use the re.fullmatch function to check if the input string matches the pattern
    match = re.fullmatch(pattern, email)

    # If the match is not None, then the input string is a valid email address
    if match:
        print("Email is a match!")
    else:
        print("Email is not a match.")


# Test the function with some example input strings
check_email("test@example.com77")  #X
check_email("tet@sub.example.com.ddd")  #X
check_email("te+st@123.com")
check_email("tes@texample.co.ukr")
check_email("test@example.123")
check_email("test@example.com123")
check_email("test@-example.com")
check_email("test@example-.com")
check_email("test@example.com-")
