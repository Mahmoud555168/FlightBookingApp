import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Flight Booking App")
root.geometry("400x300")

# Welcome message
label = tk.Label(root, text="Welcome to Flight Booking App!", font=("Arial", 14))
label.pack(pady=20)

# Exit button
btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack()

root.mainloop()
import sqlite3

# Connect to database and create table
conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    departure TEXT NOT NULL,
    destination TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

conn.commit()
conn.close()
import sqlite3

# Connect to database and create table
conn = sqlite3.connect("flights.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    departure TEXT NOT NULL,
    destination TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

conn.commit()
conn.close()
import tkinter as tk
from tkinter import messagebox
import sqlite3

def book_flight():
    name = entry_name.get()
    flight_number = entry_flight.get()
    departure = entry_departure.get()
    destination = entry_destination.get()
    date = entry_date.get()

    if name and flight_number and departure and destination and date:
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (name, flight_number, departure, destination, date) VALUES (?, ?, ?, ?, ?)", 
                       (name, flight_number, departure, destination, date))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Booking added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields")

# Create main window
root = tk.Tk()
root.title("Flight Booking")

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Flight Number:").pack()
entry_flight = tk.Entry(root)
entry_flight.pack()

tk.Label(root, text="Departure:").pack()
entry_departure = tk.Entry(root)
entry_departure.pack()

tk.Label(root, text="Destination:").pack()
entry_destination = tk.Entry(root)
entry_destination.pack()

tk.Label(root, text="Date (YYYY-MM-DD):").pack()
entry_date = tk.Entry(root)
entry_date.pack()

# Book button
btn_book = tk.Button(root, text="Book Flight", command=book_flight)
btn_book.pack(pady=10)

# Exit button
btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack()

root.mainloop()
def view_bookings():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        bookings_window = tk.Toplevel(root)
        bookings_window.title("Bookings")

        for i, row in enumerate(rows):
            tk.Label(bookings_window, text=f"{row[1]} - {row[2]} ({row[3]} -> {row[4]}) on {row[5]}").pack()
    else:
        messagebox.showinfo("No Bookings", "No bookings found.")

# Add "View Bookings" button
btn_view = tk.Button(root, text="View Bookings", command=view_bookings)
btn_view.pack()
import tkinter as tk
from tkinter import messagebox
import sqlite3