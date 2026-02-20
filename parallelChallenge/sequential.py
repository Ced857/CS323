import time

def process_patient(patient_id):
    time.sleep(1)# record checking
    time.sleep(1)# questioning
    time.sleep(2) # ultrasound scan

patients = list(range(7))

start = time.time()
for patient in patients:
    process_patient(patient)
end = time.time()

print("Sequential Time:", round(end - start, 2), "seconds")


import time
from concurrent.futures import ThreadPoolExecutor

def process_patient(patient_id):
    time.sleep(1)
    time.sleep(1)
    time.sleep(2)



