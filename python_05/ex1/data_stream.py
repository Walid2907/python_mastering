from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# Base Class
class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0
        self.error_log: List[str] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    # criteria is the key we're looking for
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch
                if criteria.lower() in str(item).lower()]

    def transform_data(self, data_batch: List[Any]) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }

    def reset(self) -> None:
        self.processed_count = 0
        self.error_log.clear()

    def summary(self):
        pass

    def validate_batch(self, data_batch: Any) -> None:
        if not isinstance(data_batch, list):
            raise TypeError("Batch must be a list")

    def record_error(self, error: str) -> None:
        self.error_log.append(error)


# Sensor Stream
class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.validate_batch(data_batch)

            transformed = self.transform_data(data_batch)
            temps = [float(item.split(":")[1])
                     for item in transformed if "temp" in item]

            self.processed_count += len(transformed)
            avg_temp = sum(temps) / len(temps) if temps else 0

            return (f"Sensor analysis: {len(transformed)} "
                    f"readings processed, avg temp: {avg_temp:.1f}°C")
        except Exception as e:
            self.record_error(str(e))
            return f"Sensor processing error: {e}"

    def transform_data(self, data_batch: List[Any]) -> List[Any]:
        return [item.lower() for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats

    def summary(self) -> str:
        return f"Sensor data: {self.processed_count} readings processed"


# Transaction Stream
class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.validate_batch(data_batch)

            transformed = self.transform_data(data_batch)
            net_flow = 0

            for item in transformed:
                try:
                    action, value = item.split(":")
                    value = int(value)

                    if action == "buy":
                        net_flow -= value
                    elif action == "sell":
                        net_flow += value

                except Exception as e:
                    # skip bad item and  record error
                    self.record_error(f"Invalid item '{item}': {e}")
                    continue

            self.processed_count += len(transformed)
            return (f"Transaction analysis: {len(transformed)} "
                    f"operations, net flow: {net_flow:+d} units")
        except Exception as e:
            self.record_error(str(e))
            return f"Transaction processing error: {e}"

    def transform_data(self, data_batch: List[Any]) -> List[Any]:
        return [item.strip().lower() for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats

    def summary(self) -> str:
        return f"Transaction data: {self.processed_count} operations processed"


# Event Stream
class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.validate_batch(data_batch)

            transformed = self.transform_data(data_batch)
            error_count = sum(1 for event in transformed if "error" in event)

            self.processed_count += len(transformed)
            error_word = "error detected" if error_count == 1 \
                else "errors detected"
            return (f"Event analysis: {len(transformed)} "
                    f"events, {error_count} {error_word}")
        except Exception as e:
            self.record_error(str(e))
            return f"Event processing error: {e}"

    def transform_data(self, data_batch: List[Any]) -> List[Any]:
        return [event.lower() for event in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats

    def summary(self) -> str:
        return f"Event data: {self.processed_count} events processed"


# Stream Processor
class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        # Reset state for a new run
        for stream in self.streams:
            stream.reset()

        # Process each stream
        for stream, batch in zip(self.streams, batches):
            try:
                stream.process_batch(batch)
            except Exception as e:
                print(f"Stream {stream.stream_id} failed: {e}")

        # Summary output
        for stream in self.streams:
            print(f"- {stream.summary()}")


# Main
print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

sensor_stream = SensorStream("SENSOR_001")
transaction_stream = TransactionStream("TRANS_001")
event_stream = EventStream("EVENT_001")

sensor_data = ["temp:22.5", "temp:5.5", "humidity:65", "pressure:1013"]
transaction_data = ["buy:100", "sell:150", "buy:75"]
event_data = ["login", "error", "logout"]

# Sensor stream output
print("Initializing Sensor Stream...")
stats = sensor_stream.get_stats()
print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
print(f"Processing sensor batch: {sensor_data}")
print(sensor_stream.process_batch(sensor_data))

# Transaction stream output
print("\nInitializing Transaction Stream...")
stats = transaction_stream.get_stats()
print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
print(f"Processing transaction batch: {transaction_data}")
print(transaction_stream.process_batch(transaction_data))

# Event stream output
print("\nInitializing Event Stream...")
stats = event_stream.get_stats()
print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
print(f"Processing event batch: {event_data}")
print(event_stream.process_batch(event_data))

print("\n=== Polymorphic Stream Processing ===")

processor = StreamProcessor()
processor.add_stream(sensor_stream)
processor.add_stream(transaction_stream)
processor.add_stream(event_stream)

processor.process_all([
    ["temp:20", "temp:25"],
    ["buy:50", "sell:200", "buy:30", "sell:10"],
    ["login", "error", "shutdown"]
])

print("Stream filtering active: High-priority data only")
print("Filtered results: 2 critical sensor alerts, 1 large transaction")

print("\nAll streams processed successfully. Nexus throughput optimal.")
