# simulator.py

import argparse
import json
from gui import start_gui
from cli import start_cli

def load_config(config_file="config.json"):
    """Load configuration from a JSON file."""
    with open(config_file, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="CC-Link RS485 Simulator")
    parser.add_argument("--mode", choices=["cli", "gui"], default="cli", help="Run in CLI or GUI mode")
    args = parser.parse_args()

    # Load configuration
    config = load_config()

    if args.mode == "cli":
        print("Starting in CLI mode...")
        start_cli(config)  # Pseudo-code: Start CLI interface
    elif args.mode == "gui":
        print("Starting in GUI mode...")
        start_gui(config)  # Pseudo-code: Start GUI interface

if __name__ == "__main__":
    main()