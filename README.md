# Python Keystroke Injector

This Python script is a keystroke injector that reads text from a file and simulates typing it into an active window on your computer. It's designed to mimic the typing speed and rhythm of a human, complete with randomized pauses between keystrokes.


## Potential Applications

1. **Demonstrations and Tutorials:** This script can be useful for creating demonstrations or tutorials where you want to show the process of writing code or text.
2. **Testing:** It can be used in software testing, particularly for applications that involve text input.
3. **Automating Repetitive Tasks:** If you have a task that involves repetitive text input, this script can automate it.
4. **Typing Practice:** With some modifications, this script can be used as a typing tutor, helping users to learn and practice typing skills.


## Installation

Please note that the script uses the pyautogui library to simulate keystrokes. You'll need to install this library before running the script. 

```pip install pyautogui```

## Usage

This script reads from a text file named ```keystrokes.txt```, so ensure this file exists and contains the text you want to type.

1. Open your console.
2. Navigate to the folder where the script is located using the cd command.
3. To run this script, type: ```python keystroke_injector.py```

Remember to switch to the window where you want the text to be typed within 5 seconds of running the script, as it includes a delay to allow you to do so.


# Key Features

1. **Delay before Starting:** The script includes a 5-second delay at the start, allowing you to switch to the appropriate window before the simulated typing begins.
2. **Simulated Human Typing:** The script simulates typing with randomized delays between keystrokes, providing a realistic typing effect.
3. **Prevention of Auto-Complete:** To ensure the integrity of the text being typed and prevent interference from text editor or IDE auto-complete features, the script includes an additional 'Enter' press for the first 5 lines.


# Disclaimer

This tool is intended for legitimate and responsible use. It should not be used for intrusive or malicious purposes. Please respect the privacy and rights of others while using this tool.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

<a href="https://www.buymeacoffee.com/ascensao1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>


