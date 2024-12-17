import cv2
import face_recognition as fr
import pymysql
import pickle

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='database_name'
)
cursor=connection.cursor()
imagepaths=[("IMAGE ADDRESS","PERSON NAME"),("IMAGE ADDRESS","PERSON NAME"),("IMAGE ADDRESS","PERSON NAME")]
for i in imagepaths:
    image=cv2.imread(i[0])
    encoding=fr.face_encodings(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))[0]
    encoding_sterialized=pickle.dumps(encoding)
    try:
        cursor.execute("INSERT INTO face_encodings(name,encoding) VALUES(%s,%s)",(i[1],encoding_sterialized))
        connection.commit()
        print("Face encoding stored successfully.")
    except Exception as e:
        print(f"Error inserting face encoding: {e}")
cursor.close()
connection.close()



