db = db.getSiblingDB("trading_db");
db.createCollection("users");
db.createCollection("trade_logs");
db.users.insert({ username: "admin", balance: 10000 });
