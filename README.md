# Portage Unmask
Portage Unmask is a lightweight CLI tool for unmasking specified packages.
It easily appends package atoms directly to ```/etc/portage/package.unmask``` without any need of text editors or manual navigation.


## Features
- **Quick Package Unmasking : Appends package atoms directly to ```/etc/portage/package.unmask```.**
- **Clean System Integration : Includes a simple ```Makefile``` for fast system-wide installation to ```/usr/local/bin```.**

## Installation

Clone repository to your desired location ( For example : /home/user/Downloads/ )
``` git clone https://github.com/yigit-sozmen/PortageUnmask```
and run ```sudo make install```

**To Install :**
```
git clone https://github.com/yigit-sozmen/PortageUnmask
cd PortageUnmask
sudo make install
```

## Usage

```
sudo unmask -p 'package'

or

sudo unmask --package 'package'

# For example :

sudo unmask -p 'www-client/firefox'
```

## How it works

When the program is executed:
- Validates if you're root or not
- Appends the desired package to /etc/portage/package.unmask
- Displays a success/confirmation message upon completion.

## Uninstallation 

To basically remove unmask from /usr/local/bin : 
```sudo make uninstall```


