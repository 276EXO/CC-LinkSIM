# CC-Link RS485 Simulator
---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

---

## Introduction

The **CC-Link RS485 Simulator** is a lightweight, open-source tool designed to simulate CC-Link communication over an RS485 interface. It allows developers and engineers to test and debug CC-Link master-slave communication without requiring physical hardware. The simulator provides a virtual environment where you can emulate multiple devices on the same RS485 bus for testing purposes.

Whether you're developing CC-Link applications or troubleshooting existing systems, this simulator will save you time and effort by providing a flexible testing platform.

---

## Features

- **Simulated CC-Link Master/Slave Communication**: Simulate multiple CC-Link devices (masters and slaves) on an RS485 network.
- **Customizable Device Behavior**: Configure device responses, data registers, and error conditions.
- **Real-Time Monitoring**: Monitor RS485 traffic in real-time for debugging purposes.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux.
- **User-Friendly Interface**: Simple command-line or GUI-based interaction for ease of use.
- **Extensible Architecture**: Easily extendable to support additional protocols or custom behaviors.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- `pyserial` library (`pip install pyserial`)
- RS485-compatible hardware (optional, for physical testing)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cc-link-rs485-simulator.git
   cd cc-link-rs485-simulator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulator:
   ```bash
   python simulator.py
   ```

---

## Usage

### Command-Line Interface (CLI)

To start the simulator in CLI mode:
```bash
python simulator.py --mode cli
```

#### Available Commands:
- `start`: Start the simulation.
- `stop`: Stop the simulation.
- `add_device <id>`: Add a new simulated device with the specified ID.
- `remove_device <id>`: Remove a simulated device.
- `monitor`: Display live RS485 traffic.

Example:
```bash
> add_device 1
Device 1 added successfully.
> start
Simulation started.
```

### Graphical User Interface (GUI)

If you prefer a graphical interface, run:
```bash
python simulator.py --mode gui
```

The GUI provides a visual representation of the RS485 bus, allowing you to interact with devices and monitor communication.

---

## Configuration

The simulator's behavior can be customized using the `config.json` file. Here's an example configuration:

```json
{
  "baud_rate": 9600,
  "parity": "N",
  "stop_bits": 1,
  "devices": [
    {
      "id": 1,
      "registers": {
        "0x0000": 123,
        "0x0001": 456
      }
    },
    {
      "id": 2,
      "registers": {
        "0x0000": 789
      }
    }
  ]
}
```

- `baud_rate`: Set the baud rate for RS485 communication.
- `parity`: Parity setting (`N` for none, `E` for even, `O` for odd).
- `stop_bits`: Number of stop bits (1 or 2).
- `devices`: List of simulated devices with their IDs and register values.

---

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or feedback, feel free to reach out:

- **GitHub Issues**: [Open an issue](https://github.com/yourusername/cc-link-rs485-simulator/issues)

---

Thank you for using the CC-Link RS485 Simulator! We hope it helps streamline your development and debugging processes. If you find this tool useful, consider giving it a ⭐️ on GitHub!





oh, no, you've been phished :(
federico, marco
