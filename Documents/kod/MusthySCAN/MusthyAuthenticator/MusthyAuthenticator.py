import customtkinter as ctk
import json
import os
import time
import pyotp
import qrcode
from PIL import Image
import io

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MusthyAuthenticator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MusthyAuthenticator")
        self.geometry("400x600")
        self.accounts_file = "accounts.json"
        self.accounts = self.load_accounts()
        self.init_ui()
        self.update_codes()
        self.start_timer()

    def init_ui(self):
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=380, height=500)
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.account_frames = []

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, padx=20, fill="x")

        self.add_button = ctk.CTkButton(button_frame, text="Add Account", command=self.add_account)
        self.add_button.pack(side="left", padx=10)

        self.remove_button = ctk.CTkButton(button_frame, text="Remove Account", fg_color="red", command=self.remove_account)
        self.remove_button.pack(side="right", padx=10)

    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            with open(self.accounts_file, 'r') as f:
                return json.load(f)
        return []

    def save_accounts(self):
        with open(self.accounts_file, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def add_account(self):
        dialog = ctk.CTkInputDialog(text="Enter Account Name:", title="Add Account")
        name = dialog.get_input()
        if name:
            dialog2 = ctk.CTkInputDialog(text="Enter Secret Key:", title="Add Account")
            secret = dialog2.get_input()
            if secret:
                try:
                    totp = pyotp.TOTP(secret)
                    totp.now()
                    self.accounts.append({"name": name, "secret": secret})
                    self.save_accounts()
                    self.update_codes()
                except Exception as e:
                    # CustomTkinter'de messagebox
                    error_dialog = ctk.CTkMessagebox(title="Error", message=f"Invalid secret key: {str(e)}")
                    error_dialog.get()

    def remove_account(self):
        # For simplicity, use input for index
        dialog = ctk.CTkInputDialog(text="Enter account index to remove (0-based):", title="Remove Account")
        index_str = dialog.get_input()
        if index_str:
            try:
                index = int(index_str)
                if 0 <= index < len(self.accounts):
                    del self.accounts[index]
                    self.save_accounts()
                    self.update_codes()
                else:
                    error_dialog = ctk.CTkMessagebox(title="Error", message="Invalid index")
                    error_dialog.get()
            except ValueError:
                error_dialog = ctk.CTkMessagebox(title="Error", message="Invalid number")
                error_dialog.get()

    def delete_account(self, index):
        del self.accounts[index]
        self.save_accounts()
        self.update_codes()

    def update_codes(self):
        # Clear previous frames
        for frame in self.account_frames:
            frame.destroy()
        self.account_frames = []

        for i, account in enumerate(self.accounts):
            totp = pyotp.TOTP(account["secret"])
            code = totp.now()
            remaining = 30 - (int(time.time()) % 30)
            frame = ctk.CTkFrame(self.scrollable_frame)
            frame.pack(pady=5, padx=10, fill="x")
            
            label = ctk.CTkLabel(frame, text=f"{account['name']}: {code}", font=("Courier", 16, "bold"))
            label.pack(side="left", padx=10)
            
            time_label = ctk.CTkLabel(frame, text=f"{remaining}s", font=("Courier", 12))
            if remaining <= 5:
                time_label.configure(text_color="red")
            else:
                time_label.configure(text_color="green")
            time_label.pack(side="right", padx=10)
            
            delete_button = ctk.CTkButton(frame, text="Sil", width=50, fg_color="red", command=lambda idx=i: self.delete_account(idx))
            delete_button.pack(side="right", padx=5)
            
            self.account_frames.append(frame)

    def start_timer(self):
        self.after(1000, self.update_codes_loop)

    def update_codes_loop(self):
        self.update_codes()
        self.after(1000, self.update_codes_loop)

if __name__ == "__main__":
    app = MusthyAuthenticator()
    app.mainloop()