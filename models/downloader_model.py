import json

class DownloaderModel:
    def __init__(self):
        with open('models/downloader_json/satellite_bands.json', 'r') as f:
            data = json.load(f)
            self.satellite_bands = {}
            for satellite, bands in data.items():
                self.satellite_bands[satellite] = []
                for band in bands:
                    code = band["code"]
                    description = band["description"]
                    self.satellite_bands[satellite].append({"code": code.strip(), "description": description.strip()})

    def get_satellites(self):
        return list(self.satellite_bands.keys())

    def get_bands(self, key):
        return self.satellite_bands[key]
