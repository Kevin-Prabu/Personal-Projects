import keyboard
import webbrowser

print("Code has Started")
keyboard.add_hotkey('0',lambda: webbrowser.open("https://google.com"))
keyboard.add_hotkey('1',lambda: webbrowser.open("https://www.youtube.com"))
keyboard.add_hotkey('2',lambda: webbrowser.open("https://www.instagram.com/"))
keyboard.add_hotkey('3',lambda: webbrowser.open("https://www.torn.com/index.php"))
keyboard.add_hotkey('4',lambda: webbrowser.open("https://www.conflictnations.com/play.php?bust=1&gameID=-1"))
keyboard.add_hotkey('5',lambda: webbrowser.open("https://github.com/Kevin-Prabu"))
keyboard.add_hotkey('6',lambda: webbrowser.open("https://chatgpt.com/"))
keyboard.add_hotkey('7',lambda: webbrowser.open("https://classroom.google.com/u/1/"))
keyboard.add_hotkey('8',lambda: webbrowser.open_new_tab())
keyboard.add_hotkey('9',lambda: keyboard.write("hello world")) #use this to write a custom message

#Use this code below to add more hotkeys, when you are out of numbers use letters rather then using mutliple numbers
#keyboard.add_hotkey('',lambda: webbrowser.open(""))

keyboard.wait('esc')
print("Code has ended")