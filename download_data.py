import os
import zipfile

# 1. Install the Kaggle library if not already installed
try:
    import kaggle
except ImportError:
    print("Kaggle library not found. Installing...")
    os.system('pip install kaggle')
    print("Please ensure you have your kaggle.json file in ~/.kaggle/")

def download_kaggle_dataset():
    # The dataset slug for the famous Credit Card Fraud Detection dataset
    dataset_slug = "mlg-ulb/creditcardfraud"
    
    print(f"Downloading {dataset_slug}...")
    
    # Download the dataset using the Kaggle API
    # This looks for kaggle.json in your home folder (.kaggle/kaggle.json)
    os.system(f'kaggle datasets download -d {dataset_slug}')
    
    # Unzip the file
    zip_name = "creditcardfraud.zip"
    if os.path.exists(zip_name):
        print("Unzipping dataset...")
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        # Clean up zip file to save space
        os.remove(zip_name)
        print("Download and extraction complete!")
    else:
        print("Error: Download failed. Check your Kaggle API credentials.")

if __name__ == "__main__":
    download_kaggle_dataset()