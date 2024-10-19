import time
import schedule
from src import (
    get_last_announcement,
    load_current_announcement,
    save_current_announcement,
    send_email
)


def main():
    """
    Main function that checks for new announcements and sends an email if a new announcement is found.
    """
    MAIL_FLAG = False

    try:
        last_announcement = get_last_announcement()
    except Exception as e:
        raise Exception(F"Error while fetching announcement. Details: {e}")
    
    try:
        current_announcement = load_current_announcement()
    except Exception as e:
        raise Exception(F"Error while loading current announcement. Details: {e}")
    

    for key, value in last_announcement.items():
        if current_announcement[key] != value:
            MAIL_FLAG = True
            break
    
    if MAIL_FLAG:
        mail_body = f"""
            <html>
                <body>
                    <strong>{last_announcement["organization_name"]}</strong>, 
                    {last_announcement["announcement_text"]}. 
                    Bu alım {last_announcement["announcement_date"]} tarihleri arasında yapılacak. 
                    İlanın tamamına <a href="https://kamuilan.sbb.gov.tr">buradan</a> ulaşabilirsiniz.
                </body>
            </html>
            """
        try:
            send_email(mail_body)
        except Exception as e:
            raise Exception(F"Error while sending email. Details: {e}")
        save_current_announcement(last_announcement)
    else:
        print("No new announcement found.")


if __name__ == "__main__":
    """
    Main function that schedules the main function to run every hour.
    """
    schedule.every(1).hours.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
