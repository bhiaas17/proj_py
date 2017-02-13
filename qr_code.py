#!/usr/bin/env python2
import webbrowser
import os
os.system("python input.py | qrencode -o qr_out.png -s 10x8| firefox qr_out.png")
