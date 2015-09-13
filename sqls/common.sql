CREATE TABLE IF NOT EXISTS `mobile_device_tokens` (
  `mobile_device_id` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `cloud_registration_id` longtext,
  `user_id` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mobile_device_tokens`
--

-- Test insert

INSERT INTO `mobile_device_tokens` (`mobile_device_id`, `cloud_registration_id`, `user_id`) VALUES
('4001', 'APA91bH_s8KxnQmUuDOjKkE1mNcV2f2Fx9bcZScvhHg06BjHAlDYRqN5hvwfdo0lFTNdlcE2U4XGhwzd1MKjxopiI8_DOlnSztWGXFaL3sNtNxa7pkHOTxYYsHmDKz07wrh6ZI8iPv5o', 'sbose78@gmail.com');


--
-- Table structure for table `task_status`
--

CREATE TABLE IF NOT EXISTS `task_status` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(32) DEFAULT NULL,
  `input` varchar(5000) DEFAULT NULL,
  `output` varchar(256) DEFAULT NULL,
  `type` varchar(32) DEFAULT NULL,
  `celery_task_id` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;


