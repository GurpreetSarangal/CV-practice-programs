import cv2 as cv
import os

def register_new_user(name, id):
    base_path = r'C:\Users\DAVASR\Documents\AFRAAS_practice\train\persons'
    # name = str(id)+'_'+name
    path_for_user = os.path.join(base_path, str(id)+'_'+name)

    if (os.path.exists(path_for_user) == True):
        print("This is user already registered")
        return "already registered"

    # directory = os.path.join(path_for_user)
    os.mkdir(path_for_user)

    haar_cascade = cv.CascadeClassifier('C:\\Users\\DAVASR\\Documents\\AFRAAS_practice\\testing_files\\haar_face.xml')
    capture = cv.VideoCapture(1)
    os.chdir(path_for_user)
    temp_id = 1
    # digit = len(str(int(capture.get(cv.CAP_PROP_FRAME_COUNT))))
    # print('{}\{}.{}'.format(base_path, name, digit))
    timer = 0
    while True:
        istrue, frame = capture.read()
        cv.imshow("frame", frame)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
        # print(faces_rect)
        # print('{}\{}.{}'.format(base_path, name, digit))



        if len(faces_rect) == 1 and timer == 0:
            record_frame(faces_rect)
            
        
        if cv.waitKey(20) == ord('e') or len(list(os.listdir(path_for_user))) >= 40 :
            break

    capture.release()
    # print(list(os.listdir(os.path.join(base_path, name))))
    # print(len(list(os.listdir(os.path.join(base_path, name)))))
    cv.destroyAllWindows()
    return f"{name} is registerd"

def record_frame(faces_rect, ):
    if len(faces_rect) == 1 :
            x, y, h, w = faces_rect[0]
            cv.imwrite('{}_{}.{}'.format(temp_id, name, 'jpg'), frame[y:y+h, x:x+w])
            temp_id+=1
            cv.imshow('{}.{}'.format(name, "jpg"), frame[y:y+h, x:x+w])

register_new_user("gurpreet", 1)