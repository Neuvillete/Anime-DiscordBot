@echo off
REM Change directory to the location of your main.py script
cd /d "C:\Users\Aditya\Projects\Anime-DiscordBot"

REM Activate the virtual environment (if you have one)
call venv\Scripts\activate

REM Run the bot.py script
python bot.py

REM Keep the command prompt open after the script finishes
pause
