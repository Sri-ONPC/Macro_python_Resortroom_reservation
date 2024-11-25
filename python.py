import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class ResortBookingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Resort Room Booking System")
        self.root.geometry("600x600")
        self.root.configure(bg="#e0f7fa")  # Light blue background

        # Room Prices
        self.room_prices = {
            "AC Room": 500,
            "Deluxe Room": 900,
            "Suite": 1500,
            "Beachfront Villa": 2000
        }
        self.bookings = []  # List to store booking history
        self.reviews = []  # List to store reviews

        # Admin login credentials
        self.admin_credentials = {"username": "admin", "password": "admin"}

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#00796b")
        header_frame.pack(fill=tk.X, pady=10)
        tk.Label(header_frame, text="Welcome to Paradise Resort", font=("Helvetica", 24), fg="white", bg="#00796b").pack(pady=10)

        # Customer Information Frame
        info_frame = tk.Frame(self.root, bg="#e0f7fa")
        info_frame.pack(pady=10)

        tk.Label(info_frame, text="Full Name:", bg="#e0f7fa").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(info_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Contact No:", bg="#e0f7fa").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.contact_entry = tk.Entry(info_frame, width=30)
        self.contact_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Special Requests:", bg="#e0f7fa").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.request_entry = tk.Entry(info_frame, width=30)
        self.request_entry.grid(row=2, column=1, padx=10, pady=5)

        # Room Type Selection
        tk.Label(info_frame, text="Room Type:", bg="#e0f7fa").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.room_var = tk.StringVar(value="Deluxe Room")
        self.room_menu = ttk.Combobox(info_frame, textvariable=self.room_var, values=list(self.room_prices.keys()), width=28)
        self.room_menu.grid(row=3, column=1, padx=10, pady=5)
        self.room_menu.bind("<<ComboboxSelected>>", self.update_price)

        # Room Price Display
        tk.Label(info_frame, text="Room Price ($):", bg="#e0f7fa").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.price_label = tk.Label(info_frame, text="0", bg="#e0f7fa")
        self.price_label.grid(row=4, column=1, padx=10, pady=5)

        # Date Selection
        tk.Label(info_frame, text="Check-in Date (YYYY-MM-DD):", bg="#e0f7fa").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.check_in_entry = tk.Entry(info_frame, width=30)
        self.check_in_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(info_frame, text="Check-out Date (YYYY-MM-DD):", bg="#e0f7fa").grid(row=6, column=0, padx=10, pady=5, sticky='e')
        self.check_out_entry = tk.Entry(info_frame, width=30)
        self.check_out_entry.grid(row=6, column=1, padx=10, pady=5)

        # Payment Method Selection
        tk.Label(info_frame, text="Payment Method:", bg="#e0f7fa").grid(row=7, column=0, padx=10, pady=5, sticky='e')
        self.payment_var = tk.StringVar(value="Credit Card")
        self.payment_menu = ttk.Combobox(info_frame, textvariable=self.payment_var, values=["Credit Card", "PayPal", "Cash"], width=28)
        self.payment_menu.grid(row=7, column=1, padx=10, pady=5)

        # Confirm Booking Button
        self.confirm_button = tk.Button(self.root, text="Confirm Booking", command=self.confirm_booking, bg="#00796b", fg="white", font=("Arial", 12))
        self.confirm_button.pack(pady=20)

        # Booking History Button
        self.history_button = tk.Button(self.root, text="Show Booking History", command=self.show_booking_history, bg="#4caf50", fg="white", font=("Arial", 12))
        self.history_button.pack(pady=10)

        # Leave a Review Button
        self.review_button = tk.Button(self.root, text="Leave a Review", command=self.leave_review, bg="#00796b", fg="white", font=("Arial", 12))
        self.review_button.pack(pady=10)

        # Admin Login Button
        self.admin_button = tk.Button(self.root, text="Admin Login", command=self.admin_login, bg="#f57c00", fg="white", font=("Arial", 12))
        self.admin_button.pack(pady=10)

    def update_price(self, event):
        room_type = self.room_var.get()
        price = self.room_prices[room_type]
        self.price_label.config(text=str(price))

    def confirm_booking(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        special_requests = self.request_entry.get()
        check_in = self.check_in_entry.get()
        check_out = self.check_out_entry.get()
        room_type = self.room_var.get()
        payment_method = self.payment_var.get()

        # Validate input
        if not name or not contact or not check_in or not check_out:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        # Validate date format
        try:
            check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
            check_out_date = datetime.strptime(check_out, '%Y-%m-%d')
            if check_in_date >= check_out_date:
                raise ValueError("Check-out date must be after check-in date.")
        except ValueError as e:
            messagebox.showwarning("Date Error", str(e))
            return

        price = self.room_prices[room_type]
        total_cost = price * ((check_out_date - check_in_date).days)

        response = messagebox.askyesno(
            "Confirm Booking",
            f"Name: {name}\nContact: {contact}\nRoom: {room_type}\nCheck-in: {check_in}\nCheck-out: {check_out}\nSpecial Requests: {special_requests}\nPayment Method: {payment_method}\nTotal Cost: ${total_cost:.2f}\n\nDo you want to proceed with the booking?"
        )

        if response:
            self.process_payment()
            booking_info = {
                "name": name,
                "contact": contact,
                "room_type": room_type,
                "check_in": check_in,
                "check_out": check_out,
                "special_requests": special_requests,
                "payment_method": payment_method,
                "total_cost": total_cost
            }
            self.bookings.append(booking_info)  # Save booking info
        else:
            messagebox.showinfo("Booking Cancelled", "Feel free to explore other options!")

    def process_payment(self):
        messagebox.showinfo("Payment Successful", "Your payment has been processed. Thank you for booking with us!")

    def show_booking_history(self):
        if not self.bookings:
            messagebox.showinfo("No Bookings", "No bookings made yet.")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("Booking History")
        history_window.geometry("400x400")
        history_window.configure(bg="#e0f7fa")

        history_text = tk.Text(history_window, bg="#ffffff", fg="#000000")
        history_text.pack(expand=True, fill='both')

        for booking in self.bookings:
            booking_info = (f"Name: {booking['name']}, Room: {booking['room_type']}, "
                            f"Check-in: {booking['check_in']}, Check-out: {booking['check_out']}, "
                            f"Payment Method: {booking['payment_method']}, "
                            f"Total Cost: ${booking['total_cost']:.2f}\n")
            history_text.insert(tk.END, booking_info + "\n")

    def leave_review(self):
        review_window = tk.Toplevel(self.root)
        review_window.title("Leave a Review")
        review_window.geometry("400x300")
        review_window.configure(bg="#e0f7fa")

        tk.Label(review_window, text="Write your review:", bg="#e0f7fa").pack(pady=10)

        self.review_text = tk.Text(review_window, height=5, width=40)
        self.review_text.pack(pady=10)

        def submit_review():
            review = self.review_text.get("1.0", tk.END).strip()
            if review:
                self.reviews.append(review)
                messagebox.showinfo("Review Submitted", "Thank you for your feedback!")
                review_window.destroy()
            else:
                messagebox.showwarning("Empty Review", "Please write a review before submitting.")

        submit_button = tk.Button(review_window, text="Submit Review", command=submit_review, bg="#00796b", fg="white", font=("Arial", 12))
        submit_button.pack(pady=10)

    def admin_login(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Admin Login")
        login_window.geometry("400x200")
        login_window.configure(bg="#e0f7fa")

        tk.Label(login_window, text="Username:", bg="#e0f7fa").pack(pady=10)
        username_entry = tk.Entry(login_window, width=30)
        username_entry.pack(pady=5)

        tk.Label(login_window, text="Password:", bg="#e0f7fa").pack(pady=10)
        password_entry = tk.Entry(login_window, width=30, show="*")
        password_entry.pack(pady=5)

        def verify_admin():
            username = username_entry.get()
            password = password_entry.get()

            if username == self.admin_credentials["username"] and password == self.admin_credentials["password"]:
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                login_window.destroy()
                self.show_admin_dashboard()
            else:
                messagebox.showwarning("Login Failed", "Invalid username or password.")

        login_button = tk.Button(login_window, text="Login", command=verify_admin, bg="#00796b", fg="white", font=("Arial", 12))
        login_button.pack(pady=10)

    def show_admin_dashboard(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Admin Dashboard")
        admin_window.geometry("600x400")
        admin_window.configure(bg="#e0f7fa")

        tk.Label(admin_window, text="Admin Dashboard", font=("Helvetica", 24), fg="white", bg="#00796b").pack(pady=20)

        # Show bookings and reviews
        bookings_button = tk.Button(admin_window, text="View All Bookings", command=self.show_all_bookings, bg="#00796b", fg="white", font=("Arial", 12))
        bookings_button.pack(pady=10)

        reviews_button = tk.Button(admin_window, text="View All Reviews", command=self.show_all_reviews, bg="#00796b", fg="white", font=("Arial", 12))
        reviews_button.pack(pady=10)

    def show_all_bookings(self):
        if not self.bookings:
            messagebox.showinfo("No Bookings", "No bookings made yet.")
            return

        all_bookings_window = tk.Toplevel(self.root)
        all_bookings_window.title("All Bookings")
        all_bookings_window.geometry("400x400")
        all_bookings_window.configure(bg="#e0f7fa")

        bookings_text = tk.Text(all_bookings_window, bg="#ffffff", fg="#000000")
        bookings_text.pack(expand=True, fill='both')

        for booking in self.bookings:
            booking_info = (f"Name: {booking['name']}, Room: {booking['room_type']}, "
                            f"Check-in: {booking['check_in']}, Check-out: {booking['check_out']}, "
                            f"Payment Method: {booking['payment_method']}, "
                            f"Total Cost: ${booking['total_cost']:.2f}\n")
            bookings_text.insert(tk.END, booking_info + "\n")

    def show_all_reviews(self):
        if not self.reviews:
            messagebox.showinfo("No Reviews", "No reviews have been submitted yet.")
            return

        all_reviews_window = tk.Toplevel(self.root)
        all_reviews_window.title("All Reviews")
        all_reviews_window.geometry("400x400")
        all_reviews_window.configure(bg="#e0f7fa")

        reviews_text = tk.Text(all_reviews_window, bg="#ffffff", fg="#000000")
        reviews_text.pack(expand=True, fill='both')

        for review in self.reviews:
            reviews_text.insert(tk.END, review + "\n\n")


if _name_ == "_main_":
    root = tk.Tk()
    app = ResortBookingApp(root)
    root.mainloop()