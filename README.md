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


## ✨ Features

- ⏱️ **Simple command-line usage:** `python sleep_timer.py <minutes>`
- 💤 **Set and forget:** Script runs in background, sleeps laptop automatically
- 🎵 **Perfect for music:** Fall asleep to Spotify without battery drain
- ⚡ **Lightweight:** < 50 lines of code, no dependencies
- 🔋 **Battery saver:** Prevents overnight drain (saves ₦5,000+/month electricity)

---


## 🚀 Quick Start

### Installation

**1. Download the script**
```bash
git clone https://github.com/0sinach1/laptop-sleep-timer.git
cd laptop-sleep-timer
```

**2. Run it!**
```bash
# Sleep in 30 minutes
python sleep_timer.py 30
```

That's it! No installation, no dependencies.

---

## 📖 Usage

### Basic Usage

```bash
python sleep_timer.py <minutes>
```

**Examples:**

```bash
# Sleep in 45 minutes (typical music session)
python sleep_timer.py 45

# Sleep in 1 hour (long podcast)
python sleep_timer.py 60

# Sleep in 20 minutes (quick nap)
python sleep_timer.py 20
```

### My Typical Workflow

```bash
# 10:30 PM - Getting ready for bed
# Open Spotify, start playlist

# 10:45 PM - In bed, ready to sleep
python sleep_timer.py 30

# Output:
# Laptop will sleep in 30 minutes (at 11:15 PM)
# Timer started...

# 11:00 PM - I'm asleep
# 11:15 PM - Laptop automatically sleeps
# 7:00 AM - Wake up, laptop still has battery! ✅
```

---
