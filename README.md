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


# 🎯 The Problem

**My laptop wouldn't go to sleep automatically.**

**Symptoms:**
- played songs on laptop on overnight → dead battery by morning
- Windows sleep settings weren't working consistently
- Battery health declining (constant power drain)
- Wasted electricity when laptop idle for hours

**Root Cause:**
Windows 10/11 sleep timer occasionally fails when:
- Background processes prevent sleep
- External devices connected
- Power plan conflicts
- Windows Updates pending

**Impact:**
- ~30% battery capacity lost over 6 months
- ₦5,000+ monthly electricity waste
- Frustration from dead laptop before important tasks
- Reduced laptop lifespan

**Why Not Just Fix Windows Settings?**
- Tried: Power Options, Group Policy, Registry tweaks
- Result: Worked sometimes, failed randomly
- Need: Reliable, automated solution
