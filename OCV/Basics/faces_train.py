import cv2 as cv
import os 
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

p = []
for i in os.listdir(r'Faces/train'):
    p.append(i)


print(p)

def create_train():
    for person in people:
        path = os.path.join('Faces/train', person) # path to the folder
        features = [] # list of images
        labels = [] # list of labels
        for img in os.listdir(path): # loop through each image
            img_path = os.path.join(path, img) # path to the image
            image = cv.imread(img_path) # read the image
            cv.imshow('Training', image) # display the image
            cv.waitKey(10) # wait for 10ms
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # convert the image to grayscale
            # detect the face in the image
            haar_cascade = cv.CascadeClassifier('haar_face.xml')
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # crop the face
                features.append(faces_roi) # append the face to the list of images
                labels.append(people.index(person)) # append the label to the list of labels

    
    features = np.array(features, dtype='object')
    labels = np.array(labels)

    return features, labels

create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create() # create the face recognizer

# train the face recognizer
features, labels = create_train()
face_recognizer.train(features, np.array(labels))

face_recognizer.save('face_trained.yml') # save the trained model
np.save('features.npy', features) # save the features
np.save('labels.npy', labels) # save the labels
