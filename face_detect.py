"""
face detection functions
"""
import face_recognition
import cv2
import file_handler

def sort_faces(path):
    images = file_handler.get_images(path)
