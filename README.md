# Weekly Schedule Customiser
***"Stay organised. Stay nerdy. Prettily."***
For all the HKU students who want to have their weekly schedule as their phone's wallpaper. Now you can show everybody how early you must wake up in the colours and font of your choice!

## Installation and Usage
1. Open a browser tab, login to HKU Portal, navigate to Timetables > My Weekly Schedule
2. Hit Ctrl+s on your keyboard or right-click and click "Save as...". Take note of the destination folder. For example, it may be downloaded to your Downloads folder "C:\Users\Obama\Downloads".
3. Download [this executable file](), and save it into the folder "View My Weekly Schedule_files" that was downloaded previously. For example, save it into "C:\Users\Obama\Downloads\View My Weekly Schedule_files".
4. Great! You've downloaded everything you need to! Now open File Explorer and navigate to the "View My Weekly Schedule_files". You should see "scheduler.exe" along with many other files that you need not care about. The "scheduler.exe" is **NOT** meant to be double-clicked.
5. Shift+right-click anywhere and you will see "Open command window here" and/or "Open PowerShell window here", click either one of them. You will a black/blue screen with nothing but texts.
6. *For those comfortable with using the command-line, type `scheduler -h` to see the help menu*
7. Pick the colours you want from this [colour picker](https://www.w3schools.com/colors/colors_picker.asp). Copy the hexadecimal codes of your chosen colours (such as #000000 for black and #ffffff for white).
8. Pick your font-family from these five choices (serif, sans-serif, cursive, fantasy, monospace). [Learn more about font-families](https://www.masterclass.com/articles/font-family-guide#5-generic-font-families)
9. In the command/PowerShell window, enter your chosen font-family and colours. For example:
`schedule --font=sans-serif --background=#666666 --table=#009879`
Hit Enter.
10. You're done! Your very own schedule can now be found in the File Explorer in the aptly named "your_very_own_schedule.html" file. Just double-click this file to open it with your browser of choice and take a screenshot of it.
11. If you would like to customise it more, feel free to repeat steps 7 to 10 as needed.
## Notes
1. If I ever find enough free time, I will implement a GUI for this. So, pretty unlikely.
2. Tested on Brave, Chrome.