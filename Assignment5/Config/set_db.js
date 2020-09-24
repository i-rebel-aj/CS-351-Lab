var mysql = require('mysql');

var con = mysql.createConnection({
  host: "cloudlab5.cmmms4en2jqr.us-east-2.rds.amazonaws.com",
  user: "admin",
  password: "akshay123",
  database: "TestDB"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected! to the Database");
  var sql="create table User(email varchar(50) primary key, password varchar(100), usertype varchar(20))";
  con.query(sql, (err, result)=>{
	  if(err){
		console.log("Some error was there in creating user table");
	  }
  });
  sql="create table Messages(message varchar(100), email varchar(50))";
  con.query(sql, (err, result)=>{
	  if(err){
		console.log("Some error was there in creating Message table");
	  }else{
		console.log("Tables created successfully!");
	  }
  });
});
