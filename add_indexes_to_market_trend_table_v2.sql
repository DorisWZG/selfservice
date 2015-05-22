LOCK tables self_service.market_trend WRITE;

ALTER TABLE `self_service`.`market_trend` 
ADD INDEX `index_date_column` (`index_date` DESC),
ADD INDEX `index_cat1` (`cat1_id` ASC),
ADD INDEX `index_cat2` (`cat2_id` ASC),
ADD INDEX `index_cat3` (`cat3_id` ASC);