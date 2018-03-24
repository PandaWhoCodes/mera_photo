import argparse
from .face_detect import sort_faces


def argParser():
    """
    The main CLI function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to the folder where all your images are stored.",
                        type=str)
    args = parser.parse_args()
    try:
        # print(args)
        sort_faces(args.path)
    except Exception as e:
        print(e)
