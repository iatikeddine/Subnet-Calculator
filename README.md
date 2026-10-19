# Custom IPv4 Subnet Calculator

A lightweight, purely Python-based command-line IPv4 subnet calculator. This tool calculates the Network ID, Broadcast ID, and usable IP range for any given IPv4 address using either CIDR notation or a standard decimal subnet mask.

## Motivation

I built this project from scratch to deepen my understanding of core networking concepts, specifically focusing on low-level IPv4 packet mechanics and subnetting. Rather than relying on heavy external networking libraries to do the heavy lifting, this tool processes IP addresses using raw bitwise operations (`&`, `|`, `~`, `<<`). 

This approach serves as excellent practice for CCNA preparation and demonstrates a practical application of binary math, data validation, and Python scripting.

## Features

*   **Dual Input Formats:** Accepts input in both `Address/Prefix` (CIDR) and `Address Subnet_Mask` formats.
*   **Bitwise Calculations:** Uses efficient bitwise operations for fast and accurate network boundary calculations.
*   **Strict Validation:** Robust custom error handling ensures that non-numeric characters, out-of-range octets, and non-contiguous subnet masks are caught immediately with actionable feedback.
*   **Edge Case Handling:** Automatically detects and accurately formats `/31` (point-to-point links) and `/32` (single host routes) networks without breaking standard usable range math.
*   **Zero Dependencies:** Built entirely with Python's standard library.

## Prerequisites

*   Python 3.x installed on your system.

## Usage

You can run the calculator directly from your terminal. It takes arguments in one of two formats:

### 1. CIDR Notation (Prefix)
Provide the IP address and the prefix length separated by a slash (`/`).
```bash
make run ARGS="192.168.1.10/24"
```
**Output:**
```text
Network ID: 192.168.10.0
Broadcast ID: 192.168.10.255
Usable IP address range: 192.168.10.1 - 192.168.10.254
```

### 2. Standard Subnet Mask
Provide the IP address and the subnet mask separated by a space.
```bash
make run ARGS="10.0.0.5 255.255.255.0"
```
**Output:**
```text
Network ID: 10.0.0.0
Broadcast ID: 10.0.0.255
Usable IP address range: 10.0.0.1 - 10.0.0.254
```

### Edge Cases (/31 and /32)
The calculator intelligently handles special network sizes:
```bash
make run ARGS="172.16.0.2/31"
```
**Output:**
```text
This is a point-to-point network
First ip address: 172.16.0.2
Second ip address: 172.16.0.3
```

## Using the Makefile

A `Makefile` is included for quick testing and cleanup. 

*   `make help` - Show available commands.
*   `make clean` - Remove Python `__pycache__` directories.

## Project Structure

*   `src.py` - The main executable script containing the core bitwise calculation logic and standard output formatting.
*   `parsing.py` - The validation module responsible for parsing command-line arguments, verifying contiguous bits in subnet masks, and checking octet bounds.