# Cyber-Shield: Kernel-Level Honeypot

A tool for those who believe the best defense is the one that operates at the speed of the kernel.

## Why this exists?
Traditional firewalls are often too slow for the modern threat landscape. Cyber-Shield doesn't just block access—it does so at the kernel level via eBPF, cutting off unwelcome guests before they even realize they’ve walked into a trap.

## How it works (The Honest Breakdown)
1. The Trap: A Python controller "listens" on a designated port, acting as a honeypot.
2. The Response: As soon as someone knocks, Cyber-Shield plays its "death song" and sends the attacker's IP straight to the kernel.
3. The Block: bpftool updates the eBPF map, slamming the door shut on that IP permanently.

## Engineering Philosophy
I believe security should be brutally effective, but there should always be room for poetry in the code. That’s why every intrusion attempt ends with a "death song" for the attacker.

## Prerequisites
- Linux kernel with eBPF support (5.x+)
- bpftool installed
- Python 3.6+
- Root/sudo privileges

## Usage

1. Ensure your eBPF map is loaded (e.g., via XDP/TC program):
    sudo bpftool map dump name BLACK_LIST

2. Run the honeypot controller:
    sudo python3 honeypot.py

3. Watch the logs as attackers get serenaded and banned.

## Why you should care
This is a clean, practical example of User Space (Python) interacting with Kernel Space (eBPF). Use it, break it, improve it, and don't let the sharks get too comfortable.

## License
MIT. Part of the ValkyrieSentinel ecosystem.
