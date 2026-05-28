"""
שירות התראות (Notification Service) - שלד בלבד!
פונקציות לדוגמא לשליחת הודעות SMS / Email / Push ללקוחות וקבלנים
"""


class NotificationService:
    """
    שירות לשליחת הודעות והתראות
    שלד בלבד - דורש חיבור לשירותי SMS / Email בעתיד
    """

    def send_match_notification_to_customer(self, customer_id: int, offer_id: int) -> bool:
        """
        שליחת התראה ללקוח על התאמה שנמצאה
        TODO: לחבר לשירות SMS (כמו Twilio) או Email
        """
        # פונקציה לדוגמא בלבד
        raise NotImplementedError("יש לחבר לשירות SMS/Email")

    def send_match_notification_to_contractor(self, contractor_id: int, request_id: int) -> bool:
        """
        שליחת התראה לקבלן על לקוח שמעוניין בהצעה שלו
        TODO: לחבר לשירות שליחת הודעות
        """
        raise NotImplementedError("יש לחבר לשירות SMS/Email")

    def send_expiry_warning(self, offer_id: int) -> bool:
        """
        שליחת התראה לקבלן שההצעה שלו עומדת לפוג
        TODO: לממש לוגיקה של בדיקת זמני תפוגה
        """
        raise NotImplementedError("יש לממש בדיקת תפוגה ושליחת התראה")
