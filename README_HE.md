# פרויקט Beton - תיווך שאריות בטון

> פרויקט שרת בפייתון שמתאם בין קבלנים שיש להם שאריות בטון לבין לקוחות שצריכים כמות מועטה של בטון.

## תוכן עניינים

1. [מבנה הפרויקט](#מבנה-הפרויקט)
2. [הסבר על כל קובץ](#הסבר-על-כל-קובץ)
3. [התקנה](#התקנה)
4. [הרצה](#הרצה)
5. [בדיקה שהשרת עובד](#בדיקה-שהשרת-עובד)
6. [רשימת ה-endpoints](#רשימת-ה-endpoints)

---

## מבנה הפרויקט

הפרויקט בנוי בשכבות (Layered Architecture):

```
projectBeton/
│
├── app.py                  ← קובץ ראשי - מרים את שרת FastAPI
├── config.py               ← הגדרות הפרויקט (חיבור ל-DB)
├── database.py             ← ניהול חיבור לבסיס הנתונים
├── requirements.txt        ← רשימת חבילות פייתון נדרשות
├── .env.example            ← דוגמא להגדרות סביבה
├── .gitignore              ← קבצים שלא נדחפים לגיט
│
├── models/                 ← שכבת המודלים (ORM)
│   ├── __init__.py
│   ├── customer.py                       ← מודל לקוח
│   ├── contractor.py                     ← מודל קבלן
│   ├── concrete_request.py               ← מודל בקשת בטון של לקוח
│   ├── contractor_concrete_request.py    ← מודל הצעה של קבלן
│   ├── strength.py                       ← מודל חוזק
│   ├── reliant.py                        ← מודל סומך
│   ├── stone_size.py                     ← מודל גודל אבן
│   ├── purpose.py                        ← מודל מטרה
│   └── concrete_type.py                  ← מודל סוג בטון
│
├── dto/                    ← שכבת DTO (Data Transfer Objects)
│   ├── __init__.py
│   ├── customer_dto.py
│   ├── contractor_dto.py
│   ├── concrete_request_dto.py
│   ├── contractor_concrete_request_dto.py
│   ├── strength_dto.py
│   ├── reliant_dto.py
│   ├── stone_size_dto.py
│   ├── purpose_dto.py
│   └── concrete_type_dto.py
│
├── repository/             ← שכבת גישה ל-DB
│   ├── __init__.py
│   ├── customer_repository.py
│   ├── contractor_repository.py
│   ├── concrete_request_repository.py
│   ├── contractor_concrete_request_repository.py
│   ├── strength_repository.py
│   ├── reliant_repository.py
│   ├── stone_size_repository.py
│   ├── purpose_repository.py
│   └── concrete_type_repository.py
│
├── controller/             ← שכבת ה-API (FastAPI Routers)
│   ├── __init__.py
│   ├── customer_controller.py
│   ├── contractor_controller.py
│   ├── concrete_request_controller.py
│   ├── contractor_concrete_request_controller.py
│   ├── strength_controller.py
│   ├── reliant_controller.py
│   ├── stone_size_controller.py
│   ├── purpose_controller.py
│   └── concrete_type_controller.py
│
└── service/                ← שכבת לוגיקה עסקית (שלד בלבד!)
    ├── __init__.py
    ├── matching_service.py       ← שירות התאמה - שלד
    ├── notification_service.py   ← שירות התראות - שלד
    └── region_service.py         ← שירות אזורים - שלד
```

---

## הסבר על כל קובץ

### קבצי תשתית

#### `app.py`
**תפקיד:** קובץ הכניסה לאפליקציה. מרים את שרת FastAPI, מחבר את כל ה-routers, ומגדיר CORS.
**מכיל:**
- יצירת אובייקט `FastAPI`
- הוספת middleware של CORS (כדי שצד הלקוח / React יוכל להתחבר)
- חיבור כל ה-controllers
- נקודות קצה בסיסיות (`/` ו-`/health`)

#### `config.py`
**תפקיד:** הגדרות פרויקט מרכזיות.
**מכיל:** קריאת משתני סביבה מקובץ `.env` ובניית URL החיבור ל-SQL Server.

#### `database.py`
**תפקיד:** ניהול החיבור לבסיס הנתונים באמצעות SQLAlchemy.
**מכיל:**
- `engine` - מנוע החיבור
- `SessionLocal` - יצרן סשנים
- `Base` - מחלקת בסיס לכל המודלים
- `get_db()` - dependency של FastAPI שמספק סשן חדש לכל בקשה

### שכבת Models (`models/`)
**תפקיד:** מחלקות SQLAlchemy שמייצגות את הטבלאות ב-DB.
**מטרה:** מיפוי בין אובייקטים בפייתון לטבלאות SQL.

קבצים:
- `customer.py` - טבלת Customers (לקוחות)
- `contractor.py` - טבלת Contractors (קבלנים)
- `concrete_request.py` - טבלת ConcreteRequests (בקשות לקוח)
- `contractor_concrete_request.py` - טבלת ContractorConcreteRequests (הצעות קבלן)
- `strength.py`, `reliant.py`, `stone_size.py`, `purpose.py` - טבלאות lookup
- `concrete_type.py` - טבלת Concrete_type (סוג בטון מורכב)

### שכבת DTO (`dto/`)
**תפקיד:** מחלקות Pydantic שמגדירות מבנה של בקשות ותגובות API.
**מטרה:** ולידציה אוטומטית של נתונים שמגיעים מהלקוח, והמרת נתוני DB לפורמט JSON להחזרה.

לכל ישות יש 2 DTOs:
- `XxxCreateDTO` - מבנה הנתונים שמגיע מהלקוח (POST/PUT)
- `XxxResponseDTO` - מבנה הנתונים שמוחזר ללקוח (כולל `id`)

### שכבת Repository (`repository/`)
**תפקיד:** גישה ל-DB. מחביא את פרטי SQLAlchemy מהשאר.
**מטרה:** לרכז את כל השאילתות לכל ישות במקום אחד.

לכל repository יש פונקציות:
- `get_all()` - שליפת כל הרשומות
- `get_by_id(id)` - שליפה לפי מזהה
- `create(data)` - יצירת רשומה חדשה
- `update(id, data)` - עדכון רשומה
- `delete(id)` - מחיקת רשומה

### שכבת Controller (`controller/`)
**תפקיד:** חשיפת ה-API החוצה ב-HTTP.
**מטרה:** קבלת בקשות, וידוא תקינות, קריאה ל-repository, החזרת תשובה.

לכל ישות יש endpoints סטנדרטיים:
- `GET /xxx/` - שליפת הכל
- `GET /xxx/{id}` - שליפה לפי מזהה
- `POST /xxx/` - יצירה
- `PUT /xxx/{id}` - עדכון
- `DELETE /xxx/{id}` - מחיקה

### שכבת Service (`service/`)
**שים לב: שלד בלבד!** הקבצים בתיקייה הזאת מכילים פונקציות לדוגמא שצריך לממש בהמשך.

- `matching_service.py` - לוגיקה של התאמה בין בקשות להצעות (לפי מיקום, כמות, סוג בטון)
- `notification_service.py` - שליחת התראות ללקוחות וקבלנים (SMS / Email)
- `region_service.py` - חישוב אזור גיאוגרפי מקואורדינטות

---

## התקנה

### דרישות מוקדמות
1. **Python 3.10+** - בדוק עם `python --version`
2. **SQL Server** - הותקן ופעיל
3. **ODBC Driver 17 for SQL Server** - דרייבר נחוץ לחיבור ל-SQL Server
   - הורדה: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
4. **בסיס נתונים `beton`** - יצרת אותו ב-SQL Server לפי הסקריפט שלך

### שלבי התקנה

#### שלב 1: יצירת סביבה וירטואלית (מומלץ!)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### שלב 2: התקנת חבילות
```powershell
pip install -r requirements.txt
```

#### שלב 3: הגדרת חיבור ל-DB
1. העתק את `.env.example` ל-`.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
2. פתח את `.env` ועדכן:
   - `DB_SERVER` - שם השרת שלך (לרוב `localhost\SQLEXPRESS`)
   - `DB_NAME` - `beton`
   - אם משתמש ב-Windows Auth - השאר `USE_WINDOWS_AUTH=True`
   - אחרת - מלא `DB_USER` ו-`DB_PASSWORD`

---

## הרצה

### אפשרות 1: הרצה ישירה
```powershell
python app.py
```

### אפשרות 2: עם uvicorn (מומלץ - יש reload אוטומטי בפיתוח)
```powershell
uvicorn app:app --reload
```

השרת יעלה בכתובת: **http://localhost:8000**

---

## בדיקה שהשרת עובד

### בדיקה 1: דף הבית
פתח דפדפן וגלוש ל:
```
http://localhost:8000/
```
אמורה להופיע הודעת "ברוכים הבאים ל-Beton API".

### בדיקה 2: תיעוד אינטראקטיבי של Swagger
**זו הדרך הכי טובה לבדוק את כל ה-API!**

פתח דפדפן וגלוש ל:
```
http://localhost:8000/docs
```

תראה רשימה של כל ה-endpoints, ותוכל ללחוץ על כל אחד מהם, ללחוץ **"Try it out"**, להזין נתונים וללחוץ **"Execute"** - הכל מהדפדפן!

### בדיקה 3: ReDoc - תיעוד יפה יותר
```
http://localhost:8000/redoc
```

### בדיקה 4: בדיקת CRUD מלאה ידנית
דוגמא ליצירת לקוח חדש דרך PowerShell:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/customers/" `
                  -Method POST `
                  -ContentType "application/json" `
                  -Body '{"name":"דני","phone":"050-1234567"}'
```

שליפת כל הלקוחות:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/customers/" -Method GET
```

---

## רשימת ה-endpoints

### לקוחות
- `GET /customers/` - כל הלקוחות
- `GET /customers/{id}` - לקוח לפי מזהה
- `POST /customers/` - יצירת לקוח
- `PUT /customers/{id}` - עדכון לקוח
- `DELETE /customers/{id}` - מחיקת לקוח

### קבלנים
- `GET /contractors/` - כל הקבלנים
- `GET /contractors/{id}` - קבלן לפי מזהה
- `POST /contractors/` - יצירת קבלן
- `PUT /contractors/{id}` - עדכון
- `DELETE /contractors/{id}` - מחיקה

### בקשות בטון של לקוחות
- `GET /concrete-requests/` - כל הבקשות (אפשר `?region=צפון` לסינון)
- `GET /concrete-requests/{id}` - בקשה לפי מזהה
- `GET /concrete-requests/customer/{customer_id}` - בקשות של לקוח מסויים
- `POST /concrete-requests/` - יצירת בקשה
- `PUT /concrete-requests/{id}` - עדכון
- `DELETE /concrete-requests/{id}` - מחיקה

### הצעות של קבלנים
- `GET /contractor-offers/` - כל ההצעות (אפשר `?region=צפון`)
- `GET /contractor-offers/{id}` - הצעה לפי מזהה
- `GET /contractor-offers/contractor/{contractor_id}` - הצעות של קבלן מסויים
- `POST /contractor-offers/` - יצירת הצעה
- `PUT /contractor-offers/{id}` - עדכון
- `DELETE /contractor-offers/{id}` - מחיקה

### טבלאות עזר (lookup)
- `/strengths/` - חוזקים
- `/reliants/` - סומכים
- `/stone-sizes/` - גדלי אבן
- `/purposes/` - מטרות / קטגוריות
- `/concrete-types/` - סוגי בטון

לכל אחד מהם יש את אותם 5 endpoints: GET (כל / לפי id), POST, PUT, DELETE.

---

## הערות חשובות

1. **שכבת ה-service היא שלד בלבד!** הפונקציות בה זורקות `NotImplementedError`. יש להשלים את המימוש בהמשך לפי דרישות הפרויקט.

2. **טבלאות עם שמות עמודות לא רגילים:** בטבלאות Reliant, Stone_size, Purpose, Concrete_type יש עמודות שמתחילות באות גדולה (כמו `Reliant`, `Purpose` וכו'). זה נשמר כפי שהוגדר ב-SQL המקורי.

3. **בעיות חיבור ל-DB?**
   - וודא ש-SQL Server רץ
   - בדוק את `DB_SERVER` ב-`.env`
   - וודא שהותקן ODBC Driver 17
   - אם משתמשים בסיסמא - וודא שהיא נכונה

4. **CORS פתוח לכל המקורות** - מתאים לפיתוח בלבד. בייצור צריך להגביל לדומיין הספציפי של ה-React.
