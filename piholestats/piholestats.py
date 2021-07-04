#
# ██████╗ ██╗██╗  ██╗ ██████╗ ██╗     ███████╗    ███████╗████████╗ █████╗ ████████╗███████╗
# ██╔══██╗██║██║  ██║██╔═══██╗██║     ██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
# ██████╔╝██║███████║██║   ██║██║     █████╗      ███████╗   ██║   ███████║   ██║   ███████╗
# ██╔═══╝ ██║██╔══██║██║   ██║██║     ██╔══╝      ╚════██║   ██║   ██╔══██║   ██║   ╚════██║
# ██║     ██║██║  ██║╚██████╔╝███████╗███████╗    ███████║   ██║   ██║  ██║   ██║   ███████║
# ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
#

# Place this file in /usr/local/bin/piholestats/piholestats.py

# Dependencies
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pihole as ph

# Startup delay
time.sleep(15)

# PiHole local IP address
pihole = ph.PiHole("192.168.1.2")

# Raspberry Pi pin configuration
RST = 24
# Note the following are only used with SPI:
# DC = 23
# SPI_PORT = 0
# SPI_DEVICE = 0

# Raspberry Pi Display configuration
# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128x32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)


# Advanced display configuration
# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)


# Initialize library and clear the display.
disp.begin()
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Padding configuration
padding = -2
top = padding
bottom = height-padding
x = 0

# Font configuration
font = ImageFont.truetype('/usr/local/bin/piholestats/BalooBhai2-Regular.ttf', 12)
font_title = ImageFont.truetype('/usr/local/bin/piholestats/BalooBhai2-Bold.ttf', 17)

# Main loop
while True:
    draw.rectangle((x,x,127,63), outline=255, fill=0)

    # PiHole password
    pihole.authenticate("PASSWORD")

    # PiHole API variables
    status = pihole.status
    blocked = pihole.blocked
    queries = pihole.queries
    percent = pihole.ads_percentage

    # Refresh PiHole API data
    pihole.refresh()

    if status == "enabled":
        # Execute code when PiHole is enabled

        status1 = "ON"

        # Clear the display
        disp.clear()

        # Draw the UI
        draw.text((x, top),       " Pihole              " + str(status1), font=font_title, fill=255)
        draw.text((x, top+15),    "  Queries   " + str(queries),  font=font, fill=255)
        draw.text((x, top+27),    "  Blocked   " + str(blocked),  font=font, fill=255)
        draw.text((x, top+36),    "  Percent   " + str(percent) + " %",  font=font, fill=255)

        # Draw a progress bar showing percent of blocked traffic
        pct_bar=127*(int(float(percent))/100)
        draw.rectangle((pct_bar, 63, 0, 50), fill="white")
        draw.rectangle((127, 63, 0, 50), outline="white")

        # Display the UI
        disp.image(image)
        disp.display()
    else:
        # Execure code when PiHole is disabled

        status1 = "OFF"

        # Clear the display
        disp.clear()

        # Draw the UI
        draw.text((x, top),       " Pihole              " + str(status1), font=font_title, fill=255)

        # Display the UI
        disp.image(image)
        disp.display()
    # UI refresh delay
    time.sleep(0.1)
