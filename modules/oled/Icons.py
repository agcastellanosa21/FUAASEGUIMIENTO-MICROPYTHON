WIDTH = 50
HEIGHT = 50


def Wifi():
    return [
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x07, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3f, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8,
        0x07, 0xc0, 0x00, 0x00, 0x00, 0x01, 0xec, 0x31, 0xe0, 0x00, 0x00, 0x00, 0x03, 0x8c, 0x30, 0x70,
        0x00, 0x00, 0x03, 0xfe, 0x00, 0x07, 0xff, 0xf0, 0x00, 0x0f, 0xfc, 0x61, 0x9f, 0xff, 0xfc, 0x00,
        0x1e, 0x18, 0x61, 0xb8, 0x00, 0x0e, 0x00, 0x38, 0x00, 0x00, 0x60, 0x00, 0x07, 0x00, 0x70, 0xc3,
        0x00, 0xe0, 0x00, 0x03, 0x80, 0x70, 0xc3, 0x00, 0xc0, 0x00, 0x01, 0x80, 0xe0, 0x00, 0x1c, 0xc0,
        0x00, 0x60, 0xc0, 0xc7, 0x39, 0xdc, 0xc3, 0xfe, 0xe0, 0xc0, 0xc7, 0x39, 0x9c, 0xc3, 0xfe, 0x60,
        0xc0, 0xc3, 0x3b, 0x80, 0xc3, 0x80, 0x00, 0xc0, 0xf3, 0xfb, 0x9c, 0xc3, 0x80, 0xe0, 0xc0, 0xf3,
        0xff, 0x9c, 0xc3, 0x80, 0xe0, 0xc0, 0xc3, 0xff, 0x9c, 0xc3, 0xfc, 0xe0, 0xc0, 0xc1, 0xef, 0x1c,
        0xc3, 0xfc, 0xe0, 0xc0, 0xc1, 0xef, 0x1c, 0xc3, 0xfc, 0xe0, 0xc0, 0xc1, 0xef, 0x1c, 0xc3, 0x80,
        0xe0, 0xc0, 0xf1, 0xef, 0x1c, 0xc3, 0x80, 0xe0, 0xc0, 0xf1, 0xc6, 0x1c, 0xc3, 0x80, 0xe0, 0xc0,
        0x60, 0x00, 0x00, 0xc0, 0x00, 0x01, 0x80, 0x76, 0x18, 0x61, 0xc0, 0x00, 0x03, 0x80, 0x3e, 0x18,
        0x61, 0x80, 0x00, 0x07, 0x00, 0x1e, 0x00, 0x07, 0x00, 0x00, 0x0e, 0x00, 0x0f, 0xff, 0x3f, 0xff,
        0xff, 0xfc, 0x00, 0x03, 0xff, 0x3f, 0xff, 0xff, 0xf0, 0x00, 0x00, 0x03, 0x80, 0x00, 0x78, 0x00,
        0x00, 0x00, 0x01, 0xe1, 0x87, 0xe0, 0x00, 0x00, 0x00, 0x00, 0xf9, 0x87, 0xc0, 0x00, 0x00, 0x00,
        0x00, 0x3f, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
    ]


def Gps():
    return [
        0x00, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff,
        0xf8, 0x00, 0x00, 0x00, 0x00, 0x07, 0xc0, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x1e, 0x00,
        0x00, 0x00, 0x00, 0x1c, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x38, 0x00, 0x07, 0xbc, 0x00, 0x00,
        0x00, 0x38, 0x1f, 0x03, 0xff, 0xe0, 0x00, 0x00, 0x70, 0x7f, 0x83, 0xff, 0xf8, 0x00, 0x00, 0x70,
        0xff, 0xc1, 0xe7, 0xfe, 0x00, 0x00, 0xe0, 0xe1, 0xe1, 0xc3, 0x9f, 0x80, 0x00, 0xe1, 0xc0, 0xe1,
        0xc3, 0x87, 0xc0, 0x00, 0xe1, 0xc0, 0x60, 0xc1, 0xc1, 0xe0, 0x00, 0xe1, 0xc0, 0x60, 0xc1, 0xc0,
        0xf0, 0x00, 0xe1, 0xc0, 0xe1, 0xc0, 0xc0, 0x78, 0x00, 0xe1, 0xe0, 0xe1, 0xc0, 0xe0, 0x3c, 0x00,
        0x70, 0xf3, 0xc1, 0xc0, 0xe0, 0x1c, 0x00, 0x70, 0x7f, 0xc1, 0x80, 0xe0, 0x0e, 0x00, 0x70, 0x3f,
        0x03, 0x80, 0x60, 0x0f, 0x00, 0x38, 0x00, 0x07, 0x80, 0x70, 0x07, 0x00, 0x3c, 0x00, 0x0f, 0x00,
        0x70, 0x07, 0x00, 0x1e, 0x00, 0x1e, 0x00, 0x70, 0x03, 0x80, 0x0f, 0x00, 0x3e, 0x00, 0x70, 0x03,
        0x80, 0x07, 0x80, 0x3e, 0x00, 0x70, 0x03, 0x80, 0x03, 0xc0, 0x7e, 0x00, 0x70, 0x01, 0xc0, 0x01,
        0xe0, 0xfe, 0x00, 0x30, 0x01, 0xc0, 0x03, 0xf3, 0xfe, 0x00, 0x78, 0x01, 0xc0, 0x03, 0xff, 0xff,
        0xff, 0xff, 0xff, 0xc0, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 0x03, 0xff, 0xff, 0xff, 0xff,
        0xff, 0xc0, 0x01, 0x8c, 0x0e, 0x00, 0x30, 0x01, 0xc0, 0x01, 0x80, 0x0e, 0x00, 0x70, 0x01, 0xc0,
        0x01, 0xc0, 0x0e, 0x00, 0x70, 0x01, 0x80, 0x01, 0xc0, 0x0e, 0x00, 0x70, 0x03, 0x80, 0x01, 0xc0,
        0x0e, 0x00, 0x70, 0x03, 0x80, 0x00, 0xe0, 0x0e, 0x00, 0x70, 0x03, 0x00, 0x00, 0xe0, 0x06, 0x00,
        0x70, 0x07, 0x00, 0x00, 0x70, 0x06, 0x00, 0x60, 0x07, 0x00, 0x00, 0x70, 0x07, 0x00, 0x60, 0x0e,
        0x00, 0x00, 0x38, 0x07, 0x00, 0xe0, 0x1e, 0x00, 0x00, 0x3c, 0x07, 0x00, 0xe0, 0x3c, 0x00, 0x00,
        0x1e, 0x03, 0x00, 0xe0, 0x38, 0x00, 0x00, 0x0f, 0x03, 0x81, 0xc0, 0xf0, 0x00, 0x00, 0x07, 0x83,
        0x81, 0xc1, 0xe0, 0x00, 0x00, 0x03, 0xe1, 0xc1, 0xc3, 0xc0, 0x00, 0x00, 0x01, 0xf9, 0xc3, 0x8f,
        0x80, 0x00, 0x00, 0x00, 0x7f, 0xe7, 0xff, 0x00, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xfc, 0x00, 0x00,
        0x00, 0x00, 0x07, 0xff, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0x00
    ]
