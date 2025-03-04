# wp-posts-set-title-from-date

A Python script to update WordPress post titles based on their publication date. Useful for cases where posts are missing titles, especially after importing from other platforms like Blogger.

## Features
- Selects WordPress posts with empty or null titles.
- Sets the title based on the post date in the format: `Monday January 01, 2024`.
- Prompts for confirmation before applying changes.

## Requirements
- Python >=3.11

## Installation
1. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with database credentials:
```sh
python wp_posts_set_title_from_date.py --host YOUR_DB_HOST --user YOUR_DB_USER --password YOUR_DB_PASSWORD --database YOUR_DB_NAME
```
