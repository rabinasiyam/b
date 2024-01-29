
#!/bin/bash

TELEGRAM_BOT_TOKEN="6766117217:AAEOz-GXkWyz7U1aFpOIw_mg5B913f_dgKY"
CHAT_ID="5779948934"

while true; do
    CURRENT_TIME=$(TZ="GMT+6" date +"%Y-%m-%d %H:%M:%S GMT+6")
    MESSAGE="Current time in GMT+6: $CURRENT_TIME"
    
    # Send message to Telegram bot using curl
    curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
        -d "chat_id=$CHAT_ID" \
        -d "text=$MESSAGE"
    
    sleep 300  # Sleep for 5 minutes
done
