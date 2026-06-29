import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class RestaurantOrderApp:
    def __init__(self, root):
        self.root = root
        root.title("Restaurant Order App")

        # Menu items
        self.menu = {
            "FRIES MEAL": 2, #usd
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        # 1 usd = 280.22
        self.exchange_rate = 280  # USD → PKR
        self.pkrSymbol = "Rs"
        self.usdSymbol = "$"

        self.setup_background()
        self.build_ui()

    # ===== UI SETUP =====
    def build_ui(self):
        frame = ttk.Frame(self.root)
        # 0 
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management",
                  font=("Arial", 18, "bold")).grid(row=0, columnspan=3, pady=10)

        self.qty_boxes = {}
        self.labels = {}

        # Menu rows
        # enumerate([("Burger", 5), ("Pizza", 8)], start=1)
        # i=1, item="Burger", price=5

        # 1: (Fries, 2)
        # 2: (Burger, 3)
        # FRIES MEAL ($2)
        # 1: (item, price) = ( "FRIES", 2 )

        for i, (item, price) in enumerate(self.menu.items(), start=1):
            lbl = ttk.Label(frame, text=f"{item} (${price}):")
            lbl.grid(row=i, column=0, padx=10, pady=5)

            # [("FRIES", <label object>), ("BURGER", <label object>)]
            # [(FRies : <label>)]
            self.labels[item] = lbl

            entry = ttk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10)

            # [("FRIES", <entry object>), ("BURGER", <entry object>)]
            self.qty_boxes[item] = entry

        print("self.qty_boxes", self.qty_boxes.items())
        print("self.labels", self.labels.items())
        print(lbl.grid_size())

        # Currency dropdown row = 7
        ttk.Label(frame, text="Currency:").grid(row=len(self.menu) + 1, column=0)

        # current selected currency
        self.currency = tk.StringVar(value="USD") #USD

        dropdown = ttk.Combobox(frame, textvariable=self.currency,
                                values=["USD", "PKR"], width=10, state="readonly")
        dropdown.grid(row=len(self.menu) + 1, column=1, padx=10, pady=5)

        # attaching method to dropdwon
        # .bind 
        # binding an event with combobox
        dropdown.bind("<<ComboboxSelected>>", self.update_prices)

        # Order button
        ttk.Button(frame, text="Place Order",
                   command=self.place_order).grid(row=len(self.menu) + 2,
                                                  columnspan=3, pady=15)
        
        print(frame.grid_size())

    # ===== BACKGROUND IMAGE =====
    def setup_background(self):
        img = Image.open("background.jpg")
        img = img.resize((800, 600))
        self.bg = ImageTk.PhotoImage(img)

        # canvas is used to place images or shapes on window
        canvas = tk.Canvas(self.root, width=800, height=600)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg)

    # ===== UPDATE PRICES WHEN CURRENCY CHANGES =====
    def update_prices(self, event=None):
        # USD
        currency = self.currency.get()

          # $ "USD" "Rs"
        currencySymbol = self.usdSymbol if currency == "USD" else self.pkrSymbol
        rate = 1 if currency == "USD" else self.exchange_rate

        # Fries meal, <label>
        for item, lbl in self.labels.items(): 

            # menu["FRIES MEAL"] : 2 * 280 = 5
            lbl.config(text=f"{item} ({currencySymbol}{self.menu[item] * rate}):")

    # ===== PLACE ORDER =====
    def place_order(self):
        currency = self.currency.get() #USD
        currencySymbol = "$" if currency == "USD" else "Rs"
        rate = 1 if currency == "USD" else self.exchange_rate

        total = 0
        summary = "Order Summary:\n"

        # (FRies, <entry>)
        # $2, $1
        for item, entry in self.qty_boxes.items():
            qty = entry.get()
            if qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                price = self.menu[item] * rate
                cost = qty * price
                total += cost
                summary += f"{item}: {qty} × {currencySymbol}{price} = {currencySymbol}{cost}\n"

        if total == 0:
            messagebox.showerror("Error", "Please order at least one item.")
        else:
            summary += f"\nTotal Cost: {currencySymbol}{total}"
            messagebox.showinfo("Order Placed", summary)


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = RestaurantOrderApp(root)
    root.mainloop()
