CREATE TABLE food_desc (

	ndb_no varchar(5) NOT NULL PRIMARY KEY,
	fd_grp_cd varchar(4) NOT NULL,
	long_desc varchar(200) NOT NULL,
	short_desc varchar(60) NOT NULL,
	com_name varchar(100),
	manufac_name varchar(65),
	survey varchar(1),
	ref_desc varchar(135),
	refuse smallint,
	sci_name varchar(65),
	n_factor numeric(4,2),
	pro_factor numeric(4,2),
	fat_factor numeric(4,2),
	cho_factor numeric(4,2)
)
