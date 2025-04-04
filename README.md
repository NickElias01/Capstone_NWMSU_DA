# Colorado Regional Energy Monitoring Suite by Elias Analytics

Real-time energy monitoring system that tracks and visualizes power usage and temperature data across multiple regions in Colorado.


## Table of Contents
- [Features](#features)
- [API Integration](#api-integration)
- [Component Details](#component-details)
- [Prerequisites](#prerequisites)
- [Quick Start with Docker](#quick-start-with-docker-recommended)
- [Manual Installation](#manual-installation)
- [Project Structure](#project-structure)
- [Monitoring and Logs](#monitoring-and-logs)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Support](#support)



## Features

- 📊 Real-time power usage visualization
- 🌡️ Temperature monitoring across regions
- ⚡ Renewable energy percentage tracking
- ⚠️ Automated alert system for threshold violations
- 💾 Data persistence with SQLite
- 📝 Comprehensive logging system

## API Integration

The system uses the Open-Meteo API to fetch real-time temperature data for each monitored region:

- **API Provider**: [Open-Meteo](https://open-meteo.com/)
- **Endpoint**: Current Weather Data
- **Data Points**: Temperature in Celsius
- **Regions**: Denver, Boulder, Aurora, Lakewood, Golden

### Features
- Real-time temperature data fetching
- Automatic fallback to synthetic data if API fails
- Rate-limit compliant
- Error handling with logging

### Testing API Connection

To verify API connectivity:
```bash
python -m tests.test_weather_api
```

Expected output:
```
Testing Open-Meteo API connection for all regions...
--------------------------------------------------
✅ Denver: 23.5°C
✅ Boulder: 22.1°C
✅ Aurora: 23.8°C
✅ Lakewood: 22.9°C
✅ Golden: 21.7°C
--------------------------------------------------
```

## Component Details

### Consumer Script
The consumer script (`consumers/energy_data_consumer.py`) is responsible for:

#### Data Processing
- Receives real-time energy metrics from Kafka
- Processes messages containing power usage and temperature data
- Handles data for multiple Colorado regions concurrently

#### Visualization
- Creates dynamic line plots showing power usage trends
- Displays real-time bar charts of temperature readings
- Updates visualization every second
- Color-codes different regions for easy identification

#### Alert System
- Monitors for threshold violations:
  - High/Low power usage (>5000kW or <500kW)
  - Extreme temperatures (>50°C or <0°C)
  - Low renewable energy percentage (<5%)
- Generates immediate alerts for any violations
- Logs alerts to separate alert log files

#### Data Storage
- Persists all readings to SQLite database
- Maintains historical data for trend analysis
- Ensures data integrity with thread-safe operations

## Prerequisites

- Windows, macOS, or Linux
- Python 3.9 or higher
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for quick start method)
- [Apache Kafka & Zookeeper](https://kafka.apache.org/quickstart) (for manual installation method)

## Quick Start with Docker (Optional, if not using Docker skip to [Manual Installation](#manual-installation))

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NickElias01/streamingdata-project-06-nickelias.git
   cd streamingdata-project-06-nickelias
   ```

2. **Create `.env` file:**
   ```bash
   copy .env.template .env
   ```

3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

This will start all services: Kafka, Zookeeper, Producer, and Consumer.

## Manual Installation

1. **Set up Python environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate # Linux/macOS
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` file:**
   ```bash
   copy .env.template .env
   ```

4. **Start Kafka and Zookeeper:**
   - Download and extract [Kafka](https://kafka.apache.org/downloads)
   - Start Zookeeper (Terminal 1):
     ```bash
     cd ~/kafka
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - Start Kafka (Terminal 2):
     ```bash
     cd ~/kafka
     bin/kafka-server-start.sh config/server.properties
     ```

5. **Run the Producer (Terminal 3):**
   ```bash
   python -m producers.energy_data_producer
   ```

6. **Run the Consumer (Terminal 4):**
   ```bash
   python -m consumers.energy_data_consumer
   ```

## Project Structure

```
streamingdata-project-06-nickelias/
├── consumers/              # Consumer components
├── producers/              # Producer components
├── utils/                 # Utility modules
├── logs/                  # Application logs
│   ├── normal/           # Regular operation logs
│   ├── alerts/           # Warning and threshold alerts
│   └── errors/           # Error and critical logs
├── data/                 # SQLite database
├── docker-compose.yml    # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Monitoring and Logs

- **Normal operations:** `logs/normal/normal_YYYYMMDD.log`
- **Alert conditions:** `logs/alerts/alerts_YYYYMMDD.log`
- **Error logs:** `logs/errors/errors_YYYYMMDD.log`

## Configuration

Key settings in `.env`:
```ini
KAFKA_TOPIC=energy_data
KAFKA_BROKER=kafka:9092
MESSAGE_INTERVAL_SECONDS=5
```

## Troubleshooting

1. **No visualization?**
   - Ensure X11 forwarding is enabled
   - Check matplotlib backend settings

2. **Connection refused?**
   - Verify Kafka and Zookeeper are running
   - Check broker address in `.env`

3. **No data flowing?**
   - Confirm producer is running
   - Check Kafka topic exists

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and questions, please open a GitHub issue.