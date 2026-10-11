
from typing import Any, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    data_type = "Generic"
    """abstract class defining the common processing interface"""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    data_type = "Numeric data"

    def validate(self, data: Any) -> bool:
        try:
            for datum in data:
                datum + 0  # check if datum is int
            data[0]  # check if data is subscriptable
            return True
        except TypeError:
            return False

    def process(self, data: Union[List[float], List[int]]) -> str:
        count = 0
        total = 0
        for num in data:
            count += 1
            total += num

        avrg = total / count if count > 0 else 0
        result_pref = f"Processed {count} numeric values, "
        result = f"sum={total}, avg={avrg:.1f}"
        return (result_pref + result)

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    data_type = "Text data"

    def validate(self, data: Any) -> bool:
        try:
            data.upper()
            return True
        except TypeError:
            return False

    def process(self, data: str) -> str:
        char_count = 0
        word_count = data.count(' ') + 1

        for char in data:
            if char.isprintable():
                char_count += 1

        result = f"{char_count} charachters, {word_count} words"
        return result

    def format_output(self, result: str) -> str:
        result_str = "Processed text: "
        return super().format_output(result_str + result)


class LogProcessor(DataProcessor):

    data_type = "log entry"

    def validate(self, data: Any) -> bool:
        try:
            data.items()
            return True
        except TypeError:
            return False

    def process(self, data: dict) -> str:
        prefix = ""
        for log_type, msg in data.items():
            if log_type == "ERROR":
                prefix = "[ALERT]"
            elif log_type == "INFO":
                prefix = "[INFO]"
        result = f"{prefix} {log_type} level detected: {msg}"
        return result

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    header = "code nexus - data processor foundation"
    print(f"=== {header.upper()} ===\n")

    data_to_process = {
        "Numeric Processor": [NumericProcessor(), [1, 2, 3, 4, 5]],
        "Text Processor": [TextProcessor(), "Hello Nexus World"],
        "Log Processor": [LogProcessor(), {"ERROR": "Connection timeout"}]
    }

    for label, test_case in data_to_process.items():
        processor = test_case[0]
        test_data = test_case[1]

        print(f"Initializing {label}... ")
        if isinstance(test_data, str):
            print(f"Processing data: \"{test_data}\"")
        else:
            print(f"Processing data: {test_data}")

        if processor.validate(test_data):
            print(f"Validation: {processor.data_type} verified")

        result = processor.process(test_data)
        output_str = processor.format_output(result)
        print(f"Output: {output_str}\n")

    print("\n=== Polymorphic Processing Deemo ===")

    processors = [NumericProcessor(),
                  TextProcessor(),
                  LogProcessor()]
    poly_data = [[1, 2, 3],
                 "Hello world!",
                 {"INFO": "System ready"}]

    print("Processing multiple types through same interface...")
    for i in range(len(poly_data)):
        processor = processors[i]
        data = poly_data[i]

        result = processor.process(data)
        output = processor.format_output(result)
        print(f"Result {i + 1}: {output}")

    print("\nFoundation system online. Nexus ready for advanced streams.")
