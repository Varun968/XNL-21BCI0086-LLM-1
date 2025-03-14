CREATE TABLE trades (
    id UUID DEFAULT generateUUIDv4(),
    asset String,
    price Float64,
    quantity Float64,
    tradeType String,
    timestamp DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY timestamp;
