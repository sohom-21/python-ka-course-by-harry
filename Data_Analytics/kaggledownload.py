import kagglehub
import os

current_directory = os.getcwd()

# Download latest version
path = kagglehub.dataset_download("mojtaba142/hotel-booking")

print("Path to dataset files:", path)