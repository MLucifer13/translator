# Google Translate Assistant

Google Translate Assistant is a desktop application built using `customtkinter`, `tkinter`, and `googletrans` to provide seamless translation capabilities for multiple languages. This lightweight tool offers a user-friendly interface and supports theme customization, making it ideal for quick and efficient translations.

## Features

- **Text Translation**: Translate text between any two languages supported by Google Translate.
- **Language Swap**: Easily swap source and target languages with a single click.
- **Custom Themes**: Supports both light and dark themes for a customized look.
- **User-friendly Interface**: Designed with a modern UI for enhanced usability using `customtkinter`.
- **Error Handling**: Proper error messages for issues such as missing input text or same source and target languages.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. The application uses the following libraries:

- `customtkinter`
- `googletrans==4.0.0-rc1`
- `Pillow`

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
    pip install customtkinter googletrans==4.0.0-rc1 pillow
    ```

4. Make sure you have the required icon files in the same directory as the main script:
    - `translator_icon_converted.png`
    - `translator_icon_converted.ico` (for Windows users)
    - `swap_icon_converted.png`

5. Run the application:

    ```bash
    python translate_app.py
    ```

## Usage

1. Launch the application.
2. Enter the text you want to translate in the **Input Text** area.
3. Choose the source and target languages using the dropdown menus. By default, the source language is set to English, and the target language is set to French.
4. Click **Translate** to view the translated text.
5. Use the **Swap Languages** button to quickly swap the source and target languages.
6. The **Clear Text** button resets the input area, while the **Copy to Clipboard** feature is available to easily copy the translated text for use elsewhere.

## Code Overview

### Class: `TranslationApp`

This is the main class of the application, which combines translation functionality with the graphical interface.

- **Attributes**:
  - `__translator`: An instance of the `Translator` class from `googletrans` for performing translations.
  - `src_lang_var` and `tgt_lang_var`: Variables to track the selected source and target languages.
  - `src_text` and `tgt_text`: Widgets for the input and output text areas.
  
- **Methods**:
  - `perform_translation()`: Handles the translation process, error checking, and updating the output text.
  - `swap_languages()`: Swaps the selected source and target languages for a quick reverse translation.
  - `clear_text()`: Clears the input text area.
  - `display_translation()`: Displays the translated text in the output area.
  
### Class: `BaseGUI`

This class handles the graphical user interface (GUI) setup, such as creating menus, frames, and widgets. It also implements the theme switching and splash screen functionalities.

- **Attributes**:
  - `menu_bar`: A menu bar with options to exit and view the "About" section.
  - `swap_button`: A button to swap the source and target languages.
  - `theme_button`: A future feature for toggling between light and dark themes.
  
- **Methods**:
  - `_create_widgets()`: Builds and arranges all the widgets, such as labels, text boxes, dropdown menus, and buttons.
  - `_show_about_info()`: Displays application information.

### Decorators
- **`@log_method_call`**: Logs each action performed to help track function calls during execution.

## Limitations

- **Translation Accuracy**: The accuracy of translations depends on Google Translate’s API and the complexity of the input text.
- **Internet Requirement**: The application requires an active internet connection to use the Google Translate API.
- **GoogleTrans Version Issues**: The current implementation uses `googletrans==4.0.0-rc1`. This version might experience issues if Google’s API is updated. Consider checking for updates or alternatives if needed.

## Known Issues

- Language codes might not always be correctly mapped depending on the version of `googletrans`.
- The application might experience minor UI glitches when themes are toggled during translations.
