#intrusion detection system

import tkinter as tk
import psutil
import logging
from tkinter import messagebox
import subprocess
import time
import threading
import socket

# Configure logging
logging.basicConfig(filename='ids_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to check if the IP is authorized
def is_authorized(ip):
    authorized_ips = authorized_ips_entry.get().split(',')
    return ip in authorized_ips

# Function to handle incoming IP address
def handle_ip():
    ip = ip_entry.get()
    if is_authorized(ip):
        result_label.config(text=f"Authorized: {ip}", fg="green")
        messagebox.showinfo("Intrusion Detected", f"Authorised IP ! \n Access Allowed : {ip}")


    else:
        result_label.config(text=f"Suspicious: {ip}", fg="red")
        log_suspicious_ip(ip)
        alert_suspicious_ip(ip)
        block_suspicious_ip(ip)

# Function to log suspicious IP addresses
def log_suspicious_ip(ip):
    logging.info(f"Suspicious IP detected: {ip}")

# Function to display an alert when a suspicious IP is detected
def alert_suspicious_ip(ip):
    messagebox.showwarning("Intrusion Detected", f"Suspicious IP detected: {ip}")

# Function to block or quarantine suspicious IP addresses (simulated)
def block_suspicious_ip(ip):
    # In a real IDS, this function would take action to block or quarantine the IP address.
    # For demonstration purposes, we'll simulate blocking by adding it to a list.
    blocked_ips.append(ip)
    blocked_ips_label.config(text=f"Blocked IPs: {', '.join(blocked_ips)}")
    messagebox.askokcancel("Blocked IP ",f"Your IP is blocked! \n Blocked IP:{ip}")
    
# Function to update system monitoring information
def update_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    system_info_label.config(text=f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_percent}%")
    root.after(1000, update_system_info)  # Update every 1 second

# Create the main window
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("500x300")

# Create and configure widgets
authorized_ips_label = tk.Label(root, text="Authorized IPs (comma-separated):",font=("Helvetica",12))
authorized_ips_entry = tk.Entry(root,font=("Helvetica",12))
ip_label = tk.Label(root, text="Enter IP Address:",font=("Helvetica",12))
ip_entry = tk.Entry(root,font=("Helvetica",12))
check_button = tk.Button(root, text="Check IP",font=("Helvetica",12), command=handle_ip)
result_label = tk.Label(root, text="", fg="black",font=("Helvetica",12))
system_info_label = tk.Label(root, text="", fg="blue",font=("Helvetica",12))

# Pack widgets
authorized_ips_label.pack()
authorized_ips_entry.pack()
ip_label.pack()
ip_entry.pack()
check_button.pack()
result_label.pack()
system_info_label.pack()

# Create a list to store blocked IPs (simulated)
blocked_ips = []

# Create a label to display blocked IPs (simulated)
blocked_ips_label = tk.Label(root, text="Blocked IPs:",font=("Helvetica",12))
blocked_ips_label.pack()

# Start the system monitoring in a separate thread
system_info_thread = threading.Thread(target=update_system_info)
system_info_thread.daemon = True
system_info_thread.start()
# Start the GUI main loop
root.mainloop()