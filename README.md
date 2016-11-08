# OSU Order Cookies
## Setup

```
pip3 install -U selenium
brew install chromedriver
```

* Make a new text document in the same directory of order_cookies.py formatted as such:
    * Line 1 - OSU Username (hazardj for example)
    * Line 2 - OSU Password (123456789 for example)
    * Line 3 - OSU Student ID (935999999 for example)
    * Line 4 - Phone Number (Optional for the website, but needed for the script)

## Usage

`python3 order_cookies.py [params]`

## Command Line Parameters

```
-m, --message [Message for Food2U Employees]
-n, --number [Number of Cookies to Order]
```
