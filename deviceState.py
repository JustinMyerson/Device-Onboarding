import enum

class deviceState(enum.Enum):
    DEVICE_RECEIVED = 1
    SERIAL_NUMBER_RECORDED = 2
    DELIVERY_INFO_RECORDED = 3
    DAMAGE_RECORDED = 4
    SIM_INSERTED_AND_RECORDED = 5
    FLASHED = 6
    KEY_INJECTED = 7
    SENT_FOR_REPACK = 8
    STORED_IN_WAREHOUSE = 9