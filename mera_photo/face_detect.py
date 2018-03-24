"""
face detection functions
"""
import face_recognition
from .file_handler import get_directories, get_train_image, get_images
from shutil import copyfile
from joblib import Parallel, delayed
import multiprocessing

num_cores = multiprocessing.cpu_count()


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


def check_faces(image, to_find, known_faces, path):
    """
    Check the unknown image against known faces
    :param image: image to be checked
    :param to_find: stores the names of the known people
    :param known_faces: face_encodings of the known images
    :param path: The path that is checked : Provided by the user
    :return: None
    """
    unknown_image = face_recognition.load_image_file(image)
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)
    except IndexError:
        return 0
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
                        copyfile(image, path + "\\" + name + '/' + image[ind + 1::])
                        print("FILE COPIED")

        except Exception as e:
            print(e)
            continue


def load_faces(to_find, path):
    """

    :param to_find: stores the names of the known people
    :param path: The path that is checked : Provided by the user
    :return: loaded faces into face_recognition module
    """
    faces = []
    for id in range(len(to_find)):
        faces.append(face_recognition.load_image_file(
            get_train_image(path + "/" + to_find[id])))
    return faces


def sort_faces(path):
    """
    Sorts the faces with respect facial features
    :param path: The path that is checked : Provided by the user
    :return: None
    """
    count = 0
    to_find = get_directories(path)
    faces = load_faces(to_find, path)
    print("No. of faces to detect: ", len(to_find))
    for i in range(len(to_find)):
        print(path + "/" + to_find[i])

    images = get_images(path)
    print("Number of images loaded: ", len(images))
    known_faces = make_encodings(faces)

    results = Parallel(n_jobs=num_cores)(delayed(check_faces)(image, to_find, known_faces, path) for image in images)
