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

**請創立secert.json，放在manage.py同級目錄**
```json
{
    "EMAIL_HOST_USER": "@gmail.com",
    "EMAIL_HOST_PASSWORD": ""
}
```

**清除資料庫:**
```python
python manage.py flush
```

注意:
1. 創建顧客和銷售員時請務必使用網站創建，後台創建無法正確寫入
2. 易出錯功能有使用try catch，留意終端的報錯資訊

## 創建資料同時建立顧客和銷售員帳號

- 八位顧客：user1~8
- 五位銷售員：staff1~5
- 預設密碼："0000"