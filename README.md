# Weekly Schedule Customiser
***"Stay organised. Stay nerdy. Prettily."***
For all the HKU students who want to have their weekly schedule as their phone's wallpaper. Now you can show everybody how early you must wake up in the colours and font of your choice!

## Installation and Usage


https://user-images.githubusercontent.com/48514988/151202126-c55c84ff-1144-46d3-a482-93be99663228.mp4


1. Open a browser tab, login to HKU Portal, navigate to Timetables > My Weekly Schedule
2. Hit **Ctrl+s or right-click and click "Save as..."**.
3. Download [this executable file](https://github.com/DarrenChangJR/Weekly-Schedule-Customiser/releases/download/v1.0/scheduler.exe), and save it into the folder **"View My Weekly Schedule_files"** that was downloaded previously.
4. *Note: the "scheduler.exe" is not meant to be double-clicked, but doing so still produces a html file with the default font and colours.*
5. **Shift+right-click** anywhere and you will see **"Open command window here" and/or "Open PowerShell window here"**, click either one of them.
    * If you opened 'command window', proceed to the next step.
    * If you opened **'PowerShell'**, type **`cmd` and hit enter** before proceeding.
    * *For those comfortable with using the command-line, type `scheduler -h` to see the help menu*
6. Pick your colours from this [colour picker](https://g.co/kgs/E73EBi). Copy the **hexadecimal codes** of your chosen colours (such as #000000 for black and #ffffff for white).
7. Pick your **font-family** from these five options (serif, sans-serif, cursive, fantasy, monospace). [Learn more about font-families](https://www.masterclass.com/articles/font-family-guide#5-generic-font-families)
8. In the command/PowerShell window, enter your chosen font-family and colours. For example:

  `scheduler --font=sans-serif --background=#666666 --table=#009879`  
  `scheduler --font=serif --background=#444444 --table=#0088cc`  

9. You're done! Your very own schedule can now be found in the File Explorer in the aptly named **"your_very_own_schedule.html"** file. Just double-click this file to open it with your browser of choice and take a screenshot of it.  

10. If you would like to customise it more, feel free to repeat steps 6 to 8 as needed. "your_very_own_schedule.html" file will continuously update, just refresh the page on your browser after step 9 every time.
## Notes
1. If I ever find enough free time, I will implement a GUI for this.
2. Tested on Brave and Chrome browsers.
