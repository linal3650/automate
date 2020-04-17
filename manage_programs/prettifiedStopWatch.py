#! python3
# prettifiedStopWatch.py

import time, pyperclip

def stopwatch():
    """Records time spent per task, prints and stores in clipboard"""

    # Display the program's instructions
    input('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Crtl-C to quit.\n')
    print('Started.')
    startTime = time.time()     # Get the first lap's start time
    lastTime = startTime
    lapNum = 1

    # Start tracking the lap times
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            info = 'Lap #{}: {} ({})'.format(str(lapNum).rjust(1), str(totalTime).center(7), str(lapTime).rjust(4))
            print(info, end='')

            lapNum += 1
            lastTime = time.time() # reset the last lap time

    except KeyboardInterrupt:
        # Handle the Crtl-C exception to keep its error message from displaying
        pyperclip.copy(clip)
        print('\nDone.')
        print('Results available in clipboard')

if __name__ == "__main__":
    stopwatch()
