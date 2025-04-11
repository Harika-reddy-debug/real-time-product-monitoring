CREATE TABLE IF NOT EXISTS customer_events (
    user_id UInt32,
    product String,
    action String,
    timestamp DateTime
) ENGINE = MergeTree()
ORDER BY timestamp;

