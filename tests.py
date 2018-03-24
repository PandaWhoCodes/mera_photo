"""
All component testing code
"""
import face_recognition
import cv2
import file_handler


def run_detect_test():
    """
    Live test to check if the face recognition is working properly
    Place the image in the test_images folder (1 image would suffice - Make sure the face can be seen clealy)
    :return: Web cam view with overlay using opencv
    """
    video_capture = cv2.VideoCapture(0)
    test_image = face_recognition.load_image_file(file_handler.get_test_image())
    test_image_encoding = face_recognition.face_encodings(test_image)[0]

    known_face_encodings = [
        test_image_encoding
    ]
    known_face_names = [
        "Test Success"]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    # video_capture.release()
    # cv2.destroyAllWindows()

def single_image_detection():
    """
    Testing single image face detection
    :return:
    """
    ashish_iamge = face_recognition.load_image_file(file_handler.get_test_image())
    # obama_image = face_recognition.load_image_file("single_test2.jpg")
    unknown_image = face_recognition.load_image_file("test_images/single_test2.jpg")

    # Get the face encodings for each face in each image file
    # Since there could be more than one face in each image, it returns a list of encodings.
    # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    try:
        ashish_face_encoding = face_recognition.face_encodings(ashish_iamge)[0]
        # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [
        ashish_face_encoding,
        # obama_face_encoding
    ]

    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    for encoding in unknown_face_encoding:
        results = face_recognition.compare_faces(known_faces, encoding)
        print(results)

    # print("Is the unknown face a picture of Biden? {}".format(results[0]))
    # print("Is the unknown face a picture of Obama? {}".format(results[1]))
    # print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


single_image_detection()
# run_detect_test()