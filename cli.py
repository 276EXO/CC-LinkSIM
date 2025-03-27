# cli.py

def start_cli(config):
    """Start the CLI interface."""
    print("Welcome to the CC-Link RS485 Simulator CLI!")
    print("Type 'help' for available commands.")

    devices = {}  # Simulated devices
    running = True

    while running:
        command = input("> ").strip().lower().split()
        if not command:
            continue

        cmd, *args = command

        if cmd == "help":
            print("Available commands:")
            print("  add_device <id> - Add a new device with the specified ID.")
            print("  remove_device <id> - Remove a device by ID.")
            print("  start - Start the simulation.")
            print("  stop - Stop the simulation.")
            print("  monitor - Monitor RS485 traffic.")
            print("  exit - Exit the simulator.")

        elif cmd == "add_device" and len(args) == 1:
            device_id = args[0]
            # Pseudo-code: Add a new device to the simulation
            devices[device_id] = {"registers": {}}
            print(f"Device {device_id} added successfully.")

        elif cmd == "remove_device" and len(args) == 1:
            device_id = args[0]
            # Pseudo-code: Remove a device from the simulation
            if device_id in devices:
                del devices[device_id]
                print(f"Device {device_id} removed successfully.")
            else:
                print(f"Device {device_id} not found.")

        elif cmd == "start":
            # Pseudo-code: Start the simulation loop
            print("Simulation started.")

        elif cmd == "stop":
            # Pseudo-code: Stop the simulation loop
            print("Simulation stopped.")

        elif cmd == "monitor":
            # Pseudo-code: Display live RS485 traffic
            print("Monitoring RS485 traffic...")

        elif cmd == "exit":
            print("Exiting simulator...")
            running = False

        else:
            print("Unknown command. Type 'help' for available commands.")