export DISPLAY=localhost:4
Xvfb :4 &>/dev/null&
python3 -W ignore /export/home1/awatts/python/extbeams_plots/bnb.py
