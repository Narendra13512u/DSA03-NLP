import re

def main():
   
    text = "Hello, my email is example123@example.com and my phone number is 123-456-7890."

   
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

    
    emails = re.findall(email_pattern, text)
    print("Email addresses found:", emails)

   
    phone_numbers = re.findall(phone_pattern, text)
    print("Phone numbers found:", phone_numbers)

   
    search_pattern = r'\bexample\b'
    matches = re.findall(search_pattern, text)
    print("Occurrences of 'example':", len(matches))

if __name__ == "__main__":
    main()
