import district_List
import scraper
import db
import json

def __init__():
    print("Starting Scraper")

    distList = district_List.school_urls
    scrpr = scraper
    districts = []


    for url in distList:
        distObj = scrpr.check_school_closure(url)

        print("Now Scraping " + url + "!")
        # Example Usage
        if distObj:
            print(distObj.__dict__)
            print("\n")
            districts.append((distObj.url, distObj.title, distObj.status))
            # Serialize the district object for database storage
            # Assuming distObj can be converted to a dictionary

            # Store in the database
    try:
        query = "INSERT INTO SchoolClosures (URL,DistrictName,Status) VALUES (%s,%s,%s);"
        db.cursor.executemany(query, (districts))
        db.conn.commit()
        print("Success!")
    except Exception as e:
        db.conn.rollback()
        print(f"Error storing data: {e}")
        
    # Close the database connection
    db.close_connection()

__init__()



        
