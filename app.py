from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://power:powerranger@cluster0.jxwvnqo.mongodb.net/")
db = client.magic_search  # Replace 'magic_search' with your actual database name
collection = db.abex  # Replace 'abex' with your actual collection name

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/get-details-by-linkedin-url', methods=['POST'])
def get_details_by_linkedin_url():
    data = request.json
    linkedin_url = data.get('linkedin_url')
    
    # Query to find the record by LinkedIn URL
    query = {"Person Linkedin Url": linkedin_url}
    result = collection.find_one(query)
    
    if result:
        # Extract required fields
        name = result.get('Name', 'N/A')
        email = result.get('Email', 'N/A')
        phone = result.get('Mobile', 'N/A')  # Assuming 'Mobile' is the field name for phone
        
        return jsonify({
            "name": name,
            "email": email,
            "phone": phone
        })
    else:
        return jsonify({"error": "LinkedIn URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)