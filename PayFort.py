import hashlib
import requests
import json
import os

# Function to calculate the signature based on sorted parameters and request phrase
def calculate_signature(unsorted_dict, sha_phrase, sha_method=hashlib.sha256):
    # Sorting the keys of the data (case-insensitive)
    sorted_keys = sorted(unsorted_dict, key=lambda x: x.lower())

    # Sorting the data and concatenating "=" between the key and the value
    sorted_dict = {k: unsorted_dict[k] for k in sorted_keys}
    result = "".join(f"{k}={v}" for k, v in sorted_dict.items())

    # Adding the SHA Request Phrase at the beginning and end of the result string
    result_string = f"{sha_phrase}{result}{sha_phrase}"

    # Encrypting the result of the out string with the given algorithm from sha_method
    signature = sha_method(result_string.encode()).hexdigest()
    return signature

# Step 1: Prepare Parameters
request_phrase = os.getenv("REQUEST_PHRASE", "request_phrase")  # Use environment variables for security
parameters = {
    "access_code": os.getenv("ACCESS_CODE", "your_access_code"),
    "merchant_identifier": os.getenv("MERCHANT_IDENTIFIER", "your_merchant_indentifier"),
    "language": "en",
    "service_command": "PAYMENT_LINK",
    "merchant_reference": "merchantTest-10080",
    "amount": "125000",
    "currency": "AED",
    "customer_email": "customer_email",
    "request_expiry_date": "2024-12-22T15:36:55+03:00",
    "notification_type": "EMAIL/SMS",
    "order_description": "Iphone 16",
    "customer_name" : "Nishant Chauhan"
}

# Step 2: Generate Signature
signature = calculate_signature(parameters, request_phrase)
parameters["signature"] = signature  # Add signature to the request

# Debugging: Check signature and parameter values
print("Generated Signature:", signature)
print("Request Parameters:", json.dumps(parameters, indent=4))

# Step 3: Make API Request with Error Handling
try:
    response = requests.post(
        "https://sbpaymentservices.payfort.com/FortAPI/paymentApi",
        headers={"Content-Type": "application/json"},
        data=json.dumps(parameters)
    )
    response.raise_for_status()  # Raise an HTTPError for bad responses
    response_data = response.json()
    print("Response:", response_data)

    # Additional debugging if signature mismatch occurs
    if response_data.get("response_message") == "Signature mismatch":
        print("Signature Mismatch Debugging:")
        print("Generated Signature:", signature)
        print("Request Parameters (sorted):", parameters)

except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

# Step 4: Optional Debugging
if os.getenv("DEBUG", "False") == "True":
    print("Generated Signature:", signature)
    print("Request Parameters:", json.dumps(parameters, indent=4))
