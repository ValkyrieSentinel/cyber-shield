import socket
import struct
import subprocess
import time

PORT = 1234
MAP_NAME = "BLACK_LIST"

def sing_death_song(ip):
    print(f"\n [DEATH SONG OF THE TRAP]")
    print(f" Oh, come closer, little shark from {ip}...")
    print(f" Your packet is tasty, but this port is not for you.")
    print(f" Chick-chicka-whoop-whoop! Snap — and you're lost in the kernel's dark!")
    print(f" Adding your code to the eternal BLACK_LIST...\n")

def ban_ip_in_ebpf(ip_str):
    """
    Updates the kernel-level eBPF map to block the specified IP.
    """
    try:
        packed_ip = socket.inet_aton(ip_str)
        key_hex = " ".join(f"{b:02x}" for b in packed_ip)
        value_hex = "01 00 00 00"

        cmd = ["sudo", "bpftool", "map", "update", "name", MAP_NAME, "key", "hex", key_hex, "value", "hex", value_hex]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f" [KERNEL] Map updated. IP {ip_str} is now under lockdown.")
        else:
            print(f" [KERNEL ERROR] Error: {result.stderr}")
    except Exception as e:
        print(f" [SWORD ERROR] {e}")

def start_trap():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', PORT))
            s.listen(128)
            print("===========================================")
            print("      PYTHON SWORD: POETIC EXECUTION      ")
            print(f"    Listening on: {PORT} | Target: {MAP_NAME}")
            print("===========================================")
            while True:
                conn, addr = s.accept()
                shark_ip = addr[0]
                sing_death_song(shark_ip)
                ban_ip_in_ebpf(shark_ip)
                try:
                    conn.sendall(b"Chick-chicka-whoop-whoop! Goodbye, shark.\n")
                    conn.close()
                except: pass
    except Exception as e:
        print(f" CATASTROPHE: {e}")

if __name__ == "__main__":
    start_trap()
