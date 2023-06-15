# SE_Group11

```python
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
```

**導覽:**
```
127.0.0.1:8000/
```

**建立測試數據url:**
此創建資料待更正，但仍可使用
```
127.0.0.1:8000/DB/create_test_data/
```

**清除資料庫:**
```python
python manage.py flush
```

注意:
    1. 創建顧客時請務必使用網站創建，後台創建無法正確寫入
    2. 銷售員帳號請從後台創立
    3. 假設一筆訂單僅能購買一個商品
    4. 易出錯功能使用try catch，留意終端的報錯資訊