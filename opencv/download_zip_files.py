# import os
# from urllib.request import urlretrieve
# from zipfile import ZipFile


# def download_unzip(url, save_path):
#     urlretrieve(url, save_path)
#     try:
#         with ZipFile(save_path) as zip:
#             zip.extractall(os.path.split(save_path)[0])
#     except Exception as e:
#         print(f"Invalid file,: {e}")


# URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

# current_working_dir = os.getcwd()

# asset_zip_path = os.path.join(current_working_dir, "opencv_bootcamp_assets_NB1.zip")


# if not os.path.exists(asset_zip_path):
#     print("DOES NOT EXIST NEED TO DOWNLOAD")
#     download_unzip(URL, asset_zip_path)

# # BUG: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)>
