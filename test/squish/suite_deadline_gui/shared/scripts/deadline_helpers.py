# -*- coding: utf-8 -*-
import subprocess

def print_deadline_version():
    try:
        result = subprocess.run(['deadline', '--version'], capture_output=True, text=True, check=True)
        print(f"Deadline version: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to get Deadline version. {e}")
    except FileNotFoundError:
        print("Error: Deadline command not found. Make sure it's installed and in your PATH.")
        