
#אני בונה פרויקט בפייתון וריאקט
# הפרויקט אמור לתאם בין קבלנים שנשארו עם שאריות בטון לבין לקוחות שצריכים כמות מועטת של בטון
# בניתי את המסד נתונים בsql server
# אני צריכה שתבנה לי בשפת פייתון את הצד שרת לפי מה שבניתי במסד נתונים
#
#create database beton
#use beton
#
# CREATE TABLE Customers (
#     id INT PRIMARY KEY identity(100,1),
#     name VARCHAR(15) ,
#     phone VARCHAR(20)
# );
#
# CREATE TABLE Contractors (
#     id INT PRIMARY KEY identity(300,1),
#     name VARCHAR(15) ,
#     phone VARCHAR(15),
#
# );
#
# CREATE TABLE ConcreteRequests (
#     request_id INT identity(200,1) PRIMARY KEY,
#     customer_id INT ,
#     purpose_id INT ,
#     quantity DECIMAL(6,2),
#     address VARCHAR(255),
#     lat DECIMAL(9,6) NOT NULL,
#     lng DECIMAL(9,6) NOT NULL,
#
# );
#
# ALTER TABLE ConcreteRequests
# ADD [date] DATE NOT NULL DEFAULT GETDATE();
#
#
# ALTER TABLE ConcreteRequests
# ADD region VARCHAR(100) NULL;
#
#
#
# CREATE TABLE ContractorConcreteRequests (
#     request_id INT IDENTITY(600,1) PRIMARY KEY,
#     concrete_id INT ,
#     contractor_id INT ,
#     quantity DECIMAL(6,2) ,
#     address VARCHAR(255),
# 	lat DECIMAL(9,6) ,
#     lng DECIMAL(9,6) ,
#     expiry_time DATETIME
# );
#
# ALTER TABLE ContractorConcreteRequests
# ADD region VARCHAR(100) NULL;
#
#
# ALTER TABLE ConcreteRequests
# ADD CONSTRAINT FK_ConcreteRequests_Customers
# FOREIGN KEY (customer_id) REFERENCES Customers(id);
#
# ALTER TABLE ContractorConcreteRequests
# ADD CONSTRAINT FK_ContractorConcreteRequests_Contractors
# FOREIGN KEY (contractor_id) REFERENCES Contractors(id);
#
#
#
# --יצירת חוזק
# CREATE TABLE Strength (
#     id INT IDENTITY(1100,1) PRIMARY KEY,
#     strength VARCHAR(50),
# );
#
# --יצירת סומך
# CREATE TABLE Reliant (
#     id INT IDENTITY(1200,1) PRIMARY KEY,
#     Reliant VARCHAR(50),
# );
#
# --יצירת גודל אבן
# CREATE TABLE Stone_size (
#     id INT IDENTITY(1300,1) PRIMARY KEY,
#     Stone_size VARCHAR(50),
# );
#
# --יצירת קטגוריה
# CREATE TABLE Purpose (
#     id INT IDENTITY(1400,1) PRIMARY KEY,
#     Purpose VARCHAR(50),
# );
#
# --קישור מטבלת הזמנת לקוח לקטגוריה
# ALTER TABLE ConcreteRequests
# ADD CONSTRAINT FK_ConcreteRequests_Purpose
# FOREIGN KEY (purpose_id) REFERENCES Purpose(id);
#
#
# CREATE TABLE Concrete_type (
#     id INT IDENTITY(2000,1) PRIMARY KEY,
#     strength_id INT NULL,
#     Reliant_id INT NULL,
#     Stone_size_id INT NULL,
#     Purpose_id INT NULL
# );
#
#  ALTER TABLE Concrete_type
# ADD CONSTRAINT FK_Concrete_type_Strength
# FOREIGN KEY (strength_id) REFERENCES Strength(id);
#
# ALTER TABLE Concrete_type
# ADD CONSTRAINT FK_Concrete_type_Reliant
# FOREIGN KEY (Reliant_id) REFERENCES Reliant(id);
#
# ALTER TABLE Concrete_type
# ADD CONSTRAINT FK_Concrete_type_StoneSize
# FOREIGN KEY (Stone_size_id) REFERENCES Stone_size(id);
#
# ALTER TABLE Concrete_type
# ADD CONSTRAINT FK_Concrete_type_Purpose
# FOREIGN KEY (Purpose_id) REFERENCES Purpose(id);
#
# ALTER TABLE ContractorConcreteRequests
# ADD CONSTRAINT FK_ContractorConcreteRequests_ConcreteType
# FOREIGN KEY (concrete_id)
# REFERENCES Concrete_type(id);
#
#
#
# הפקודות האלו יצרו לי את המסד נתונים
# לפי זה תבנה לי בבקשה פרויקט מחולק לשכבות
#תכין לי תיקיות לכול השכבות הניצרכות
# ותבנה לי את השכבות model,dto,repository,controler
#  בינתיים  בשיכבת הservise אל תבנה אותה אלה לגמרי, אלה תבנה שם פונקציות לדוגמא
#וכשגמרת -תדחוף בחזרה לחשבון הזה בגיט-לחשבון s123k456g789
# תכיו לי גם קובץ שכתוב בעיברית מה עשית בכול דף ואיך אפשר להפעיל אותו ולראות שהוא באמת עובד
# בנוסף בזמן שאתה בונה את הפרויקט תוסיף ליד כל דבר הסברים בהערות בעיברית!!!
#




