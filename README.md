# Laptop Sleep Timer

**Python automation script that monitors system inactivity and triggers sleep mode, saving battery life and extending laptop lifespan.**

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



## 📋 Table of Contents
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Author](#author)


## 🎯 The Problem

**You want to fall asleep listening to Spotify, but your laptop stays on all night.**

**What happens:**
- Play music/podcast to fall asleep 🎵
- Fall asleep within 30-60 minutes 😴
- Laptop keeps playing all night ❌
- Wake up to dead battery (100% → 0%) 🔋
- Wasted electricity + reduced battery lifespan 💸

**Why Windows sleep timer doesn't help:**
- Can't set a one-time sleep timer
- Sleep settings interfere with music playback
- Too complex to adjust every night

---


## 💡 The Solution

**Run a Python script with your desired sleep time:**

```bash
python sleep_timer.py 45
```

**What it does:**
1. You start the script with a time (e.g., 45 minutes)
2. Play your Spotify/music/podcast
3. Script waits 45 minutes
4. Laptop automatically sleeps
5. You're already asleep, battery saved ✅

**Real-world usage:**
```bash
# Going to bed, want to sleep in 30 mins
python sleep_timer.py 30

# Longer playlist, need 60 mins
python sleep_timer.py 60

# Quick nap, 15 mins
python sleep_timer.py 15
```

---

