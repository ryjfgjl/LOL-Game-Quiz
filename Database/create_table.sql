# team
drop table if exists team;
create table team
(
    id int unsigned primary key auto_increment,
    tid varchar(255) default null,
    name varchar(255) default null,
    area varchar(255) default null
);


commit;

