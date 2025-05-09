import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🎂 Age Calculator")
        self.root.geometry("480x550")
        self.root.resizable(False, False)
        
        # Color scheme
        self.bg_color = "#2E3440"  # Dark blue-gray
        self.header_color = "#88C0D0"  # Light blue
        self.button_color = "#5E81AC"  # Medium blue
        self.button_hover = "#81A1C1"  # Lighter blue
        self.result_bg = "#3B4252"  # Darker blue-gray
        self.text_color = "#E5E9F0"  # Light gray
        self.accent_color = "#A3BE8C"  # Soft green
        self.warning_color = "#BF616A"  # Soft red
        
        # Configure root window background
        self.root.configure(bg=self.bg_color)
        
        # Configure the grid
        self.root.columnconfigure(0, weight=1)
        
        # Custom style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('TLabel', 
                           background=self.bg_color, 
                           foreground=self.text_color,
                           font=('Arial', 11))
        
        self.style.configure('Header.TLabel', 
                           font=('Arial', 18, 'bold'),
                           foreground=self.header_color)
        
        self.style.configure('TButton', 
                           font=('Arial', 12, 'bold'),
                           background=self.button_color,
                           foreground=self.text_color,
                           borderwidth=1)
        
        self.style.map('TButton',
                     background=[('active', self.button_hover)],
                     foreground=[('active', self.text_color)])
        
        self.style.configure('TEntry', 
                           font=('Arial', 11),
                           fieldbackground="#4C566A",
                           foreground=self.text_color,
                           insertcolor=self.text_color)
        
        self.style.configure('TFrame', 
                           background=self.bg_color)
        
        self.style.configure('TLabelframe', 
                           background=self.result_bg,
                           foreground=self.accent_color)
        
        self.style.configure('TLabelframe.Label', 
                           background=self.result_bg,
                           foreground=self.accent_color,
                           font=('Arial', 12, 'bold'))
        
        self.style.configure('Result.TLabel', 
                           font=('Arial', 14),
                           background=self.result_bg,
                           foreground=self.text_color)
        
        self.style.configure('Highlight.TLabel', 
                           font=('Arial', 14, 'bold'),
                           background=self.result_bg,
                           foreground=self.accent_color)
        
        self.style.configure('Footer.TLabel', 
                           font=('Arial', 8),
                           background=self.bg_color,
                           foreground="#D8DEE9")
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = ttk.Label(self.root, 
                          text="AGE CALCULATOR", 
                          style='Header.TLabel')
        header.grid(row=0, column=0, pady=(20, 15), sticky='n')
        
        # Date of birth frame
        dob_frame = ttk.Frame(self.root)
        dob_frame.grid(row=1, column=0, pady=10, padx=20, sticky='ew')
        
        ttk.Label(dob_frame, 
                 text="Enter your date of birth:").pack(anchor='w')
        
        # Date entry
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var = tk.StringVar()
        
        entry_frame = ttk.Frame(dob_frame)
        entry_frame.pack(pady=15, fill='x')
        
        # Day entry
        ttk.Label(entry_frame, text="Day (DD):").grid(row=0, column=0, padx=(0, 5))
        self.day_entry = ttk.Entry(entry_frame, 
                                  textvariable=self.day_var, 
                                  width=5)
        self.day_entry.grid(row=0, column=1, padx=5)
        
        # Month entry
        ttk.Label(entry_frame, text="Month (MM):").grid(row=0, column=2, padx=(15, 5))
        self.month_entry = ttk.Entry(entry_frame, 
                                    textvariable=self.month_var, 
                                    width=5)
        self.month_entry.grid(row=0, column=3, padx=5)
        
        # Year entry
        ttk.Label(entry_frame, text="Year (YYYY):").grid(row=0, column=4, padx=(15, 5))
        self.year_entry = ttk.Entry(entry_frame, 
                                   textvariable=self.year_var, 
                                   width=7)
        self.year_entry.grid(row=0, column=5, padx=5)
        
        # Calculate button
        calc_btn = ttk.Button(self.root, 
                             text="CALCULATE AGE", 
                             command=self.calculate_age)
        calc_btn.grid(row=2, column=0, pady=15, ipadx=30, ipady=8)
        
        # Results frame
        self.result_frame = ttk.LabelFrame(self.root, 
                                         text="  YOUR AGE  ",
                                         padding=(20, 15))
        self.result_frame.grid(row=3, column=0, pady=(0, 20), padx=20, sticky='nsew')
        
        # Configure grid weights for the result frame
        self.result_frame.columnconfigure(0, weight=1)
        
        # Default result labels (empty)
        self.years_label = ttk.Label(self.result_frame, 
                                    text="", 
                                    style='Result.TLabel')
        self.years_label.grid(row=0, column=0, pady=5, sticky='w')
        
        self.months_label = ttk.Label(self.result_frame, 
                                     text="", 
                                     style='Result.TLabel')
        self.months_label.grid(row=1, column=0, pady=5, sticky='w')
        
        self.days_label = ttk.Label(self.result_frame, 
                                   text="", 
                                   style='Result.TLabel')
        self.days_label.grid(row=2, column=0, pady=5, sticky='w')
        
        # Separator
        ttk.Separator(self.result_frame, orient='horizontal').grid(row=3, column=0, pady=10, sticky='ew')
        
        self.next_bday_label = ttk.Label(self.result_frame, 
                                        text="", 
                                        style='Highlight.TLabel')
        self.next_bday_label.grid(row=4, column=0, pady=(5, 15), sticky='w')
        
        # Additional info
        self.additional_info = ttk.Label(self.result_frame, 
                                       text="", 
                                       wraplength=350,
                                       style='Result.TLabel')
        self.additional_info.grid(row=5, column=0, pady=(10, 5), sticky='w')
        
        # Footer
        footer = ttk.Label(self.root, 
                          text="Made with Python & Tkinter • © 2023", 
                          style='Footer.TLabel')
        footer.grid(row=4, column=0, pady=(0, 10), sticky='s')
        
        # Bind Enter key to calculate
        self.root.bind('<Return>', lambda event: self.calculate_age())
        
        # Set focus to day entry
        self.day_entry.focus()
        
    def calculate_age(self):
        try:
            day = int(self.day_var.get())
            month = int(self.month_var.get())
            year = int(self.year_var.get())
            
            birth_date = datetime.date(year, month, day)
            today = datetime.date.today()
            
            if birth_date > today:
                messagebox.showerror("Error", "Birth date cannot be in the future!")
                return
                
            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day
            
            # Adjust for negative months or days
            if days < 0:
                months -= 1
                # Get the last day of the previous month
                previous_month = today.replace(day=1) - datetime.timedelta(days=1)
                days += previous_month.day
            
            if months < 0:
                years -= 1
                months += 12
                
            # Update result labels with colorful emojis
            self.years_label.config(text=f"📅 Years: {years}")
            self.months_label.config(text=f"🗓️ Months: {months}")
            self.days_label.config(text=f"📆 Days: {days}")
            
            # Calculate next birthday
            next_birthday = datetime.date(today.year, month, day)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            
            days_until_birthday = (next_birthday - today).days
            self.next_bday_label.config(text=f"🎂 Next birthday in: {days_until_birthday} days")
            
            # Additional info with colorful icons
            total_days = (today - birth_date).days
            total_months = years * 12 + months
            total_weeks = total_days // 7
            
            if years >= 18:
                age_category = f"👔 Adult (since {years - 18} years)"
            elif years >= 13:
                age_category = f"🎒 Teenager ({years - 13} years as teen)"
            else:
                age_category = "🧒 Child"
            
            info_text = (
                f"📊 You are {total_months:,} months old\n"
                f"⏳ {total_days:,} days | {total_weeks:,} weeks lived\n"
                f"{age_category}"
            )
            self.additional_info.config(text=info_text)
            
        except ValueError as e:
            messagebox.showerror("Error", 
                               "Invalid date format!\nPlease enter:\n"
                               "• Day as 1-31\n"
                               "• Month as 1-12\n"
                               "• Year as 1900-2023",
                               icon='warning')
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculator(root)
    app.run()