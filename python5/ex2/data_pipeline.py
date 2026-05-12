# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_pipeline.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: vsack <vsack@student.42vienna.com>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/12 17:03:33 by vsack           #+#    #+#               #
#  Updated: 2026/05/12 17:05:58 by vsack           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        data = self._storage.pop(0)
        current_rank = self._rank
        self._rank += 1
        return current_rank, data


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None: ...


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item[1] for item in data]
        cvs_string = ", ".join(values)
        print(f"CSV Output:\n{cvs_string}")


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_value = []
        for rank, value in data:
            entry = f'"item_{rank}": "{value}"'
            json_value.append(entry)
        json_string = "{" + ", ".join(json_value) + "}"
        print(f"JSON Output:\n{json_string}")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Incorrect numeric data")
        if isinstance(data, (int, float)):
            self._storage.append(str(data))
        elif isinstance(data, list):
            for item in data:
                self._storage.append(str(item))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Incorrect string data")
        if isinstance(data, str):
            self._storage.append(str(data))
        elif isinstance(data, list):
            for item in data:
                self._storage.append(str(item))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list):
            return all(isinstance(item, dict) for item in data)
        else:
            return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise TypeError("Incorrect dictionary data")
        if isinstance(data, dict):
            formatted_str = f"{data['log_level']}: {data['log_message']}"
            self._storage.append(formatted_str)
        elif isinstance(data, list):
            for item in data:
                formatted_str = f"{item['log_level']}: {item['log_message']}"
                self._storage.append(formatted_str)


class DataStream:
    def __init__(self) -> None:
        self.procs_reg: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.procs_reg.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processor_found = False
            for processor in self.procs_reg:
                if processor.validate(item):
                    processor.ingest(item)
                    processor_found = True
                    break
            if not processor_found:
                print(
                    f"DataStream error: Can't process "
                    f"element in stream: {item}")

    def print_processor_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self.procs_reg:
            print("No processor found, no data")
            return
        for proc in self.procs_reg:
            name = type(proc).__name__.replace("Processor", " Processor")
            remaining = len(proc._storage)
            total = remaining + proc._rank
            print(
                f"{name}: total {total} items processed, remaining "
                f"{remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        all_data: list[tuple[int, str]] = []
        for proc in self.procs_reg:
            for _ in range(nb):
                try:
                    item = proc.output()
                    all_data.append(item)
                except IndexError:
                    break
        if all_data:
            plugin.process_output(all_data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    stream = DataStream()
    stream.print_processor_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
             "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch1}\n")
    stream.process_stream(batch1)
    stream.print_processor_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExport())
    print()
    stream.print_processor_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message":
             "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch2}\n")
    stream.process_stream(batch2)
    stream.print_processor_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExport())
    print()
    stream.print_processor_stats()
