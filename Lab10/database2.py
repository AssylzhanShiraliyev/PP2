import psycopg2
import json
from datetime import datetime

class SnakeGameDB:
    def __init__(self):
        """Initialize database connection"""
        self.conn = psycopg2.connect(
            host="localhost",
            database="snake_game",
            user="postgres",
            password="your_password"  # Change to your password
        )
        self.cur = self.conn.cursor()
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary tables if they don't exist"""
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS players (
                player_id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS game_sessions (
                session_id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(player_id),
                score INTEGER NOT NULL,
                level INTEGER NOT NULL,
                snake_length INTEGER NOT NULL,
                game_data JSONB,
                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def get_or_create_player(self, username):
        """Get player ID or create new player"""
        self.cur.execute(
            "SELECT player_id FROM players WHERE username = %s",
            (username,)
        )
        player = self.cur.fetchone()
        
        if player:
            return player[0]
        else:
            self.cur.execute(
                "INSERT INTO players (username) VALUES (%s) RETURNING player_id",
                (username,)
            )
            player_id = self.cur.fetchone()[0]
            self.conn.commit()
            return player_id
    
    def save_game_session(self, player_id, score, level, snake_length, game_data):
        """Save game session to database"""
        self.cur.execute("""
            INSERT INTO game_sessions 
            (player_id, score, level, snake_length, game_data)
            VALUES (%s, %s, %s, %s, %s)
        """, (player_id, score, level, snake_length, json.dumps(game_data)))
        self.conn.commit()
    
    def get_player_stats(self, player_id):
        """Get player statistics"""
        self.cur.execute("""
            SELECT MAX(score), MAX(level), MAX(snake_length)
            FROM game_sessions 
            WHERE player_id = %s
        """, (player_id,))
        return self.cur.fetchone()
    
    def close(self):
        """Close database connection"""
        self.cur.close()
        self.conn.close()