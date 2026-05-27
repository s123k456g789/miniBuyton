"""
קובץ הגדרות כללי לפרויקט
מטרה: לרכז את כל הגדרות החיבור לבסיס הנתונים במקום אחד
הקובץ הזה קורא משתני סביבה מקובץ .env (אם קיים) או משתמש בברירות מחדל
"""

import os                                  # ספריה לעבודה עם משתני סביבה
from dotenv import load_dotenv             # פונקציה לטעינת קובץ .env

# טעינת משתנים מקובץ .env לתוך משתני הסביבה של התהליך
load_dotenv()


class Settings:
    """
    מחלקה שמרכזת את כל ההגדרות של הפרויקט
    כל הערכים נטענים ממשתני סביבה או מערכי ברירת מחדל
    """

    # כתובת השרת של SQL Server - לרוב localhost או localhost\SQLEXPRESS
    DB_SERVER: str = os.getenv("DB_SERVER", "localhost\\SQLEXPRESS")

    # שם בסיס הנתונים - לפי מה שיצרנו ב-SQL: "beton"
    DB_NAME: str = os.getenv("DB_NAME", "beton")

    # שם משתמש לבסיס הנתונים (במידה ולא משתמשים ב-Windows Authentication)
    DB_USER: str = os.getenv("DB_USER", "")

    # סיסמא לבסיס הנתונים
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    # האם להשתמש ב-Windows Authentication במקום שם משתמש וסיסמא
    USE_WINDOWS_AUTH: bool = os.getenv("USE_WINDOWS_AUTH", "True").lower() == "true"

    @property
    def database_url(self) -> str:
        """
        בונה את כתובת ה-URL לחיבור לבסיס הנתונים בפורמט של SQLAlchemy
        אם משתמשים ב-Windows Authentication - בונים URL בלי משתמש וסיסמא
        אחרת - בונים URL רגיל עם שם משתמש וסיסמא
        """
        # פרמטרים קבועים לחיבור (הדרייבר של SQL Server)
        driver = "ODBC+Driver+17+for+SQL+Server"

        if self.USE_WINDOWS_AUTH:
            # חיבור עם Windows Authentication
            return (
                f"mssql+pyodbc://@{self.DB_SERVER}/{self.DB_NAME}"
                f"?driver={driver}&trusted_connection=yes"
            )
        else:
            # חיבור עם שם משתמש וסיסמא
            return (
                f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SERVER}/{self.DB_NAME}?driver={driver}"
            )


# יצירת אובייקט הגדרות גלובלי שאפשר לייבא מכל הפרויקט
settings = Settings()
