import json
from datetime import datetime
from typing import List

class EnergyUsage:
    today_runtime: int
    month_runtime: int
    today_energy: int
    month_energy: int
    local_time: datetime
    past24h: List[int]
    past30d: List[int]
    past1y: List[int]
    past7d: List[List[int]]
    current_power: int

class EnergyUsageFactory:
    result: dict
    error_code: int

    def __init__(self, result: dict, error_code: int) -> None:
        self.result = result
        self.error_code = error_code

    def deserialize(self) -> EnergyUsage:
        res = EnergyUsage()
        res.today_runtime = self.result['today_runtime']
        res.month_runtime = self.result['month_runtime']
        res.today_energy = self.result['today_energy']
        res.month_energy = self.result['month_energy']
        res.local_time = self.result['local_time']
        res.past24h = self.result['past24h']
        res.past30d = self.result['past30d']
        res.past1y = self.result['past1y']
        res.past7d = self.result['past7d']
        res.current_power = self.result['current_power']

        return res
        