# be_python_flask
Simple Backend Product

## Developer
muhamadalfarisy98@gmail.com

## Architecture
<img width="644" height="382" alt="image" src="https://github.com/user-attachments/assets/dc448161-a425-4881-81da-45ac6daa95fc" />

## Tools & Teknologi

- Python (v3.10+)
- FastAPI (untuk REST API)
- SQLAlchemy (ORM untuk akses database)
- MySQL (database)
- Pydantic (validasi data)
- Uvicorn (server dev)
- HTML


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
## Result
<img width="1109" height="432" alt="image" src="https://github.com/user-attachments/assets/f919e751-7d06-4d52-a058-9b87e325a773" />

<img width="920" height="415" alt="image" src="https://github.com/user-attachments/assets/9da3fb51-8d4c-4492-81b7-6c74dc596e34" />

<img width="1009" height="462" alt="image" src="https://github.com/user-attachments/assets/a79664d0-b6ae-4d79-9232-8a1bfc5e3ff0" />

