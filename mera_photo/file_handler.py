"""
All file handling functions.
"""
import glob
import os
from pathlib import Path


def get_test_image():
    """
    Checks the test_images folder and returns only one image
    :return: The top most image found
    """
    images = glob.glob("test_images/*.jpg", recursive=True)
    return images[0]


def get_train_image(path):
    """
    returns the one training image in each folder
    :return: image path
    """
    images = glob.glob(path + "/*.jpg")
    return images[0]


def get_images(path):
    """
    Checks the folder for images
    :param path: The folder in which we will check for images
    :return: An array of all images found
    """
    path = path + "/images/IV/Camera"
    images = glob.glob(path + "**/**/**/*.jpg", recursive=True)
    images.extend((glob.glob(path + "**/**/**/*.png", recursive=True)))
    return images


def get_directories(path):
    """
    Get directorty names of only the known faces
    :param path: The path for all images provided by user
    :return: list of folders - the images folder
    """
    folders = []
    cwd = os.getcwd()
    os.chdir(path)
    images_folder = "images"
    files = os.listdir(".")
    for item in files:
        if os.path.isdir(item) == True and item != images_folder:
            folders.append(item)
    os.chdir(cwd)

    return folders