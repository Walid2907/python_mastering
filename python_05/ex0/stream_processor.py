from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not isinstance(data, list):
            data = [data]
        # validating the input and raise ValueError if it fails
        try:
            if not self.validate(data):
                raise ValueError("Input is not Numeric")
        except ValueError as e:
            return f"{e}"
        count = len(data)
        total = sum(data)
        average = total / count
        pre_result = (f"Processed {count} numeric values, "
                      f"sum={total}, avg={average}")
        result = self.format_output(pre_result)
        return result

# method that validat the input
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for num in data:
            if not isinstance(num, (int, float)) or isinstance(num, bool):
                return False
        return True


# Processed text: 17 characters, 3 words
class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # validating the input and raise ValueError if it fails
        try:
            if not self.validate(data):
                raise ValueError("Input is not String")
        except ValueError as e:
            return f"{e}"
        characters = len(data)
        words = len(data.split())
        pre_result = (f"Processed text: "
                      f"{characters} characters, {words} words")
        result = self.format_output(pre_result)
        return result

# method that validat the input
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True


class LogProcessor(DataProcessor):
    # if u need mode logs add them to this dict
    __valid_levels = {"ERROR": "[ALERT]",
                      "INFO": "[INFO]",
                      "WARNING": "[WARNING]"}

    def process(self, data: Any) -> str:
        # validating the input and raise ValueError if it fails
        try:
            if not self.validate(data):
                raise ValueError("Input is not Log entry")
        except ValueError as e:
            return f"{e}"
        level, rest = data.split(":", 1)
        level = level.strip()
        rest = rest.strip()
        prefix = self.__valid_levels.get(level)
        pre_result = (f"{prefix} {level} "
                      f"level detected: {rest}")
        result = self.format_output(pre_result)
        return result

# method that validat the input
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ":" not in data:
            return False
        level, _ = data.split(":")
        if level.strip() not in self.__valid_levels.keys():
            return False
        return True


print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
# treating Numeric input
print("Initializing Numeric Processor...")
numeric = NumericProcessor()
my_list = [1, 2, "9"]
print(f"Processing data: {my_list}")
if numeric.validate(my_list):
    print("Validation: Numeric data verified")
out = numeric.process(my_list)

print(f"output :{out}\n")

# treating text
print("Initializing Text Processor...")
text = TextProcessor()
my_txt = "Hello Nexus World"
print(f"Processing data: {my_txt}")
if text.validate(my_txt):
    print("Validation: Text data verified")
out = text.process(my_txt)
print(f"output :{out}\n")

# treating Errors
print("Initializing Log Processor...")
log = LogProcessor()
my_log = "TEST: Connection timeout"
print(f"Processing data: {my_log}")
if log.validate(my_log):
    print("Validation: Log entry verified")
out = log.process(my_log)
print(f"output :{out}\n")

print("\n=== Polymorphic Processing Demo ===")
processors = [
    NumericProcessor(),
    TextProcessor(),
    LogProcessor()
]
data_inputs = [
    [1, 2, 3],
    "Hello World",
    "INFO: System ready"
]
for i in range(len(processors)):
    result = processors[i].process(data_inputs[i])
    print(f"Result {i + 1}: {result}")
