# inclusive_test_api
Api to generate PDFs from invoice data.

To get script working.
->Download the code

->Using terminal/command prompt change directory to inclusive_test/Scripts (cd inclusive_test/Scripts & activate to initialize virtual environment) and run activate (To initialize virtual environment)

->Using terminal/command prompt change directory to invoice server

->run the command python manage.py runserver and it should start the server at port http//localhost:8000


Accessing the API

-> go to invoice_server/settings.py and look for the setting CORS_ORIGIN_WHITELIST add the url of the address you'd like to access the api from and add any urls from which you wish to post data to the api to CSRF_TRUSTED_ORIGINS.

->API Routes

---http://localhost:8000/invoices/ GET
To list all invoices

---http://localhost:8000/invoices/11/ DELETE
To delete any invoice (requires id, 11 can be replaced with any valid ID.

---http://localhost:8000/invoice/1/download/ GET
To download any invoice (required id, 1 can be replaced with any valid ID).

---http://localhost:8000/invoice/item/ POST
To add items to an invoice, needs the following formdata varialbes 
  invoice_id, integer,
  item_name, string,
  amount, decimal

---http://localhost:8000/invoice/item/5 GET
To view a specific item. 5 is an item id

---http://localhost:8000/invoice/item/5/ PATCH
To update an item, 5 is an item id.
To update items, the 3 fields below are needed 
Invoice_id, integer,
amount, decimal,
item_name, string,

---http://localhost:8000/invoices/1/
To update an invoice, 1 is an invoice id.
To update items, you need to send a title but an image is note required
title, string
image, file

---http://localhost:8000/invoices/?order_date=desc&order_price=desc&price_gte=15000&date_gte=2020-09-26&date_lte=2020-09-28&price_lte=23000
To filter the invoice data, based off date invoice was created, and order the data accordingly (in descending or ascending order).
To filter the invoice data, based off total price of items in invoice, and order the data accordingly (in descending or ascending order).

Params
order_date desc (specifies date to be sorted in descending order) or asc (specifies date to be sorted in ascending order)
order_price desc (specifies total_price for an invoice to be sorted in descending order) or asc (specifies total price to be sorted in ascending order)

price_gte 15000 (specifies filter to look for invoices with total price greater than 15000)
price_lte 23000 (specifies filter to look for invoices with total price less than 23000)

date_gte 2020-09-28 (specifies filter to look for invoices created after 2020-09-28)
date_lte 2020-09-28 (specifies filter to look for invoices created before 2020-09-28)
