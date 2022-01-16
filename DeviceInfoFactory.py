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


class DeviceInfo:
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

class DeviceInfoFactory:
    result: dict
    error_code: int

    def __init__(self, result: dict, error_code: int) -> None:
        self.result = result
        self.error_code = error_code

    def serialize(self) -> DeviceInfo:
        res = DeviceInfo()
        res.device_id = self.result['device_id']
        res.fw_ver = self.result['fw_ver']
        res.hw_ver = self.result['hw_ver']
        res.type = self.result['type']
        res.model = self.result['model']
        res.mac = self.result['mac']
        res.hw_id = self.result['hw_id']
        res.fw_id = self.result['fw_id']
        res.oem_id = self.result['oem_id']
        res.overheated = self.result['overheated']
        res.ip = self.result['ip']
        res.time_diff = self.result['time_diff']
        res.ssid = self.result['ssid']
        res.rssi = self.result['rssi']
        res.signal_level = self.result['signal_level']
        res.latitude = self.result['latitude']
        res.longitude = self.result['longitude']
        res.lang = self.result['lang']
        res.avatar = self.result['avatar']
        res.region = self.result['region']
        res.specs = self.result['specs']
        res.nickname = self.result['nickname']
        res.has_set_location_info = self.result['has_set_location_info']
        res.device_on = self.result['device_on']
        res.on_time = self.result['on_time']
        res.default_states = self.result['default_states']
        return res


