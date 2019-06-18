# webassign_scraper

* quick and dirty Python scraper that uses [selenium](https://github.com/SeleniumHQ/selenium) to traverse this Javascript-riddled website

* this guide is written for Debian but the script will work on any platform



## dependencies needed

[selenium](https://github.com/SeleniumHQ/selenium)

[geckodriver](https://github.com/mozilla/geckodriver/releases)



## install selenium
* install with the following (or with pip in python console, pipenv, etc.)

```bash
pip3 install selenium
```



## download driver and place in PATH 
[geckodriver](https://github.com/mozilla/geckodriver/releases)
* use latest release appropriate for your os
* chrome and safari drivers will work too
* if unfamiliar with tar balls and adding to PATH, use the following commands

```bash
tar -xvzf geckodriver-v0.24.0-linux64.tar.gz
```
* make it executable with

```bash
chmod +x geckodriver
```
* add to your PATH with

```bash
sudo mv geckodriver /usr/local/bin
```

* *also make sure you have the latest release of the browser you are using*

## ensure shebang has correct path
```bash
which python3
```
* add appropriate path to top of python script like below

```bash
#! usr/local/bin/python3
```

## automate with cron

* once you test and confirm script works and scrapes data you want, create a cron job

```bash
crontab -e
```

* this will allow you to edit the cron jobs and there are examples for use
* check out [crontab guru](https://crontab.guru/) to play around with intervals
