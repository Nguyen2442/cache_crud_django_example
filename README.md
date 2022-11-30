# Django Postgres/MariaDB/Mysql Faust Kafka

-   Run `docker-compose -f local.yml build` and `docker-compose -f local.yml up -d` to start the  containers.


### API 
An API to create a product in store 

-   Endpoint: http://127.0.0.1:8000/products/
-   Method: POST
-   Content-Type: application/json

    {
        "name": "Laptop MSI modern 15",
        "description": "Laptop for gaming",
        "price": "10000"
    }

```
curl --location --request POST 'http://127.0.0.1:8000/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "Laptop MSI modern 15",
	"description": "Laptop for gaming",
	"price": "10000"
}}'
```
