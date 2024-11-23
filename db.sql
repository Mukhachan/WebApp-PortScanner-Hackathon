CREATE TABLE IF NOT EXISTS `WebScanner`.`results` (
    id int NOT NULL AUTO_INCREMENT,
    search_id text NOT NULL,
    ip text NOT NULL,
    port int NOT NULL,
    country text NOT NULL,
    city text NULL,
    service text NOT NULL,
    message text NOT NULL,
    datetime datetime NOT NULL,
    PRIMARY KEY (`id`)
)