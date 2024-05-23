import os

class TumorDetector():
    data_path = 'data'
    current_training_directories = []
    child_directories = []
    unsplit_data = []
    train_data = []
    test_data =[]
    image_list = []

    def open_folder_and_files(self):
        exists = os.path.exists(self.data_path)
        if not exists:
            raise Exception('Data path entered does not exists')
        return exists
    
    def scan_sub_folders(self):
        print('Scanning sub directories')
        sub_dirs = []
        for root, dirs, files in os.walk(self.data_path):
            sub_dirs.append(dirs)
        self.child_directories.extend(sub_dirs)
        return self.child_directories
    
    def get_training_data(self):
        print("Geting training data")
        directories = self.child_directories[0]
        self.current_training_directories = [
            folder for folder in directories
            if 'brain_tumor_dataset' not in folder
        ]
        return self.current_training_directories

    def get_images(self):
        full_data = []
        for folder in self.current_training_directories:
            files = [
                x for x in os.listdir(
                    os.path.join(self.data_path, folder)
                ) 
            ]
            print(f"{folder} has {len(files)}")
            for file in files:
                folder_path = os.path.join(
                    self.data_path,
                    folder
                )
                full_path = os.path.join(folder_path, file)
                data = {
                    'prognosis': folder,
                    'path': full_path
                }
                full_data.append(data)
        self.unsplit_data.extend(full_data)
        return self.unsplit_data
    
    def make_csv_file(self):
        pass

    def split_data(self):
        pass

    def train_model(self):
        pass

    def save_model(self):
        pass

    def test_model(self):
        pass

    def start(self):
        self.open_folder_and_files()
        self.scan_sub_folders()
        self.get_training_data()
        self.get_images()
        print(self.unsplit_data)


td = TumorDetector()
td.start()