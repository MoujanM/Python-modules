
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):

    def __init__(self, stream_id: Any) -> None:

        self.stream_id = stream_id
        self.stats: Dict[str, Any] = {"info": "",
                                      "priority": ""}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Each child-stream processes its own batch, parent knows none"""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Parent gives generic filter, child can specify."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Parent returns overall, child specifies."""
        return self.stats


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def _high_priority(self, item: Any) -> bool:
        try:
            if isinstance(item, dict):
                for val in item.values():
                    return float(val) > 50
            elif isinstance(item, str) and ":" in item:
                return float(item.rsplit(":", 1)[1]) > 50
        except Exception:
            return False

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        clean = [item for item in data_batch if isinstance(item, (str, dict))]
        if criteria == "high_priority":
            filtered = []
            count = 0
            for item in clean:
                if self._high_priority(item):
                    filtered.append(item)
                    count += 1

                if count > 0:
                    label = ("critical sensor alert" +
                             ("s" if count > 1 else ""))
                    self.stats["priority"] = f"{count} {label}"
                else:
                    self.stats["priority"] = ""
            return filtered
        return clean

    def process_batch(self, data_batch: List[Any]) -> str:

        clean_data = self.filter_data(data_batch)

        count = 0
        temp_count = 0
        temp_total = 0.0

        for data in clean_data:
            try:
                if isinstance(data, str) and ":" in data:
                    kind, val_str = data.rsplit(":", 1)
                    val = float(val_str)
                    if kind == "temp":
                        temp_count += 1
                        temp_total += val
                elif isinstance(data, dict):
                    for k, v in data.items():
                        kind, val = k, float(v)
                    if kind == "temp":
                        temp_count += 1
                        temp_total += val
                count += 1
            except (ValueError, TypeError):
                continue

        average = temp_total / temp_count if temp_count > 0 else 0
        stats_str = f"{count} readings processed"
        self.stats["info"] = stats_str
        return f"{stats_str}, avg temp: {average}˚C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def _high_priority(self, item: Any) -> bool:
        try:
            if isinstance(item, dict):
                for val in item.values():
                    return float(val) > 200
            elif isinstance(item, str) and ":" in item:
                return float(item.rsplit(":", 1)[1]) > 200
            else:
                return False
        except Exception:
            return False

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        clean = [item for item in data_batch if isinstance(item, (str, dict))]

        if criteria == "high_priority":
            filtered = []
            count = 0
            for item in clean:
                if self._high_priority(item):
                    filtered.append(item)
                    count += 1

                if count > 0:
                    label = "large transaction" + ("s" if count > 1 else "")
                    self.stats["priority"] = f"{count} {label}"
                else:
                    self.stats["priority"] = ""
            return filtered
        return clean

    def process_batch(self, data_batch: List[Any]) -> str:

        clean_data = self.filter_data(data_batch)

        kind = None

        count = 0
        buy_total = 0.0
        sell_total = 0.0

        for data in clean_data:
            try:
                if isinstance(data, dict):
                    for k, v in data.items():
                        kind, value = k, float(v)
                elif isinstance(data, str):
                    kind, val_str = data.rsplit(':')
                    value = float(val_str)

                if kind == "buy":
                    buy_total += value
                else:
                    sell_total += value

                count += 1
            except (ValueError, TypeError):
                continue

        stats_str = f"{count} operations processed"
        self.stats["info"] = stats_str
        net = int(buy_total - sell_total)
        sign = "+" if net > 0 else "-"
        return f"{stats_str}, net flow: {sign}{net} units"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def _high_priority(self, item: Any) -> bool:
        try:
            if isinstance(item, str):
                return item == "error"
            return False
        except Exception:
            return False

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        clean = [item for item in data_batch if isinstance(item, str)]
        if criteria == "high_priority":
            filtered = []
            count = 0
            for item in clean:
                if self._high_priority(item):
                    filtered.append(item)
                    count += 1

                if count > 0:
                    label = "error event" + ("s" if count > 1 else "")
                    self.stats["priority"] = f"{count} {label}"
                else:
                    self.stats["priority"] = ""
            return filtered
        return clean

    def process_batch(self, data_batch: List[Any]) -> str:

        clean_data = self.filter_data(data_batch)

        count = 0
        error_count = 0

        for event in clean_data:
            count += 1
            if event == "error":
                error_count += 1

        label = "event" + ("s" if count > 1 else "")
        stats_str = f"{count} {label} processed"
        self.stats["info"] = stats_str
        elabel = "error" + ("s" if error_count > 1 else "")
        res = f"{stats_str}, {error_count} {elabel} detected"
        return res


class StreamProcessor():
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]],
                    filter: Optional[str] = None) -> None:
        results = []
        i = 0
        for batch in batches:
            current_stream = self.streams[i]
            current_stream.process_batch(batch)
            results.append(current_stream.get_stats()["info"])
            i += 1

        return results

    def filter_data(self, batches: List[List[Any]],
                    filter: Optional[str] = None) -> str:
        i = 0
        results = []
        stream_count = 0
        for _ in self.streams:
            stream_count += 1

        for batch in batches:
            if i < stream_count:
                current_stream = self.streams[i]
                current_stream.filter_data(batch, criteria=filter)
                report = current_stream.get_stats()["priority"]
                if report:
                    results.append(report)
            i += 1
        return ", ".join(results)


if __name__ == "__main__":
    header = "code nexus - polymorphic stream system"
    print(f"=== {header.upper()} ===\n")

    test_data = {"sensor":
                 ["SENSOR_001: Environmental Data",
                     ["temp:22.5", "humidity:65", "pressure:1013"]],
                 "transaction":
                     ["TRANS_001: Financial Data",
                      ["buy:100", "sell:150", "buy: 75"]],
                 "event":
                     ["EVENT_001: System Events",
                      ["login", "error", "logout"]]}

    for label, test in test_data.items():
        print(f"Initializing {label.title()} Stream...")

        stream_id, data_type = test[0].rsplit(":")
        data = test[1]

        if label == "sensor":
            processor = SensorStream(stream_id)
        elif label == "transaction":
            processor = TransactionStream(stream_id)
        elif label == "event":
            processor = EventStream(stream_id)

        print(f"Stream ID: {stream_id}, Type: {data_type}")
        print(f"Processing sensor batch: {data}")
        analysis = processor.process_batch(data)
        print(f"{label} analysis: {analysis}\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams = [
        SensorStream("S-002"),
        TransactionStream("T-002"),
        EventStream("E-002")]
    stream_manager = StreamProcessor()
    stream_data = {
        "sensor":
            ["temp:56", "temp:80"],
        "transaction":
            [{"buy": 50}, {"sell": 200}, {"buy": 450}, {"sell": 40}],
        "event":
            ["login", "login", "logout"]
        }

    for stream in streams:
        stream_manager.add_stream(stream)

    print("\nBatch 1 Results:")

    results = stream_manager.process_all(stream_data.values())
    i = 0
    for name in stream_data:
        print(f"- {name.title()} data: {results[i]}")
        i += 1

    print("\nStream filtering active: High-priority data only")
    filtered_str = stream_manager.filter_data(stream_data.values(),
                                              filter="high_priority")
    print(f"Filtered results: {filtered_str}")

    print("\n All streams processed successfully. Nexus throughput optimal.")
    
