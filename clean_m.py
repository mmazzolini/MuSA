import config as cfg
#use python to remove the files from cfg.intermediate and cfg.results
import shutil
import os
import config as cfg
import shutil



# Remove the files inside cfg.output_path
for file_name in os.listdir(cfg.output_path):
    file_path = os.path.join(cfg.output_path, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Remove the files inside cfg.intermediate_path
for file_name in os.listdir(cfg.intermediate_path):
    file_path = os.path.join(cfg.intermediate_path, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
        