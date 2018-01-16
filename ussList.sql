create table if not exists usslist (
	symbol  VARCHAR(28),
	code    VARCHAR(28),
	name    VARCHAR(28),
	'current' REAL,
	percent REAL,
	change  REAL,
	high    REAL,
	low REAL,
	high52w REAL,
	low52w  REAL,
	marketcapital   BIGINT,
	amount  REAL,
	'type'    INT,
	pettm   REAL,
	volume  BIGINT,
	hasexist    BOOL,
	timestamp INTEGER
);

