from flask import Flask, jsonify
import boto3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
s3 = boto3.client('s3', region_name='us-east-1')

@app.route('/videos')
def list_videos():
    response = s3.list_objects_v2(Bucket='yourname-surveillance-footage')
    videos = [obj['Key'] for obj in response.get('Contents', [])]
    return jsonify(videos)

@app.route('/logo')
def get_logo():
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': 'yourname-branding', 'Key': 'logo.png'},
        ExpiresIn=3600
    )
    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(port=5000)