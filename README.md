# SE_Group11

基於按摩椅銷售業務的 ERP & CRM 系統，使用Django框架開發。

基於OMO模式的銷售管理系統，軟體專案管理課程期末。  

## 系統功能概述，分為三個子應用服務

### 按摩椅銷售網頁
- 銷售前商品頁面
- 基礎後台管理：顧客、產品、訂單

### 業務員工作用 WebApp
- **銷售業務**
    - 優惠與廣告信件推播
    - 發送售後問券
- **單一顧客追蹤**
    - 在銷售網頁的行為追蹤
    - 瀏覽次數追蹤
    - 進入網站入口位置追蹤
- **銷售報表**
    - 本月銷售表現
    - 熱點商品
- **所屬顧客資料管理**
    - 顧客
    - 顧客資料
    - 顧客訂單
    - 顧客預約

### 顧客用按摩椅 WebApp
- 推薦碼系統
- 按摩椅喜好模式儲存
- 預約試用服務


## 實機展示圖集

![](https://picsum.photos/id/684/600/400)


## Deployment

### 前置作業

1. **建立配置文件**

    在`manage.py`同級目錄下建立`secert.json`配置文件：

    ```json
    {
        "EMAIL_HOST_USER": "@gmail.com",
        "EMAIL_HOST_PASSWORD": ""
    }
    ```

2. **初始化資料庫**

    執行以下命令以初始化資料庫、創建遷移檔案，並創建超級用戶：

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

### 啟動與使用

3. **啟動伺服器**

    執行以下命令以啟動伺服器，並進入系統導覽頁：

    ```bash
    python manage.py runserver
    ```

    系統導覽頁入口：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

4. **創建初始資料**

    在系統導覽頁中，點選`建立測試數據`以創建初始資料。此操作將會創建：

    - 八位顧客：user1~8
    - 五位銷售員：staff1~5
    - 預設密碼：`"0000"`

**注意事項：**

- 在創建顧客和銷售員時，請務必透過網站介面進行，以確保數據能夠正確寫入。
- 對於易出錯的功能，已使用`try-catch`進行錯誤捕捉，請留意終端的報錯資訊。

### Contribuitors

> 資管三甲

- 10944134 [陳澔恩](https://github.com/hank1224)
- 10944115 [蔡翊甄](https://github.com/10944115)
- 10944135 [楊芷昀](https://github.com/sheep826)
- 10944133 [曾順莉](https://github.com/zshunli)

