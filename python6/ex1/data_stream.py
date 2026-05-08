# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_stream.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 21:23:55 by vsack             #+#    #+#              #
#    Updated: 2026/05/08 21:05:50 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
                    f"DataStream error: Can't process element in stream: {item}"
                )

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
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processor_stats()
    print("\nRegistering Processors\n")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)

    batch = [
        "HEYYYYY",
        [1, 1.321, 231, 23],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processor_stats()

    print("\nRegistering other data processors")
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processor_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    # We manually call output() to remove items from the queues
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream.print_processor_stats()
