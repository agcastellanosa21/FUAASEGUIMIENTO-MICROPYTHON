class Config:
    __value = {
        "wifiName": "TIGO-2632",
        "wifiPass": "4D9697502082"
    }

    @staticmethod
    def value(name):
        return Config.__value[name]
