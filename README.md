# X-Touch-Mini-FS2020
_Control FS2020 with a Behringer X-Touch Mini_  
![Build exe](https://github.com/maartentamboer/X-Touch-Mini-FS2020/workflows/Build%20exe/badge.svg)
![Release](https://github.com/maartentamboer/X-Touch-Mini-FS2020/workflows/Release/badge.svg)
[![Download](https://img.shields.io/badge/Download-.zip-blue)](https://github.com/maartentamboer/X-Touch-Mini-FS2020/releases/latest/download/X-Touch-Mini-FS2020.zip)


<img src="https://user-images.githubusercontent.com/82336/96199071-7e8d7e80-0f4e-11eb-97e7-30d4527aa112.png" alt="X-TOUCH-MINI_P0B3M_Top_XL" width="500">

# Installation
Download the zip, extract, run the exe. In case you want to modify the code follow the instructions below.

| Release archive | Development |  
| -------------------------------------------------- | -------- |  
| [![Download](https://img.shields.io/badge/Download-.zip-blue)](https://github.com/maartentamboer/X-Touch-Mini-FS2020/releases/latest/download/X-Touch-Mini-FS2020.zip) | See below |  

You also need [MobiFlight](https://www.mobiflight.com/en/index.html) for some functions to work.

# Configuration
Modify the files in the Configuration folder to change assignments.

# X-Touch configuration
To use the encoders, the behavior must be set to Relative2 mode.
To help with that I've added my config files that can be programmed to the X-Touch by using the
X-Touch editor software from Behringer.  
Download it from their [Product page](https://www.behringer.com/product.html?modelCode=P0B3M).

<img src="https://user-images.githubusercontent.com/82336/96199074-7fbeab80-0f4e-11eb-9bb6-bf8b912a0fb2.png" alt="xtouch_editor" width="500">

# Development
Note from @ticktricktrack
I'm not a python coder and I usually work on a Mac, I'll put as many comments in here to be able to follow this with minimal coding knowledge.

- `git`
- `python` [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- Make sure you add python to your command line path variable

<img src="https://user-images.githubusercontent.com/82336/96336775-1045da80-107a-11eb-8b4e-bd80fd6b170d.png" alt="python_path" width="500">

- Visual C++, installed via [build tools installer](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)

```powershell
# I prefer to use git bash as a terminal over the windows cmd
git clone https://github.com/maartentamboer/X-Touch-Mini-FS2020.git
cd X-Touch-Mini-FS2020
pip install -r requirements.txt
# start msfs
python main.py
```
