
# world2019
DROP TABLE IF EXISTS world2019;
CREATE TABLE world2019
(
	id int unsigned primary key auto_increment,
	date varchar(255) default null,
	processor varchar(255) default null,
	dayNum varchar(255) default null,
	dayOrder varchar(255) default null,
    teamA varchar(255) default null,
    teamB varchar(255) default null,
    scoreA varchar(255) default null,
    scoreB varchar(255) default null,
	fullTeamA varchar(255) default null,
    fullTeamB varchar(255) default null
);

# rank2019
DROP TABLE IF EXISTS rank2019;
CREATE TABLE rank2019
(
	id int unsigned primary key auto_increment,
    teamName varchar(255) default null,
    rank varchar(255) default null,
	region VARCHAR(255) DEFAULT NULL
);


commit;	

#####################################
# worlds 2020

# world2020
DROP TABLE IF EXISTS world2020;
CREATE TABLE world2020
(
	id int unsigned primary key auto_increment,
	date varchar(255) default null,
	processor varchar(255) default null,
	dayNum varchar(255) default null,
	dayOrder varchar(255) default null,
    teamA varchar(255) default null,
    teamB varchar(255) default null,
    scoreA varchar(255) default null,
    scoreB varchar(255) default null,
	fullTeamA varchar(255) default null,
    fullTeamB varchar(255) default null
);

# rank2020
DROP TABLE IF EXISTS rank2020;
CREATE TABLE rank2020
(
	id int unsigned primary key auto_increment,
    teamName varchar(255) default null,
    rank varchar(255) default null,
	region VARCHAR(255) DEFAULT NULL
);


commit;	



	
