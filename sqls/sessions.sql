
BEGIN;
CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` longtext NOT NULL,
    `expire_date` datetime NOT NULL
)
;
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);

COMMIT;
