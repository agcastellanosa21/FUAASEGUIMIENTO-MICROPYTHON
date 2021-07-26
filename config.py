class Config:
    __value = {
        "wifiName": "",
        "wifiPass": ""
    }

    @staticmethod
    def value(name):
        return Config.__value[name]
