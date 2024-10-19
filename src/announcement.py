import os
from bs4 import BeautifulSoup
import joblib
import requests


def get_last_announcement() -> dict:
    """
    Fetches the latest announcement from the website.

    Returns
    -------
    dict: A dictionary containing the organization name, announcement text and announcement date.
    """
    url = 'https://kamuilan.sbb.gov.tr'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        organization_name = soup.\
                find("ul", class_ = "cbp_tmtimeline").\
                find("div", class_ = "cbp_tmlabel animated fadeInUp").\
                find("p", class_ = "alt_p1").text
        desc = soup.\
                find("ul", class_ = "cbp_tmtimeline").\
                find("div", class_ = "cbp_tmlabel animated fadeInUp").\
                find("p", class_ = "alt_p2").text.strip()
        announcement_text = desc.split("(")[0].strip().lower().capitalize()
        announcement_date = desc.split("(")[1].strip()[0:-1]
        return {
            "organization_name": organization_name,
            "announcement_text": announcement_text,
            "announcement_date": announcement_date
        }
    except Exception as e:
        raise Exception(F"Error while parsing announcement. Details: {e}")


def save_current_announcement(
    announcement: dict
) -> None:
    """
    Saves the announcement to a pickle file.

    Parameters
    ----------
    announcement : dict
        A dictionary containing the organization name, announcement text and announcement date.
    """
    os.makedirs("announcement", exist_ok=True)
    joblib.dump(announcement, os.path.join("announcement", "current_announcement.pkl"))


def load_current_announcement() -> dict:
    """
    Loads the announcement from the pickle file.

    Returns
    -------
    dict: A dictionary containing the organization name, announcement text and announcement date.
    """
    try:
        return joblib.load(os.path.join("announcement", "current_announcement.pkl"))
    except Exception as e:
        raise Exception(F"Error while loading announcement. Details: {e}")
