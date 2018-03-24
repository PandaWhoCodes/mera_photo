"""
All file handling functions.
"""
import glob


def get_test_image():
    """
    Checks the test_images folder and returns only one image
    :return: The top most image found
    """
    images = glob.glob("test_images/*.jpg", recursive=True)
    return images[0]


# print(get_test_image())

def get_images(path):
    """
    Checks the folder for images
    :param path: The folder in which we will check for images
    :return: An array of all images found
    """
    images = glob.glob(path + "/**/**/*.jpg", recursive=True)
    images.extend((glob.glob(path + "/**/**/*.png", recursive=True)))
    return images
