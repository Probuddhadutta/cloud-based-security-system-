import cv2
import time
import os
from datetime import datetime

class VideoAgent:
    def __init__(self, rtsp_url, output_dir='recordings'):
        self.rtsp_url = rtsp_url
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def start_recording(self):
        cap = cv2.VideoCapture(self.rtsp_url)
        if not cap.isOpened():
            raise Exception("Could not open video stream")
            
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"recording_{timestamp}.mp4")
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
            
            start_time = time.time()
            while (time.time() - start_time) < 60:  # Record for 1 minute
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    break
                    
            out.release()
            
    def cleanup(self):
        # Implement cleanup logic for old recordings
        pass

if __name__ == "__main__":
    rtsp_url = "rtsp://your_camera_ip:554/stream"
    agent = VideoAgent(rtsp_url)
    agent.start_recording()