# SE_Group11

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 導覽頁: ###
必須先從這裡創建資料網頁才能運作!!
```
127.0.0.1:8000/
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
5. 請創立secert.json，放在manage.py同級目錄
