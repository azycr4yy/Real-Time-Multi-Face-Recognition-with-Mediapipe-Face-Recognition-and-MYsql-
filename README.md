# **Real-Time Multi-Face Recognition System**

This project implements a **real-time multi-face detection and recognition system** using:
- **MediaPipe** for face detection  
- **Face_Recognition** library for face encoding and matching  
- **OpenCV** for video capture and display  
- **MySQL** for storing face encodings and labels  

The program reads a live video feed, detects faces, matches them with pre-stored encodings in a database, and displays recognition results on the video.

---

## **Features**

- Detects **multiple faces** in a live video feed using MediaPipe.  
- Compares detected faces with a database of face encodings using `face_recognition`.  
- Draws bounding boxes around faces with confidence scores.  
- Displays recognized names for matched faces.  

---

## **Setup Instructions**

### **Step 1: Database Setup**
1. Create a MySQL database called `facerecognition`.
2. Add a table named `face_encodings` with the following structure:
   ```sql
   CREATE TABLE face_encodings (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       encoding BLOB
   );
   ```
3. Populate the database with face encodings:
   - Encode faces using `face_recognition` and serialize them using `pickle`.
   - Insert the serialized encodings into the database.

### **Step 2: Run the Code**
- Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-time-face-recognition.git
   cd real-time-face-recognition
   ```
- Run the script:
   ```bash
   python face_recognition_live.py
   ```
- Press **'q'** to exit the video window.

---

## **Code Workflow**

1. **Video Capture:** OpenCV captures frames from a webcam.
2. **Face Detection:** MediaPipe detects faces and provides bounding boxes.
3. **Face Encoding:**
   - Extract regions of interest (ROI) for each face.
   - Generate face encodings using `face_recognition`.
4. **Database Matching:**
   - Compare detected face encodings with database encodings.
   - If a match is found (distance < threshold), display the name.
5. **Visualization:**
   - Draw bounding boxes, confidence scores, and recognized names on the video feed.
