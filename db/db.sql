create table logs
(
    id        int auto_increment
        primary key,
    operation TEXT  not null,
    result    FLOAT not null
);
