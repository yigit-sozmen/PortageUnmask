# Portage Unmask
Portage Unmask is a lightweight CLI tool for unmasking specified packages.
It easily appends package atoms directly to ```/etc/portage/package.unmask``` or your desired direction without any need of text editors or manual navigation.


## Features
- **Quick Package Unmasking : Appends package atoms directly to ```/etc/portage/package.unmask or custom direction```.**
- **Clean System Integration : Includes a simple ```Makefile``` for fast system-wide installation to ```/usr/local/bin```.**

## Installation

Clone repository to your desired location and run makefile as root.

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
## Custom Directories

Instead of unmasking using : ```/etc/portage/package.unmask```

You can specify your own directory. For example: 

```sudo unmask -p x11-misc/sddm -d /etc/portage/sddm.unmask```

## Multiple Package Unmasking

To simply unmask multiple packages at once just simply type:
```\n``` at the end of the previous package.

**For example:**

```sudo unmask -p www-client/firefox\nx11-misc/sddm```

## How it works

When the program is executed:
- Validates if you're root or not
- Appends the desired package to /etc/portage/package.unmask
- Displays a success/confirmation message upon completion.

## Uninstallation 

To basically remove Portage Unmask from /usr/local/bin : 
```sudo make uninstall```


