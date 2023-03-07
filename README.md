# Installation
Install [python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe) 

Install [Arduino](https://downloads.arduino.cc/arduino-ide/arduino-ide_2.0.4_Windows_64bit.exe?_gl=1*1pdytnc*_ga*MTkzMTg5NDYxMy4xNjc4MTk5NTMy*_ga_NEXN8H46L5*MTY3ODE5OTUzMi4xLjEuMTY3ODE5OTYxNS4wLjAuMA..)

Use the package manager pip to install
```bash
pip install pip install opencv-python
pip install mediapipe
```
## Connection
![My Remote Image](https://content.instructables.com/F9G/N43W/JRGOOJJQ/F9GN43WJRGOOJJQ.jpg)
## usage 
- Download the project LedControlMl zip file
- Unzip the file
- Run the files on a python terminal or compiler
- Connect your leds to your Arduino MCU  properly using the correct pinmodes
- Open your arduino.exe software
- Go to files, then examples, then locate the library called StandardFirmata
- You can also download the library, just go to sketch >> include library >> add zip library >> called StandardFirmata
- Select the right com port and run the arduino StandardFirmata exactly the way it is
- Run the main LedControlMl python file.
