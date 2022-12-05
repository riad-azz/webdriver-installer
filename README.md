# Webdriver Installer

Download and install different web drivers 

## Description

A package that will help you download and save the latest versions of web drivers (geckodriver, chromedriver, edgedriver, operdriver).

## Getting Started

### Installing

* Using PyPI
```python
pip install webdriver-installer
```

* Using Github
```python
pip install git+https://github.com/riad-azz/webdriver-installer.git
```

### Executing program

* How to install the available webdrivers
```python
from webdriver_installer import FireFox

firefox = FireFox()
firefox.install()
```
_the install() function returns the installed driver path as a string_

* How to get the installed driver path
```python
from webdriver_installer import FireFox

firefox = FireFox()
driver_path = firefox.path
```
_The driver will be installed automatically if it wasn't found_

* Some web drivers have both 32-bit and 64-bit 
```python
from webdriver_installer import FireFox

firefox = FireFox(bit=64)
firefox.install()
```
_the default is 32-bit_

* How to uninstall a driver
```python
from webdriver_installer import FireFox

firefox = FireFox()
firefox.uninstall()
```

* How to uninstall all the drivers
```python
import webdriver_installer

webdriver_installer.uninstall()
```

* The default path for saving the web drivers
```python
C:\Users\(your pc name)\AppData\Roaming\webdrivers
```

## Authors

Riadh Azzoun - [@riad-azz](https://github.com/riad-azz)

## Version History

* 0.0.2
    * Initial Release
    * Available web drivers : Firefox - Google Chrome - Opera - Microsoft Edge
* 1.0.0
    * Stable Release
    * Available web drivers : Firefox - Google Chrome - Opera - Microsoft Edge

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details
