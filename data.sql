create table users(
id integer primary key autoincrement,
name text not null,
admin boolean not null
);
create table (
id integer primary key autoincrement,
expert_id integer not null
);
