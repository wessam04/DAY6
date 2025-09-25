import logging

logging.basicConfig(level=logging.INFO)
logging.info("student name and grades are saved")

with open("grades.txt","w") as f:
    f.write("Ali, A")