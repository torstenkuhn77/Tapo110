class State:
    pass

    def __init__(self, ) -> None:
        pass


class DefaultStates:
    type: str
    state: State

    def __init__(self, type: str, state: State) -> None:
        self.type = type
        self.state = state


class Result:
    device_id: str
    fw_ver: str
    hw_ver: str
    type: str
    model: str
    mac: str
    hw_id: str
    fw_id: str
    oem_id: str
    overheated: bool
    ip: str
    time_diff: int
    ssid: str
    rssi: int
    signal_level: int
    latitude: int
    longitude: int
    lang: str
    avatar: str
    region: str
    specs: str
    nickname: str
    has_set_location_info: bool
    device_on: bool
    on_time: int
    default_states: DefaultStates

    def __init__(self, device_id: str, fw_ver: str, hw_ver: str, type: str, model: str, mac: str, hw_id: str, fw_id: str, oem_id: str, overheated: bool, ip: str, time_diff: int, ssid: str, rssi: int, signal_level: int, latitude: int, longitude: int, lang: str, avatar: str, region: str, specs: str, nickname: str, has_set_location_info: bool, device_on: bool, on_time: int, default_states: DefaultStates) -> None:
        self.device_id = device_id
        self.fw_ver = fw_ver
        self.hw_ver = hw_ver
        self.type = type
        self.model = model
        self.mac = mac
        self.hw_id = hw_id
        self.fw_id = fw_id
        self.oem_id = oem_id
        self.overheated = overheated
        self.ip = ip
        self.time_diff = time_diff
        self.ssid = ssid
        self.rssi = rssi
        self.signal_level = signal_level
        self.latitude = latitude
        self.longitude = longitude
        self.lang = lang
        self.avatar = avatar
        self.region = region
        self.specs = specs
        self.nickname = nickname
        self.has_set_location_info = has_set_location_info
        self.device_on = device_on
        self.on_time = on_time
        self.default_states = default_states


class Welcome2:
    result: Result
    error_code: int

    def __init__(self, result: Result, error_code: int) -> None:
        self.result = result
        self.error_code = error_code
