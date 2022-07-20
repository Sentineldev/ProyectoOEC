schema = [
    """
    CREATE TABLE users(
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username varchar(32) UNIQUE KEY,
        password varchar(128),
        email varchar(256)
    );
    """,
    """
    CREATE TABLE articles(
        article_id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
        user_id INT,
        title varchar(128),
        body LONGTEXT,
        img_url LONGTEXT
    )
    """
]