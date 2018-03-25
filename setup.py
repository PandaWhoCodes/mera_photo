"""
https://github.com/PandaWhoCodes/mera_photo/blob/master/README.md
"""
from setuptools import setup

dependencies = ['face_recognition', 'argparse','joblib']
setup(
    name='mera_photo',
    version='0.1.6',
    url='https://github.com/PandaWhoCodes/mera_photo',
    license='MIT',
    author='Thomas Ashish Cherian',
    author_email='ufoundashish@gmail.com',
    description='Short for mera photo\'s bhej dena(Do remember to send me my pics). A photo sorter that sorts photos with respect to faces.',
    long_description=__doc__,
    packages=['mera_photo'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    scripts=['mera_photo/main.py'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'mera_photo = mera_photo.main:argParser',
        ],
    },

    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
