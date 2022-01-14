from datetime import datetime
from typing import List


class Result:
    today_runtime: int
    month_runtime: int
    today_energy: int
    month_energy: int
    local_time: datetime
    past24_h: List[int]
    past30_d: List[int]
    past1_y: List[int]
    past7_d: List[List[int]]
    current_power: int

    def __init__(self, today_runtime: int, month_runtime: int, today_energy: int, month_energy: int, local_time: datetime, past24_h: List[int], past30_d: List[int], past1_y: List[int], past7_d: List[List[int]], current_power: int) -> None:
        self.today_runtime = today_runtime
        self.month_runtime = month_runtime
        self.today_energy = today_energy
        self.month_energy = month_energy
        self.local_time = local_time
        self.past24_h = past24_h
        self.past30_d = past30_d
        self.past1_y = past1_y
        self.past7_d = past7_d
        self.current_power = current_power


class Welcome3:
    result: Result
    error_code: int

    def __init__(self, result: Result, error_code: int) -> None:
        self.result = result
        self.error_code = error_code
