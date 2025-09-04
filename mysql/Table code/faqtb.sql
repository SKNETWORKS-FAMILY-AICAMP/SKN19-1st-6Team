CREATE TABLE IF NOT EXISTS faq
(
    faq_id    INT AUTO_INCREMENT COMMENT 'FAQ 코드',
    question varchar(3000),
    answer varchar(10000),
    keyword varchar(120),
    company varchar(300),
     CONSTRAINT pk_faq_id PRIMARY KEY (faq_id)
) ENGINE=INNODB COMMENT 'FAQ';

drop table faq_tb;