"""
face detection functions
"""
import face_recognition
from .file_handler import get_directories,get_train_image,get_images
from shutil import copyfile


def make_encodings(faces):
    """
    Gets an array of face_recognition load image objects
    Converts them into face encodings
    :param faces: array of face_recognition load image objects
    :return: Array of face_encodings
    """
    encodings = []
    for face in faces:
        encodings.append(face_recognition.face_encodings(face)[0])
    return encodings


def sort_faces(path):
    count = 0
    to_find = get_directories(path)
    faces = []
    for id in range(len(to_find)):
        faces.append(face_recognition.load_image_file(
            get_train_image(path + "/" + to_find[id])))
    print("No. of faces to detect: ", len(to_find))
    for i in range(len(to_find)):
        print(path + "/" + to_find[i])

    images = get_images(path)
    print("Number of images loaded: ", len(images))
    known_faces = make_encodings(faces)

    for image in images:
        count = count + 1
        print("Processed: ", count ,image)
        unknown_image = face_recognition.load_image_file(image)
        try:
            unknown_face_encoding = face_recognition.face_encodings(unknown_image)
        except IndexError:
            continue
        for encoding in unknown_face_encoding:
            try:
                results = face_recognition.compare_faces(known_faces, encoding)
                if True in results:
                    c = -1
                    for result in results:
                        c = c + 1
                        if result == True:
                            name = to_find[c]
                            ind = image.rfind('\\')
                            copyfile(image, "test_images/" + name + '/' + image[ind + 1::])
                            print("FILE COPIED")

            except Exception as e:
                print(e)
                continue


# sort_faces("C:\\Users\\ashis\\Documents\\Py\\mera_photo\\test_images")
