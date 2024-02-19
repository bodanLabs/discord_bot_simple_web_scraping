# Discord Status Bot

A Discord bot designed to monitor and update server voice channel names based on the status of services from a specific website. It uses Discord.py for bot functionality, BeautifulSoup for web scraping, and SQLite for database management.

## Features

- **Status Monitoring**: Monitors the status of services from a predefined website and updates Discord voice channel names accordingly.
- **Automatic Updates**: Utilizes tasks to periodically check the service status and update channel names with appropriate emojis to reflect the current state (Working, Updating, Testing).
- **Database Integration**: Stores channel IDs and status information in an SQLite database for persistent tracking and updates.

## Requirements

- Python 3.6+
- discord.py
- BeautifulSoup4
- requests
- sqlite3

## Installation

1. Clone this repository or download the code.
2. Install the required Python packages:
```pip install -r requirements.txt```
3. Create a .env file in the root directory and add your Discord bot token:
```TOKEN=your_discord_bot_token_here```
4. Initialize the SQLite database:
```python init_db.py # You might need to create this script to set up your database tables```
5. Run the bot:
```python bot.py```

## Usage
- !start: Command to manually trigger the status check and update the voice channel names accordingly.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or encounter bugs.

