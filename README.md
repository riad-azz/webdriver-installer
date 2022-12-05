# Webdriver Installer

Download and install different web drivers 

## Description

A package that will help you download and save the latest versions of web drivers.

## Getting Started

### Installing

```python
pip install webdriver-installer
```

### Executing program

* How to install the available webdrivers
```python
from webdriver_installer import FireFox

firefox = FireFox()
firefox.install()
```

## Help

* How to get the installer driver path
```python
from webdriver_installer import FireFox

firefox = FireFox()
driver_path = firefox.path
```

* Some web drivers have both 32-bit and 64-bit and you can pick by using _(default is 32-bit)_
```python
from webdriver_installer import FireFox

firefox = FireFox(bit=64)
firefox.install()
```

* How to uninstall a driver
```python
from webdriver_installer import FireFox

firefox = FireFox()
firefox.uninstall()
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
