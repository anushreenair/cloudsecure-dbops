#!/bin/bash
# MariaDB Backup Script

TIMESTAMP=$(date +"%F")
BACKUP_DIR="/backup/$TIMESTAMP"
mkdir -p "$BACKUP_DIR"
mysqldump -u root -p'your_password' --all-databases > "$BACKUP_DIR/all_databases.sql"
echo "Backup completed at $BACKUP_DIR"