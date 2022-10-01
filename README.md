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
from webdriver_installer import ChromeDriver

chrome_installer = ChromeDriver()
chrome_installer.install()
```

## Help

* How to get the installer driver path
```python
from webdriver_installer import ChromeDriver

chrome_installer = ChromeDriver()
driver_path = chrome_installer.driver_path
```

* Some web drivers have both 32-bit and 64-bit and you can pick by using _(default is 32-bit)_
```python
from webdriver_installer import ChromeDriver

chrome_installer = ChromeDriver(bit=64)
driver_path = chrome_installer.install()
```

* If you would like for the driver to update in case of a new version _(update is False by dafault but will notify you incase of a new version)_
```python
from webdriver_installer import ChromeDriver

chrome_installer = ChromeDriver()
chrome_installer.install(update=True)
```

* How to uninstall a driver
```python
from webdriver_installer import ChromeDriver

chrome_installer = ChromeDriver()
chrome_installer.uninstall()
```

* How to disable the extra debug prints
```python
from webdriver_installer import DefaultDriver

DefaultDriver.DEBUG = False
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

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details
