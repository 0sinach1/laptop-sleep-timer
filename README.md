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


## ✨ Features

### Core Functionality
- ⏱️ **Inactivity Detection:** Monitors keyboard and mouse events
- 💤 **Automatic Sleep:** Triggers system sleep after timeout
- 🔧 **Configurable Timeout:** Adjust inactivity threshold (5-60 minutes)
- 📝 **Logging:** Records all sleep events for debugging
- 🔄 **Background Operation:** Runs silently via Task Scheduler

### Smart Features
- 🎯 **Idle vs Active Detection:** Distinguishes real inactivity from background tasks
- ⚡ **Low Resource Usage:** < 1% CPU, < 20MB RAM
- 🛡️ **Safe Shutdown:** Checks for unsaved work warnings (optional)
- 📊 **Statistics Tracking:** How often sleep triggered, time saved

### Advanced (Optional)
- 🔔 **Pre-sleep Warning:** 1-minute notification before sleep
- ⏸️ **Pause Mode:** Temporarily disable (e.g., during downloads)
- 📅 **Schedule-based:** Different timeouts for weekday vs weekend

---
