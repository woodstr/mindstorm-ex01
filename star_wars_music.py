import asyncio
import time

# from https://air.imag.fr/images/1/1b/ImperialMarch.pde.txt and GitHub copilot
async def beep_imperial_march(ev3):
    # define the notes
    c = 261
    d = 294
    e = 329
    f = 349
    g = 391
    gS = 415
    a = 440
    aS = 455
    b = 466
    cH = 523
    cSH = 554
    dH = 587
    dSH = 622
    eH = 659
    fH = 698
    fSH = 740
    gH = 784
    gSH = 830
    aH = 880

    # play imperial march!

    # start
    ev3.speaker.beep(a, 500)
    ev3.speaker.beep(a, 500)
    ev3.speaker.beep(a, 500)
    ev3.speaker.beep(f, 350)
    ev3.speaker.beep(cH, 150)

    ev3.speaker.beep(a, 500)
    ev3.speaker.beep(f, 350)
    ev3.speaker.beep(cH, 150)
    ev3.speaker.beep(a, 1000)

    ev3.speaker.beep(eH, 500)
    ev3.speaker.beep(eH, 500)
    ev3.speaker.beep(eH, 500)
    ev3.speaker.beep(fH, 350)
    ev3.speaker.beep(cH, 150)

    ev3.speaker.beep(gS, 500)
    ev3.speaker.beep(f, 350)
    ev3.speaker.beep(cH, 150)
    ev3.speaker.beep(a, 1000)

    # mid part (climb in pitch)
    ev3.speaker.beep(aH, 500)
    ev3.speaker.beep(a, 350)
    ev3.speaker.beep(a, 150)
    ev3.speaker.beep(aH, 500)
    ev3.speaker.beep(gSH, 250)
    ev3.speaker.beep(gH, 250)

    ev3.speaker.beep(fSH, 125)
    ev3.speaker.beep(fH, 125)
    ev3.speaker.beep(fSH, 250)
    time.sleep(0.05)
    ev3.speaker.beep(aS, 250)
    ev3.speaker.beep(dSH, 500)
    ev3.speaker.beep(dH, 250)
    ev3.speaker.beep(cSH, 250)

    ev3.speaker.beep(cH, 125)
    ev3.speaker.beep(b, 125)
    ev3.speaker.beep(cH, 250)
    time.sleep(0.05)
    ev3.speaker.beep(f, 125)
    ev3.speaker.beep(gS, 500)
    ev3.speaker.beep(f, 375)
    ev3.speaker.beep(a, 125)

    ev3.speaker.beep(cH, 500)
    ev3.speaker.beep(a, 375)
    ev3.speaker.beep(cH, 125)
    ev3.speaker.beep(eH, 1000)

    # end part (like mid part but with end)
    ev3.speaker.beep(aH, 500)
    ev3.speaker.beep(a, 350)
    ev3.speaker.beep(a, 150)
    ev3.speaker.beep(aH, 500)
    ev3.speaker.beep(gSH, 250)
    ev3.speaker.beep(gH, 250)

    ev3.speaker.beep(fSH, 125)
    ev3.speaker.beep(fH, 125)
    ev3.speaker.beep(fSH, 250)
    time.sleep(0.05)
    ev3.speaker.beep(aS, 250)
    ev3.speaker.beep(dSH, 500)
    ev3.speaker.beep(dH, 250)
    ev3.speaker.beep(cSH, 250)

    ev3.speaker.beep(cH, 125)
    ev3.speaker.beep(b, 125)
    ev3.speaker.beep(cH, 250)
    time.sleep(0.05)
    ev3.speaker.beep(f, 250)
    ev3.speaker.beep(gS, 500)
    ev3.speaker.beep(f, 375)
    ev3.speaker.beep(cH, 125)

    ev3.speaker.beep(a, 500)
    ev3.speaker.beep(f, 375)
    ev3.speaker.beep(c, 125)
    ev3.speaker.beep(a, 1000)

    return