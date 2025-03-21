const express = require('express');
const AWS = require('aws-sdk');
const app = express();
const s3 = new AWS.S3({ region: 'us-east-1' });

app.use(express.static('public'));

app.get('/videos', async (req, res) => {
  const params = { Bucket: 'yourname-surveillance-footage' };
  const data = await s3.listObjectsV2(params).promise();
  res.json(data.Contents.map(obj => obj.Key));
});

app.get('/logo', (req, res) => {
  const url = s3.getSignedUrl('getObject', {
    Bucket: 'yourname-branding',
    Key: 'logo.png',
    Expires: 3600
  });
  res.json({ url });
});

app.listen(3000, () => console.log('Server on port 3000'));