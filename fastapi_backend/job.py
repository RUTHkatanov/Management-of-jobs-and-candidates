from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/yourdbname"
mongo = PyMongo(app)
jobs_collection = mongo.db.jobs

@app.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.json
    job = {
        'title': data['title'],
        'description': data['description'],
        'requirements': data['requirements'],
        'location': data.get('location'),
        'company': data['company']
    }
    job_id = jobs_collection.insert_one(job).inserted_id
    return jsonify({'message': 'Job created successfully', 'job_id': str(job_id)}), 201

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = jobs_collection.find()
    jobs_list = []
    for job in jobs:
        job_data = {
            'id': str(job['_id']),
            'title': job['title'],
            'description': job['description'],
            'requirements': job['requirements'],
            'location': job['location'],
            'company': job['company']
        }
        jobs_list.append(job_data)
    return jsonify(jobs_list), 200

@app.route('/api/jobs/<job_id>', methods=['GET'])
def get_job(job_id):
    job = jobs_collection.find_one({'_id': ObjectId(job_id)})
    if job:
        job_data = {
            'id': str(job['_id']),
            'title': job['title'],
            'description': job['description'],
            'requirements': job['requirements'],
            'location': job['location'],
            'company': job['company']
        }
        return jsonify(job_data), 200
    else:
        return jsonify({'message': 'Job not found'}), 404

@app.route('/api/jobs/<job_id>', methods=['PUT'])
def update_job(job_id):
    data = request.json
    updated_job = {
        'title': data['title'],
        'description': data['description'],
        'requirements': data['requirements'],
        'location': data.get('location'),
        'company': data['company']
    }
    result = jobs_collection.update_one({'_id': ObjectId(job_id)}, {'$set': updated_job})
    if result.matched_count > 0:
        return jsonify({'message': 'Job updated successfully'}), 200
    else:
        return jsonify({'message': 'Job not found'}), 404

@app.route('/api/jobs/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    result = jobs_collection.delete_one({'_id': ObjectId(job_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Job deleted successfully'}), 200
    else:
        return jsonify({'message': 'Job not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)