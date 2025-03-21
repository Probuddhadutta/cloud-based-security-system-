import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [videos, setVideos] = useState([]);
  const [logoUrl, setLogoUrl] = useState('');
  const [selectedVideo, setSelectedVideo] = useState('');

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/videos`)
      .then(response => setVideos(response.data))
      .catch(error => console.error('Error fetching videos:', error));

    axios.get(`${process.env.REACT_APP_API_URL}/logo`)
      .then(response => setLogoUrl(response.data.url))
      .catch(error => console.error('Error fetching logo:', error));
  }, []);

  const playVideo = (videoKey) => {
    const videoUrl = `https://${process.env.REACT_APP_S3_BUCKET}.s3.amazonaws.com/${videoKey}`;
    setSelectedVideo(videoUrl);
  };

  return (
    <div className="App">
      <h1>Cloud Security System</h1>
      {logoUrl && <img src={logoUrl} alt="Company Logo" style={{ width: '100px' }} />}
      
      <h2>Video Footage</h2>
      <ul>
        {videos.map((video, index) => (
          <li key={index} onClick={() => playVideo(video)} style={{ cursor: 'pointer' }}>
            {video}
          </li>
        ))}
      </ul>

      {selectedVideo && (
        <video controls width="640" src={selectedVideo}>
          Your browser does not support the video tag.
        </video>
      )}
    </div>
  );
}

export default App;