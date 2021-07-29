class Config:
    __value = {
        "wifiName": "TIGO-2632",
        "wifiPass": "4D9697502082",
        "vehicle": "WTO304",
        "updateGeoUrl": "http://192.168.1.5:8001/create-localization"
    }

    @staticmethod
    def value(name):
        return Config.__value[name]
