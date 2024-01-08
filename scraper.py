import requests
import time
from SchoolClosureDAO import SchoolClosureDAO
from bs4 import BeautifulSoup

# Using the DAO

def check_school_closure(url):
    dao = SchoolClosureDAO()
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()   
        status = "open"

        print(response.status_code)
        dao.set_data(url, title.strip(), status)
        return dao

    except requests.exceptions.HTTPError as err:
        print(err)
        print("Initial request failed. Retrying in 10 seconds")
        time.sleep(30)  # Pauses for 10 seconds
        return check_school_closure(url)  # Recursively retry fetching data

    except Exception as e:
        print(f"An error occurred: {e}")
        dao.set_data(url + " BAD!!", "badData", "nothing")
        return dao

# Returns DAO