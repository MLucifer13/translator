import customtkinter as ct
from tkinter import messagebox, Menu
from googletrans import Translator, LANGUAGES
from PIL import Image
import sys
import os

# Set appearance and color theme before creating any widgets
ct.set_appearance_mode("Light")  # Changed from "Dark" to "Light"
ct.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Custom decorator to log method calls
def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Method '{func.__name__}' called")
        return func(*args, **kwargs)
    return wrapper

# Base class for Translation Functionality
class TranslationModel:
    def __init__(self):
        self.__translator = Translator()

    @log_method_call
    def translate_text(self, text, src_lang, tgt_lang):
        try:
            translated = self.__translator.translate(text, src=src_lang, dest=tgt_lang)
            return translated.text
        except Exception as e:
            raise ValueError("Translation failed. Please check your internet connection and try again.") from e

# Base class for GUI
class BaseGUI(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Translator")
        self.geometry("900x750")
        self.resizable(False, False)
        self.translator_icon_path = "translator_icon_converted.png"
        self.swap_icon_path = "swap_icon_converted.png"
        self._set_window_icon()
        self._create_menu_bar()
        self._create_widgets()

    def _set_window_icon(self):
        if os.path.exists(self.translator_icon_path):
            try:
                if sys.platform.startswith('win'):
                    icon_path = "translator_icon_converted.ico"
                    if os.path.exists(icon_path):
                        self.iconbitmap(icon_path)
                    else:
                        print(f"Icon file '{icon_path}' not found. Please ensure it exists.")
                else:
                    icon_image = ct.CTkImage(light_image=Image.open(self.translator_icon_path))
                    self.iconphoto(True, icon_image._PhotoImage)
            except Exception as e:
                print(f"Unable to set window icon: {e}")
        else:
            print(f"Icon file '{self.translator_icon_path}' not found. Please ensure it exists.")

    def _create_menu_bar(self):
        self.menu_bar = Menu(self)
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about_info)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        self.config(menu=self.menu_bar)

    def _show_about_info(self):
        messagebox.showinfo("About Translator", "Translator App\nVersion 1.0\nPowered by customtkinter and Google Translate")

    def _create_widgets(self):
        pass

    def display_translation(self, translated_text):
        pass

    def show_splash_screen(self):
        splash = ct.CTkToplevel()
        splash.overrideredirect(True)
        splash.geometry("400x300+{}+{}".format(
            int(self.winfo_screenwidth() / 2 - 200),
            int(self.winfo_screenheight() / 2 - 150)
        ))
        splash_label = ct.CTkLabel(
            splash,
            text="Welcome to Translator",
            font=ct.CTkFont(family="Helvetica Neue", size=24, weight="bold")
        )
        splash_label.pack(expand=True)
        self.after(2000, splash.destroy)

