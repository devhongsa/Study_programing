npm init -y 
npm install -g nodemon    //서버자동으로 껐다가 켜주는기능.  nodemon index.js 로 서버실행해야함.
npm install express --save 
npm install ejs pug --save 

https://expressjs.com/en/api.html    // express 공식 docs 



const http = require('http');


const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain; charset=utf-8');              //응답헤더, utf-8은 한글을 응답해줄때 글자 깨지지않게 해줌.
  res.end('Hello World');                                   //뭘 응답해줄건지.
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});



////////

const http = require("http");
const fs = require("fs");

const hostname = "127.0.0.1";
const port = 5000;

const server = http.createServer((req, res) => {
  console.log(req.url);
  switch (req.url) {
    case "/img":
      fs.readFile(__dirname + "/public/1.png", function (err, data) {       //3000/img를 브라우저에 치면 이미지파일을 보내줌.
        if (err) {
          res.writeHead(404);
          res.end(JSON.stringify(err));
          return;
        }
        res.writeHead(200);
        res.end(data);
      });
      break;

    default:
      fs.readFile(__dirname + "/public/index.html", function (err, data) {      //이렇게하면 브라우저에서 3000/ 뒤에 뭘 붙이던 index.html 파일을 보내주게됨.
        if (err) {
          res.writeHead(404);
          res.end(JSON.stringify(err));
          return;
        }
        res.writeHead(200);
        res.end(data);
      });
      break;
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

// __dirname 은 지금 서버가 실행되고있는 절대위치를 말함. /Express 
// req.url은 브라우저에서 localhost:3000 이렇게 되어있으면 그냥 '/' 만약 홈페이지에서 3000/public/index.html 이렇게 하면
// req.url = /public/index.html 이 되고, 그에 따른 경로에서 파일을 읽어서 보내줌. 




npm install node-static 

const http = require("http");
const statik = require("node-static");

const hostname = "127.0.0.1";
const port = 5000;
const file = new statik.Server("./public");

const server = http.createServer((req, res) => {
  console.log(req.url);
  switch (req.url) {
    case "/img":
      file.serveFile("/1.png", 500, {}, req, res);
      break;

    default:
      file.serveFile("/index.html", 500, {}, req, res);
      break;
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});




/////////////////////


const express = require('express');
const app = express();
const port = 3000;

app.use(express.static("public"));     //파일 경로 설정. public이라는 폴더로 지정. 이러면 index.html 파일에서 public안에 있는 이미지파일들을 불러올 수 있게됨.

app.get('/', (req,res)=>{
    res.send('Hello World');
})

app.get('/index', (req,res)=>{
    res.sendFile(__dirname + "public/index.html");      //이렇게 하면 파일도 보낼 수 있음.
})


app.get("/test", (req,res)=>{           //  "/test"는 endpoint 설정,   /test 이 endpoint로 접속하면 어떤 것을 보낼지. res.send("test!")
    res.send("test!");
})

app.all('*', (req,res)=>{               // '*' 이거는 모든 경로에 대해서 어떤 응답을 하라는 뜻임. 만약 이 코드 뒤에 또 다른 get 경로를 설정한다면 무시가됨.
    res.status(404).send("찾을 수 없는 페이지입니다!")              //이를 이용해서 맨마지막에 * 경로를 설정해서 404페이지를 만들면됨.
})
// all은 get과 post , delete 요청 모두를 포함한 것임.

app.listen(port, ()=>{
    console.log(`Example app listening on port ${port}`)
})

//listen은 서버를 실행하겠다는 것. 




//////////////////form으로 데이터 전송하기 : GET ////////////////////////////

// index.html 
{/* <html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="/calculator" method="get">               //form의 action은 form이 submit 됐을때, url을 /calculator로 바꾸고 
        <input type="number" name="num1" id="">             // method get으로 input의 데이터를 url의 쿼리로 바꿈 /calculator?num1=3&num2=5 이런식으로 
        <br />                                              // 그러면 query정보는 req.query에 전달이되고 {num1:"3", num2:"5"} 이런식으로 보냄.
        +
        <br />
        <input type="number" name="num2" id="">
        <br />
        <br />
        <button type="submit">제출</button>
    </form>
</body>

</html> */}
//url은 /calculator?num1=3&num2=5   이렇게 만들어짐.



// index.js

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.get("/calculator", (req, res) => {
  console.log(typeof req.query.num1);                       //여기서 query = {num1:"3", num2:"5"} 이런식으로 옴.
  let result = Number(req.query.num1) + Number(req.query.num2);
  res.send(`결과는 = ${result}`)
  //res.send(String(result));                               // send는 숫자를 보낼수가 없음 , string이나 object를 보낼수 있음.
});



//////////////////form으로 데이터 전송하기 : POST ////////////////////////////
//index.html 에서 method를 post로 변경

//post에서는 form의 정보들이 req.query에 담기는 것이 아닌 req.body에 담긴다. 

/* ... */
app.use(express.urlencoded({ extended: false }));           //body parser 없어도 이 코드사용하면, express에서 request의 body 부분을 사용할 수 있음.
/* ... */
app.post("/calculator", (req, res) => {
  console.log(req.body);
  let result = Number(req.body.num1) + Number(req.body.num2);       //req.body = {num1:"3", num2:"5"}
  res.sendFile(__dirname + "/public/result.html");                 // 여기서 sendFile의 문제점은 result 값을 html파일로 전달할 방법이 없어서 result를 response 할 수 가 없음.
});
//그래서 express 템플릿 엔진을 사용해야됨.
/* ... */





////////////////////// express 템플릿 : EJS, PUG ///////////////////////////////

