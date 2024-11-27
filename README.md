

# Amazon Payment Services - Payment Link Integration

This repository demonstrates how to integrate **Amazon Payment Services** (formerly PayFort) for generating payment links via their API.
---

## Features

- Generate secure payment links.
- Customizable parameters for merchant-specific needs.
- Handle API responses effectively.
- Debug and troubleshoot common issues.

---

## How to Use

**1. API Endpoint**
Use the following endpoint for the Payment API:
[https://sbpaymentservices.payfort.com/FortAPI/paymentApi
](https://sbpaymentservices.payfort.com/FortAPI/paymentApi
)

**Key Parameters Explained**

**Parameter	Description**
**access_code**	Unique code provided by Amazon Payment Services.
**merchant_identifier**	Your unique merchant identifier.
**service_command**	Specifies the action (**PAYMENT_LINK** for generating a link).
merchant_reference	Unique reference for the transaction.
amount	Transaction **amount** (multiplied by 100 for major currency units).
currency	Currency of the transaction (e.g., **AED** for United Arab Emirates Dirham).
**customer_email**	Customer's email address to receive the payment link.
**request_expiry_date**	The expiry date for the payment link in ISO 8601 format.
signature	A SHA-256 hashed signature for the request.

Generating a Signature
Follow these steps to create a valid SHA-256 signature:

Concatenate all request parameters in the correct order.
Add your SHA request phrase at the start and SHA response phrase at the end.
Hash the concatenated string using SHA-256.
Refer to the Amazon Payment Services Documentation for detailed guidance on signature generation.

Common Issues & Fixes
Issue	Solution
Invalid signature	Verify the order of parameters and regenerate the signature using the correct secret phrases.

Resources

[Amazon Payment Services Documentation](https://paymentservices.amazon.com/docs/EN/index.html)


[API Reference](https://paymentservices.amazon.com/docs/EN/32.html)

Support
For any issues, contact:

Amazon Payment Services Support: merchantsupport-ps@amazon.com




