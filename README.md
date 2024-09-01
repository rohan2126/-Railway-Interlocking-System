# Railway Interlocking System using AI, ML, and Raspberry Pi

## Overview
The Railway Interlocking System project aims to enhance the safety of railway operations by preventing derailments and collisions. This system leverages AI and machine learning algorithms, implemented on a Raspberry Pi with load cell integration, to automatically detect and signal potential hazards on railway tracks. The system provides real-time alerts to the control room and makes decisions on track switching to avoid accidents, thereby saving lives and reducing manual intervention.

## Features
- AI-Powered Detection**: Uses AI and machine learning to analyze sensor data and detect potential collisions.
- Real-Time Alerts**: Sends real-time alerts to the control room and the trains when another train is detected on the same track.
- Automated Track Switching**: Automatically switches tracks to prevent collisions.
- Load Cell Integration**: Monitors train weight and speed using load cells for accurate decision-making.
- Raspberry Pi Implementation**: Low-cost and efficient processing with Raspberry Pi.

System Architecture

The system architecture involves several components working together:
 - Sensors: Load cells and other sensors detect train weight, speed, and position.
 - Raspberry Pi: Processes sensor data, runs AI models, and makes decisions.
 - Control Room Interface: Receives alerts and can manually intervene if needed.
 - Track Switching Mechanism: Automatically switches tracks based on system decisions.

Usage

  - Model Training: Use the model_training.py script to train the AI model with your dataset or the provided sample data.
  - System Deployment: Deploy the system on the Raspberry Pi by running the main.py script.
  - Real-Time Monitoring: Monitor the system’s performance in real-time and respond to alerts as necessary.
  - Track Switching: The system will automatically switch tracks if a collision threat is detected.
