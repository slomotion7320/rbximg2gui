# rbximg2gui
This is a recreation of my project from ~10 years ago and likely won't be updated further.
Use this tool to convert digital image files into Roblox GUIs.

# How It Works
    Heavily utilizes Alex Clark's PIL Tools fork to take the input image, resize to make reading individual pixel colors easy, and convert to a roblox script using string manipulation. 
    This can be re-worked by modifying the code for many different projects:
    -Add OpenCV functionality, send data to a web server in JSON, then decode in Roblox (Live WebCam in Roblox. I proved this is possible.). Keep in mind the HTTPService limitations.
    -Extended GUI Object functionality
    -Add support for Animated GIFs and Video frames (This might look good in an initial loading screen for a game project).
    
#### Installation
    $ git clone https://github.com/slomotion7320/rbximg2gui.git
    cd ./rbximg2gui
    pip install -r requirements.txt

#### Usage
    rbximg2gui.py [-h] [-i filename] [--about]

    Convert an image file to a Roblox GUI.

    options:
    -h, --help   show this help message and exit
    -i filename  Input an image file to convert.
    --about      About
