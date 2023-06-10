DROP TABLE IF EXISTS races;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS prompts;

CREATE TABLE races (
    race_id integer primary key autoincrement,
    prompt_id int not null,
    user_id int not null,
    prompt_title int not null,
    wpm int not null,
    mistakes int not null,
    foreign key (user_id) references user (user_id),
    foreign key (prompt_id) references prompt (prompt_id)
);

CREATE TABLE users (
    user_id integer primary key autoincrement,
    username text unique not null,
    password text not null
);

CREATE TABLE prompts (
    prompt_id integer primary key autoincrement,
    title text not null,
    prompt text not null
);