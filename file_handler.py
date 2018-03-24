"""
All file handling functions.
"""
import glob
def get_test_image():
    """
    Checks the test_images folder and returns only one image
    :return: The top most image found
    """
    images = glob.glob("test_images/*.jpg",recursive=True)
    return images[0]
# print(get_test_image())