# Multiple inheritance
class TranslationApp(BaseGUI, TranslationModel):
    def __init__(self):
        TranslationModel.__init__(self)
        BaseGUI.__init__(self)
        self.show_splash_screen()

    def _create_widgets(self):
        # Main Frame
        self.main_frame = ct.CTkFrame(self)
        self.main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Title Label with Icon
        title_frame = ct.CTkFrame(self.main_frame, fg_color="transparent")
        title_frame.pack(pady=20)

        # Title Icon
        title_icon = None
        if os.path.exists(self.translator_icon_path):
            title_icon = ct.CTkImage(light_image=Image.open(self.translator_icon_path), size=(50, 50))

        self.title_label = ct.CTkLabel(
            title_frame,
            text=" Translator",
            image=title_icon,
            compound="left",
            font=ct.CTkFont(family="Helvetica Neue", size=32, weight="bold")
        )
        self.title_label.pack()

        # Language Selection Frame
        lang_frame = ct.CTkFrame(self.main_frame)
        lang_frame.pack(pady=10)

        # Source Language Dropdown
        self.src_lang_var = ct.StringVar(value='English')
        self.src_lang_label = ct.CTkLabel(lang_frame, text="Translate from:", font=ct.CTkFont(size=14))
        self.src_lang_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.src_lang_menu = ct.CTkOptionMenu(
            lang_frame,
            variable=self.src_lang_var,
            values=self.get_language_names(),
            width=220,
            height=40,
            font=ct.CTkFont(size=12),
            corner_radius=20
        )
        self.src_lang_menu.grid(row=0, column=1, padx=10, pady=5)

        # Swap Languages Button
        swap_icon = None
        if os.path.exists(self.swap_icon_path):
            swap_icon = ct.CTkImage(light_image=Image.open(self.swap_icon_path), size=(30, 30))
        self.swap_button = ct.CTkButton(
            lang_frame,
            text="",
            image=swap_icon,
            width=40,
            height=40,
            command=self.swap_languages,
            fg_color="transparent",
            hover_color="#e0e0e0",  # Adjusted for light mode
            corner_radius=20
        )
        self.swap_button.grid(row=0, column=2, padx=10, pady=5)

        # Target Language Dropdown
        self.tgt_lang_var = ct.StringVar(value='French')
        self.tgt_lang_label = ct.CTkLabel(lang_frame, text="Translate to:", font=ct.CTkFont(size=14))
        self.tgt_lang_label.grid(row=0, column=3, padx=5, pady=5, sticky='e')
        self.tgt_lang_menu = ct.CTkOptionMenu(
            lang_frame,
            variable=self.tgt_lang_var,
            values=self.get_language_names(),
            width=220,
            height=40,
            font=ct.CTkFont(size=12),
            corner_radius=20
        )
        self.tgt_lang_menu.grid(row=0, column=4, padx=10, pady=5)

        # Source Text Entry with Placeholder
        self.src_text = ct.CTkTextbox(
            self.main_frame,
            width=800,
            height=200,
            font=ct.CTkFont(size=16),
            corner_radius=15
        )
        self.src_text.pack(pady=10)
        self.src_text_placeholder = "Enter text to translate..."
        self._add_placeholder(self.src_text, self.src_text_placeholder)
        self.src_text.bind("<FocusIn>", lambda event: self._clear_placeholder(self.src_text, self.src_text_placeholder))
        self.src_text.bind("<FocusOut>", lambda event: self._add_placeholder(self.src_text, self.src_text_placeholder))

        # Translate Button with Hover Effect
        self.translate_button = ct.CTkButton(
            self.main_frame,
            text="Translate",
            command=self.perform_translation,
            width=320,
            height=60,
            font=ct.CTkFont(size=20, weight="bold"),
            corner_radius=30,
            fg_color="#1f6aa5",
            hover_color="#3a8bd9"
        )
        self.translate_button.pack(pady=20)

        # Target Text Display with Placeholder
        self.tgt_text = ct.CTkTextbox(
            self.main_frame,
            width=800,
            height=200,
            font=ct.CTkFont(size=16),
            corner_radius=15
        )
        self.tgt_text.pack(pady=10)
        self.tgt_text_placeholder = "Translation will appear here..."
        self._add_placeholder(self.tgt_text, self.tgt_text_placeholder, disable=True)
        self.tgt_text.bind("<FocusIn>", lambda event: self._clear_placeholder(self.tgt_text, self.tgt_text_placeholder, disable=True))
        self.tgt_text.bind("<FocusOut>", lambda event: self._add_placeholder(self.tgt_text, self.tgt_text_placeholder, disable=True))

    # Helper method to get language names from googletrans
    def get_language_names(self):
        languages = LANGUAGES
        names = [name.title() for name in languages.values()]
        return sorted(names)

    # Helper method to get language code from language name
    def get_language_code(self, language_name):
        language_name = language_name.lower()
        for code, name in LANGUAGES.items():
            if name.lower() == language_name:
                return code
        return 'en'  # Default to English if not found

    # Swap source and target languages
    def swap_languages(self):
        src_lang = self.src_lang_var.get()
        tgt_lang = self.tgt_lang_var.get()
        self.src_lang_var.set(tgt_lang)
        self.tgt_lang_var.set(src_lang)

    # Placeholder handling methods
    def _add_placeholder(self, text_widget, placeholder, disable=False):
        text_widget.configure(state='normal')
        text_widget.delete('1.0', ct.END)
        text_widget.insert('1.0', placeholder)
        text_widget.configure(text_color='grey')
        if disable:
            text_widget.configure(state='disabled')

    def _clear_placeholder(self, text_widget, placeholder, disable=False):
        current_text = text_widget.get("1.0", "end-1c")
        if current_text == placeholder:
            text_widget.delete('1.0', ct.END)
            text_widget.configure(text_color='black')
        if disable:
            text_widget.configure(state='normal')

    @log_method_call
    def display_translation(self, translated_text):
        self.tgt_text.configure(state='normal')
        self.tgt_text.delete('1.0', ct.END)
        self.tgt_text.insert(ct.END, translated_text)
        self.tgt_text.configure(text_color='black')
        self.tgt_text.configure(state='disabled')

    def perform_translation(self):
        text = self.src_text.get("1.0", "end-1c").strip()
        if text and text != self.src_text_placeholder:
            src_lang_code = self.get_language_code(self.src_lang_var.get())
            tgt_lang_code = self.get_language_code(self.tgt_lang_var.get())
            if src_lang_code == tgt_lang_code:
                messagebox.showerror("Language Selection Error", "Source and target languages must be different.")
                return
            try:
                translated_text = self.translate_text(text, src_lang_code, tgt_lang_code)
                self.display_translation(translated_text)
            except ValueError as e:
                messagebox.showerror("Translation Error", str(e))
            except Exception as e:
                messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please enter text to translate.")

# Run the application
if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
