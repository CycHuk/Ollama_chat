CREATE DATABASE IF NOT EXISTS OllamaChat
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE OllamaChat;

CREATE TABLE IF NOT EXISTS chats (
    id CHAR(36) DEFAULT (UUID()) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    can_user_write BOOLEAN DEFAULT TRUE,
    response_by ENUM('support', 'bot') DEFAULT 'bot',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id CHAR(36) NOT NULL, 
    writer ENUM('bot', 'support', 'user') NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chat_id) REFERENCES chats(id) ON DELETE CASCADE ON UPDATE CASCADE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
