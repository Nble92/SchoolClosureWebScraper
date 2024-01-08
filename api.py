from flask import Flask, request,jsonify
import db


app = Flask(__name__)



@app.route('/')
def home():
    return 'Hello'

@app.route('/store', methods=['POST'])
def store():
        
        data = request.json.get('data')
        if data and 'URL' in data:
            url = data['URL']
            district_name = data['DistrictName']
            district_status = data['Status']


            db.get_db_connection()
            try:
                query = "INSERT INTO SchoolClosures (URL,DistrictName,Status) VALUES (%s,%s,%s);"
                db.cursor.execute(query, (url, district_name, district_status,))

# Commit the transaction
                db.conn.commit()

                return jsonify({'message':  district_name +' added successfully'}), 201

            except Exception as e:
        # Rollback in case of any error
                db.conn.rollback()
                return jsonify({'error': str(e)}), 500

            finally:
             db.close_connection()

        else:
            return jsonify({'error': 'Invalid data provided'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)