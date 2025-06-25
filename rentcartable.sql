-- Active: 1750097674429@@cis2368summer.cidyiu02y2ba.us-east-1.rds.amazonaws.com@3306@cis2368summerdb
CREATE TABLE rentcar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    passengername VARCHAR(100),
    origincity VARCHAR(100),
    destinationcity VARCHAR(100),
    make VARCHAR(50),
    model VARCHAR(50),
    totalprice DECIMAL(10, 2)
);
