---

<p align="center"><img alt="PiHole OLED" src="https://xxcore.pl/pic/pihole_v2_06.jpg"></p>

<h1 align="center">PiHole Stats</h1>

<h4 align="center">A simple Python script to display PiHole stats on a SSD1306 OLED display.</h4>
<h4 align="center">Currently WIP</h4>

<p align="center">
<img alt="GitHub tag (latest by date)" src="https://img.shields.io/github/v/tag/XXCoreRangerX/piholestats?logo=github&style=flat-square">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/xxcorerangerx/piholestats?logo=github&style=flat-square">

<img alt="Python compatibility" src="https://img.shields.io/static/v1.svg?label=Compatibility&message=Python%203&logo=python&logoColor=white&color=green&style=flat-square">
</p>

---

<h2 align="center">Overview</h2>
<p align="justify">
  The script was originally built for my PiHole project (more details on <a href="https://xxcore.pl">my website</a>). It automatically starts on boot.

  It is compatible with a 128x64 0.96" SSD1306 OLED display. The script does not work with the 128x32 OLED display, but can be adjusted to do so.
</p>

<h2 align="center">Prerequisites and dependencies</h2>

Make sure I2C is enabled on your Raspberry Pi. In the `raspi-config` user interface navigate to `Interfacing Options >> I2C` and answer the question with `<Yes>`.

You might also want to improve I2C speed. To do this add the following line to the end of `/boot/config.txt`.
```
dtparam=i2c_baudrate=1000000
```

You have to install the following dependencies for PiHole Stats to work.
```console
apt install python3 python3-pip python3-pil
pip3 install adafruit-circuitpython-ssd1306
python3 -m pip install --no-cache-dir PiHole-api
```

<h2 align="center">Configuration</h2>

PiHole Stats requires some configuration to work correctly. Here's a small instruction to set it up:

1. Clone the repository:
```console
git clone https://github.com/xxcorerangerx/piholestats.git
cd piholestats
```
2. Move the `piholestats` directory to `/usr/local/bin/`:
```console
mv piholestats /usr/local/bin/
```
3. You have to make changes in the code for the script to work correctly. You can use any editor.

| Setting               | Priority    | Conditions                                                 | Line in the code |
| :-------------------: | :---------: | :--------------------------------------------------------: | :--------------: |
| Startup delay         | Optionally  | On a more powerful Raspberry Pi.                           | 21               |
| PiHole local IP       | NECESSARILY | -                                                          | 24               |
| Pin configuration     | Optionally  | -                                                          | 27               |
| Display configuration | NECESSARILY | If you're using a different screen/connection.             | 34               |
| Padding configuration | Optionally  | May have to be changed on a different screen.              | 79               |
| Font configuration    | NECESSARILY | On a different screen / to use a different font.           | 85               |
| PiHole password       | NECESSARILY | -                                                          | 93               |
| Main UI elements      | NECESSARILY | On a different screen, because not all elements might fit. | 113              |

4. Download the font.

>The font used in the pictures is [Baloo Bhai 2](https://fonts.google.com/specimen/Baloo+Bhai+2). You can use any other font, but the UI configuration and paddings might differ! You have to download it separately, unzip and place in the script directory (e.g. `/usr/local/bin/piholestats/BalooBhai2-Regular.regular` and `/usr/local/bin/piholestats/BalooBhai2-Bold.regular`). Don't forget to modify `font` and `font_title` variables in the script.

>You can also use the default font (still have to modify the UI elements):
```
font = ImageFont.load_default()
font_title = ImageFont.load_default()
```

4. Move the `piholestats.service` service to `/etc/systemd/system/piholestats.service`.
```console
mv piholestats.service /etc/systemd/system/
```
5. Execute the following commands in the terminal to set up the service:
```console
systemctl daemon-reload
systemctl enable piholestats
systemctl start piholestats
```
6. The script should now start and automatically start on the next boot.

---

## About
Created by [XXCoreRangerX](https://github.com/XXCoreRangerX) (mail@xxcore.pl)

## License
This project is licensed under the [MIT license](https://github.com/xxcorerangerx/piholestats/blob/master/LICENSE).
