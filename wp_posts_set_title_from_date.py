import mysql.connector
import argparse
from datetime import datetime

def format_date(date_obj):
    return date_obj.strftime("%A %B %d, %Y")

def update_post_titles(host, user, password, database):
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    
    # Select posts with no title
    cursor.execute("SELECT ID, post_date FROM wp_posts WHERE post_type = 'post' AND (post_title IS NULL OR post_title = '')")
    posts = cursor.fetchall()
    
    for post_id, post_date in posts:
        new_title = format_date(post_date)
        print(f"Post ID {post_id}: Original Date '{post_date}' -> New Title '{new_title}'")
    
    confirm = input("Apply changes? (yes/no): ").strip().lower()
    if confirm == "yes":
        for post_id, post_date in posts:
            new_title = format_date(post_date)
            cursor.execute("UPDATE wp_posts SET post_title = %s WHERE ID = %s", (new_title, post_id))
        conn.commit()
        print("Changes applied.")
    else:
        print("No changes made.")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update WordPress post titles.")
    parser.add_argument("--host", required=True, help="Database host")
    parser.add_argument("--user", required=True, help="Database username")
    parser.add_argument("--password", required=True, help="Database password")
    parser.add_argument("--database", required=True, help="Database name")
    args = parser.parse_args()
    
    update_post_titles(args.host, args.user, args.password, args.database)
