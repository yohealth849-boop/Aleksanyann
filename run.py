import subprocess
import sys

def run_bots():
    # Միացնում ենք երկու բոտերն էլ միաժամանակ
    p1 = subprocess.Popen([sys.executable, "Aleksanyan.py"])
    p2 = subprocess.Popen([sys.executable, "shopstar.py"])
    
    p1.wait()
    p2.wait()

if name == "main":
    run_bots()