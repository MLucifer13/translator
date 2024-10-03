# Google Translate Assistant

Google Translate Assistant is a desktop application built using `tkinter` and `googletrans` to provide seamless translation capabilities for multiple languages. This lightweight tool offers a user-friendly interface and supports theme switching, making it ideal for quick and efficient translations.

## Features

- **Text Translation**: Translate text between any two languages supported by Google Translate.
- **Language Auto-detection**: Automatically detect the source language for easy translations.
- **Theme Switching**: Toggle between light and dark themes for a customized look.
- **Clipboard Support**: Copy the translated text directly to your clipboard with a single click.
- **Recent Translations**: View your recent translations for quick reference.

## Demo

![Google Translate Assistant Screenshot](screenshot.png)

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. The application uses the following libraries:

- `tkinter` (usually included with standard Python installations)
- `googletrans==4.0.0-rc1`
  
### Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/google-translate-assistant.git
    ```

2. Navigate to the project directory:

    ```bash
    cd google-translate-assistant
    ```

3. Install the required dependencies:

    ```bash
    pip install googletrans==4.0.0-rc1
    ```

4. Run the application:

    ```bash
    python translate_app.py
    ```

## Usage

1. Launch the application.
2. Enter the text you want to translate in the **Input Text** area.
3. Choose the source and target languages using the dropdown menus. By default, the source language is set to auto-detect, and the target language is set to Spanish.
4. Click **Translate** to view the translated text.
5. Use **Clear Text** to reset the input area, **Copy to Clipboard** to copy the translated text, and **Toggle Theme** to switch between light and dark modes.

## Code Overview

### Class: `TranslationApp`

This is the main class of the application, which handles the user interface and interaction logic. It extends `tk.Tk` and `ThemeMixin` to provide theming support.

- **Attributes**:
  - `__translator`: An instance of the `Translator` class for performing translations.
  - `__languages`: Dictionary mapping language codes to language names (from `googletrans`).
  - `translation_var`: A `StringVar` for storing and displaying the translated text dynamically.

- **Methods**:
  - `translate()`: Handles the translation process and updates the output label.
  - `toggle_theme()`: Switches between light and dark themes.
  - `clear_text()`: Clears the input text area.
  - `copy_to_clipboard()`: Copies the translated text to the clipboard.

### Decorators
- **`@log_action`**: Logs each action performed.
- **`@timing_decorator`**: Measures the time taken to perform an operation.
  
## Limitations

- **Translation Accuracy**: The accuracy of translations may vary depending on the language pair and complexity of the input text.
- **Internet Requirement**: The application requires an active internet connection to use the Google Translate API.
- **GoogleTrans Version Issues**: The current implementation uses `googletrans==4.0.0-rc1`. This library may experience issues due to API updates. Consider using a maintained alternative or updating the library if needed.

## Known Issues

- Some language codes might not be properly recognized depending on the `googletrans` version.
- Changing themes while translating might cause minor UI glitches in some environments.

