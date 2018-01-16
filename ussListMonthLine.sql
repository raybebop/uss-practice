create table if not exists ussMonthLine (
	symbol  VARCHAR(28),
	code    VARCHAR(28),
	name    VARCHAR(28),
	volume BIGINT,
	open REAL,
	high REAL,
	close REAL,
	low REAL,
	chg REAL,
	percent REAL,
	turnrate REAL,
	ma5 REAL,	
	ma10 REAL,	
	ma20 REAL,	
	ma30 REAL,	
	dif REAL,
	dea REAL,
	macd REAL,
	lot_volume BIGINT,
	timestamp INTEGER,
	time TEXT	
);
