from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox
import json
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

class AccountSwitcher:

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Mass Discord Joins")
        self.root.configure(background='black')

        # Variables
        self.invite_link = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.accounts = self.load_accounts()

        # Widgets
        self.init_ui()

    def init_ui(self):
        label = tk.Label(self.root, text="Built by LinuxPhantom", fg="white", bg="black", font=("Arial", 16))
        label.pack(pady=10)

        # Add accounts frame
        account_frame = tk.Frame(self.root, bg="black")
        account_frame.pack(pady=20, fill=tk.X, padx=50)

        email_label = tk.Label(account_frame, text="Email:", fg="white", bg="black")
        email_label.grid(row=0, column=0, padx=5)

        email_entry = tk.Entry(account_frame, textvariable=self.email, fg="white", bg="#333")
        email_entry.grid(row=0, column=1, padx=5, sticky=tk.W + tk.E)

        pass_label = tk.Label(account_frame, text="Password:", fg="white", bg="black")
        pass_label.grid(row=0, column=2, padx=5)

        pass_entry = tk.Entry(account_frame, textvariable=self.password, show="*", fg="white", bg="#333")
        pass_entry.grid(row=0, column=3, padx=5, sticky=tk.W + tk.E)

        add_btn = tk.Button(account_frame, text="Add Account", bg="#555", fg="white", command=self.add_account)
        add_btn.grid(row=0, column=4, padx=5)

        account_frame.columnconfigure(1, weight=1)
        account_frame.columnconfigure(3, weight=1)

        # Invite link input
        invite_label = tk.Label(self.root, text="Enter the Discord Invite:", fg="white", bg="black")
        invite_label.pack(pady=10)

        invite_entry = tk.Entry(self.root, textvariable=self.invite_link, width=50, fg="white", bg="#333")
        invite_entry.pack(pady=10, padx=50, fill=tk.X)

        submit_btn = tk.Button(self.root, text="Submit", bg="#555", fg="white", command=self.process_invite)
        submit_btn.pack(pady=20)

    def join_discord(self, account, invite):
        options = Options()
        options.add_argument("--incognito")

        # Path to your chromedriver executable (update this path)
        driver_path = 'path_to_your_chromedriver.exe'
        driver = webdriver.Chrome(options=options)

        driver.get("https://discord.com/login")
        wait = WebDriverWait(driver, 10)

        # Fill out email and password
        email_element = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        email_element.send_keys(account['email'])

        password_element = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        password_element.send_keys(account['password'])

        # Click login
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[div[contains(text(), 'Log In')]]")))
        login_button.click()

        # Giving it some time to login
        sleep(5) 

        # Navigate to the invite link
        driver.get(invite)
        sleep(3)  # Allow the page to load
        
        # Try clicking the "Continue to Discord" button
        try:
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue to Discord')]"))
            )
            continue_button.click()
            sleep(3)  # Allow some time for the join process
        except:
            print(f"Couldn't click the 'Continue to Discord' button for account {account['email']}.")


    def open_incognito(self, url):
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'  # Update this path if your Chrome is installed somewhere else
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new(url + ' --incognito')

    def process_invite(self):
        invite = self.invite_link.get().strip()

        if not invite:
            messagebox.showerror("Error", "Please enter an invite link.")
            return

        # Open the invite link in the incognito mode
        self.open_incognito(invite)

        for account in self.accounts:
            print(f"Attempting to join {invite} using {account['email']}")
            self.join_discord(account, invite)

        messagebox.showinfo("Info", f"Attempted to join with all accounts: {invite}")

    def save_accounts(self):
        with open('accounts.json', 'w') as f:
            json.dump(self.accounts, f)

    def load_accounts(self):
        try:
            with open('accounts.json', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_account(self):
        email = self.email.get().strip()
        password = self.password.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Please enter both email and password.")
            return

        self.accounts.append({'email': email, 'password': password})
        self.save_accounts()
        self.email.set("")
        self.password.set("")
        messagebox.showinfo("Added", "Account added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountSwitcher(root)
    root.mainloop()
