import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Decorator for logging actions
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Action logged: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Decorator for timing
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
        return result
    return wrapper

# Mixin for theme functionality
class ThemeMixin:
    def set_theme(self, theme):
        """Set the theme based on user selection."""
        if theme == "dark":
            self.config(bg="#2c2c2c")
            self.style.configure("TButton", background="#444", foreground="white")
            self.style.configure("TLabel", background="#2c2c2c", foreground="white")
            self.style.configure("TCombobox", fieldbackground="#444", foreground="white")
        else:
            self.config(bg="white")
            self.style.configure("TButton", background="#dcdcdc", foreground="black")
            self.style.configure("TLabel", background="white", foreground="black")
            self.style.configure("TCombobox", fieldbackground="white", foreground="black")

class TranslationApp(tk.Tk, ThemeMixin):
    def __init__(self):
        super().__init__()
        self.title("Google Translate Assistant")
        self.geometry("700x500")
        self.style = ttk.Style()
        self.set_theme("light")
        
        self.__translator = Translator()  # Encapsulation: private attribute
        self.__languages = LANGUAGES  # Use the LANGUAGES dictionary from googletrans
        self.__reverse_languages = {v: k for k, v in self.__languages.items()}  # Create reverse lookup dictionary

        self.recent_translations = []  # Store recent translations
        self.translation_var = tk.StringVar()  # For dynamically updating the translated text

        # Use a modern theme for a better look
        self.style.theme_use("clam")
        
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header = ttk.Label(self, text="Google Translate Assistant", font=("Helvetica", 20, "bold"), padding=10)
        header.pack(pady=10)

        # Input Frame
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.input_text = tk.Text(self.input_frame, height=5, width=60, font=("Helvetica", 12))
        self.input_text.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.scrollbar = ttk.Scrollbar(self.input_frame, orient=tk.VERTICAL, command=self.input_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.input_text.config(yscrollcommand=self.scrollbar.set)

        # Language Selection Frame
        self.lang_frame = ttk.Frame(self)
        self.lang_frame.pack(padx=10, pady=5)

        language_list = list(self.__languages.values())
        self.source_lang = ttk.Combobox(self.lang_frame, values=['auto'] + language_list, width=25, font=("Helvetica", 10))
        self.source_lang.set("auto")
        self.source_lang.pack(side=tk.LEFT, padx=5)

        arrow_label = ttk.Label(self.lang_frame, text="→", font=("Helvetica", 12, "bold"))
        arrow_label.pack(side=tk.LEFT, padx=5)

        self.target_lang = ttk.Combobox(self.lang_frame, values=language_list, width=25, font=("Helvetica", 10))
        self.target_lang.set("Spanish")
        self.target_lang.pack(side=tk.LEFT, padx=5)

        # Button Frame
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)

        self.translate_button = ttk.Button(self.button_frame, text="Translate", command=self.translate)
        self.translate_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = ttk.Button(self.button_frame, text="Clear Text", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.copy_button = ttk.Button(self.button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.LEFT, padx=10)

        self.theme_button = ttk.Button(self.button_frame, text="Toggle Theme", command=self.toggle_theme)
        self.theme_button.pack(side=tk.LEFT, padx=10)

        # Output Frame
        self.output_frame = ttk.LabelFrame(self, text="Translated Text", padding=10)
        self.output_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.output_label = ttk.Label(self.output_frame, textvariable=self.translation_var, wraplength=650, relief=tk.SUNKEN, padding=10, font=("Helvetica", 12))
        self.output_label.pack(fill=tk.BOTH, expand=True)

    @log_action
    @timing_decorator
    def translate(self):
        """Perform the translation using googletrans."""
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text to translate!")
            return

        source = self.source_lang.get().lower()
        target = self.target_lang.get().lower()

        try:
            # Get language codes using the reverse lookup dictionary
            source_code = 'auto' if source == 'auto' else self.__reverse_languages[source]
            target_code = self.__reverse_languages[target]

            # Perform translation
            result = self.__translator.translate(text, src=source_code, dest=target_code)
            translated = f"Translated from {self.__languages[result.src]} to {self.__languages[result.dest]}:\n{result.text}"
            self.translation_var.set(translated)

        except Exception as e:
            self.translation_var.set(f"Translation error: {str(e)}")

    def toggle_theme(self):
        current_bg = self.cget("bg")
        new_theme = "dark" if current_bg == "white" else "light"
        self.set_theme(new_theme)

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.translation_var.set("")

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.translation_var.get())
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
