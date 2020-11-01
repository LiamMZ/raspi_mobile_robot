import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raspi_mobile_robot_liammz", # Replace with your own username
    version="0.0.1",
    author="Liam Merz Hoffmeister",
    author_email="liam.merzhoffmeister@gmail.com",
    description="Package for a 4-wheeled mobile robot with raspberry pi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LiamMZ/raspi_mobile_robot.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)