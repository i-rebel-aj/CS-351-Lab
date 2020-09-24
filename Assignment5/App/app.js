const express=require('express');
const app=express();
const bodyParser = require("body-parser");
const mysql = require('mysql');
  
const con = mysql.createConnection({
  host: "cloudlab5.cmmms4en2jqr.us-east-2.rds.amazonaws.com",
  user: "admin",
  password: "akshay123",
  database: "TestDB"
});
con.connect(function(err){
    if(err){
        console.log(err);
    }else{
        console.log("Connected To The Database");
    }
});
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set("view engine", "ejs");

//GET-Requests
app.get("/", (req,res)=>{
    res.render("homepage.ejs")
});
app.get("/user", (req,res)=>{
    res.render("user")
});
app.get("/management", (req,res)=>{
    res.render("management")
});
app.get("/user/send_message", (req,res)=>{
    res.render("send_message");
});
app.get("/management/view_message", (req,res)=>{
    con.query("select * from Messages", (err, result)=>{
        if(err){
            console.log(err);
            res.redirect("/");
        }else{
            res.render("management_messages", {results: result});
        }
    });
});
//POST-Request
app.post("/management/register", (req,res)=>{
    const Email=req.body.ManagerEmail;
    const pass=req.body.ManagerPass;
    con.query("insert into User Values(?,?,\"Manager\")",[Email, pass], (err, result)=>{
        if(err){
            console.log(err);
        }else{
            console.log("Entry Success");
            res.redirect("/management/view_message");
        }
    });
});
app.post("/user/view_message", (req, res)=>{
    const Email=req.body.customerEmail;
    con.query("select * from Messages where email=?",[Email], (err, result)=>{
        if(err){
            console.log(err);
            res.redirect("/");
        }else{
            res.render("user_messages", {results: result});
        }
    });
});
app.post("/user/send_message", (req,res)=>{
    console.log(req.body);
    const Email=req.body.customerEmail;
    const Message=req.body.customerMessage;
    console.log(Message);
    con.query("insert into Messages Values(?,?)",[Message,Email], (err, result)=>{
        if(err){
            console.log(err);
        }else{
            console.log("Entry Success");
            res.redirect("/user/send_message");
        }
    });
});
app.post("/user/register", (req,res)=>{
    console.log(req.body);
    const Email=req.body.customerEmail;
    const pass=req.body.customerPass;
    con.query("insert into User Values(?,?,\"Customer\")",[Email, pass], (err, result)=>{
        if(err){
            console.log(err);
        }else{
            console.log("Entry Success");
            res.redirect("/user/send_message");
        }
    });
});
app.post("/user/login", (req,res)=>{
    const Email=req.body.customerEmail;
    const pass=req.body.customerPass;
    con.query("select password from User where email=? AND usertype=\"Customer\"",[Email], (err, result)=>{
        if(err){
            console.log(err);
        }else{
            if(result.length>0){
                const temp=result[0].password;
                if(temp===pass){
                    console.log("Login is success");
                    res.redirect("/user/send_message");
                }
            }else{
                console.log("Username not found");
                res.redirect("/")
            }
            
        }
    });
});
app.post("/management/login", (req,res)=>{
    const Email=req.body.customerEmail;
    const pass=req.body.customerPass;
    con.query("select password from User where email=? AND usertype=\"Manager\"",[Email], (err, result)=>{
        if(err){
            console.log(err);
        }else{
            if(result.length>0){
                const temp=result[0].password;
                if(temp===pass){
                    console.log("Login is success");
                    res.redirect("/management/view_message");
                }
            }else{
                console.log("Username not found");
                res.redirect("/")
            }
            
        }
    });
});


app.get("*", (req,res)=>{
    res.send("Some Error page will go here");
})
app.listen(3000, ()=>{
    console.log("Server Has started");
})