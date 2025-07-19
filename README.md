# be_python_flask
Simple Backend Product

📦 Tools & Teknologi

- Python (v3.10+)
- FastAPI (untuk REST API)
- SQLAlchemy (ORM untuk akses database)
- MySQL (database)
- Pydantic (validasi data)
- Uvicorn (server dev)


## TODO
```bash
pip3 install -r requirement.txt


#run server
make run 

#atau
uvicorn main:app --reload

# install dependencies
make install

```

## [1] Endpoints CRUDS
1. Get all products
`curl --location 'http://localhost:8000/products'`

2. Get product by id
`curl --location 'http://localhost:8000/products/2'`

3. Update product
`curl --location --request PUT 'http://localhost:8000/products/1' \
--header 'Content-Type: application/json' \
--data '{
    "quantity" : 71
}'`

4. Delete product
`curl --location --request DELETE 'http://localhost:8000/products/111'`

5. Add product
`curl --location 'http://localhost:8000/products' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Bedakz",
    "price": 15000,
    "quantity": 15
}'`

## [2] UI Flask
running on 
http://127.0.0.1:5000/

```bash
# run UI
cd web
python app.py
```