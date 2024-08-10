# Face Recognition Attendance System

This project specification outlines the design and development of a face recognition attendance system using Python 3.12 with libraries OpenCV, Face_Recognition and Tkinter. 

The system aims to automate attendance tracking through real-time face detection, recognition of pre-enrolled faces, and logging attendance records. Key functionalities include robust face detection algorithms and machine learning models for accurate recognition, integrated with a user-friendly interface for system management and reporting. 

The project encompasses detailed requirements, technical specifications, and an implementation plan structured around milestones and timelines. Testing and validation procedures ensure compliance with performance metrics and user acceptance criteria. Security measures address data encryption and privacy concerns following regulatory standards.


## Features

1. **Maintains Student Records:** Stores student details and images.
2. **Take Attendance using Face Recognition:** Uses face recognition for taking attendance.
3. **User Friendly UI:** Ease to use and straight forward UI.


## Prerequisites

To run this project, you will need to install the following:

**Python  3.12 with libraries**

&nbsp;&nbsp; Download [Python 3.12](https://www.python.org/downloads/release/python-3125/) from here.

| libraries Used        | Version       | Description                                        |
| :--------             | :----------   | :------------------------------------------------- |
| **Tkinter**           | **N/A**       | Create graphical user interfaces.                  |
| **Pillow**            | **10.2**      | Manipulate and edit images.                        |
| **NumPy**             | **1.26.4**    | Efficient numerical computation and data analysis. |
| **OpenCV**            | **4.10.0.84** | Captures images using OpenCV.                      |
| **Face Recognition**  | **1.2.3**     | Detects and recognizes faces.                      |
| **MySQL Connector**   | **9.0.0**     | Stores data in a MySQL database.                   |
| **Pickle**            | **N/A**       | Serializes data using Pickle for efficient storage.|
| **CSV**               | **N/A**       | Exports data to CSV files for further analysis.    |

**Note :-** Face Recognition library depends on NumPy 1.26.4, which is not forward compatible with newer NumPy versions. 

**MySQL 8.0 Community Edition**

&nbsp;&nbsp; Download [MySQL 8.0](https://dev.mysql.com/downloads/installer/) from here.

## Installation

Install all libraries in you virtual environment for avoiding any conflicts with already install libraries or installing any libraries in future.
How to setup [virtual environment in python 3.12](https://youtu.be/hC5rfoIY8nU).

After creating and activating virtual environment, run command below:

Command to install to Pillow

```bash
  pip install pillow==10.2
```

Command to install to NumPy

```bash
  pip install numpy==1.26.4
```

Command to install to OpenCV

```bash
  pip install opencv-python==4.10.0.84
```

**Note :-** When installing the Face Recognition library, some users may encounter issues building the wheel for the [Dlib](http://dlib.net/) dependency. so I added compiled binary (.whl) for Python 3.12 on a Windows x64 OS.

Command to install to dlib wheel

```bash
  python -m pip install dlib-19.24.99-cp312-cp312-win_amd64.whl
```

Command to install to face_recognition

```bash
  pip install face_recognition==1.2.3
```

Command to install to MySQL Connector

```bash
  pip install mysql.connector-python==9.0.0
```

**Note :-** Tkinter, CSV, and Pickle are built-in Python libraries, no pip installation required.


## Contributing

Pull requests are welcome. 

For major changes, please open an issue first to discuss what you'd like to change.