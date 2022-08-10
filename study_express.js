npm init -y 
npm install -g nodemon    //서버자동으로 껐다가 켜주는기능.  nodemon index.js 로 서버실행해야함. global로 다운받아줘야 nodemon 인식함.
npm install express --save 
npm install --save-dev @types/express
npm install ejs pug --save 
npm install moment --save 
npm install mongodb --sav
npm install --save-dev jest @types/jest supertest @types/supertest   // 서버테스트 패키지
npm install koa   // websocket 사용

https://expressjs.com/en/api.html    // express 공식 docs 
https://inpa.tistory.com/category/Node.js/Node    //좋은 스터디 블로그 


///////////////////////////////////////////////////fastcampus nodejs express//////////////////////////////////////////////////////

// express에서의 middleware? : 요청에서 응답까지의 모든 과정에서 사용되는 함수들(미들웨어)

// main.js
// @ts-check

const express = require("express")
const fs = require("fs")

const app = express()

const PORT = 4000

//app.use 미들웨어
app.use(
  "/",
  async (req, res, next) => {
    //async함수로도 사용가능
    console.log("Middleware 1-1")

    const fileContent = await fs.promises.readFile(".gitignore")
    // @ts-ignore
    req.fileContent = fileContent  //이 방법을 통해 다른 미들웨어간의 데이터 전달 가능
    // @ts-ignore
    req.requestedAt = new Date() 

    next() ///  next의 뜻은 이 미들웨어 작업이 끝났고 다음 미드웨어로 넘어가라는 뜻임 이 코드가 없으면 다음 미들웨어가 실행되지않음
  },
  (req, res, next) => {
    //이런식으로 여러 미들웨어를 한 함수안에 넣을 수 있음
    console.log("Middleware 1-2")
    next()
  }
)

app.use((req, res) => {
  console.log("Middleware 2")
  // @ts-ignore
  res.send(`Hello, express! : ${req.requestedAt}, ${req.fileContent}`)    //다른 미들웨어에서 저장한 정보를 불러옴 
})

app.listen(PORT, () => {
  console.log(`The Express server is listening at port : ${PORT}`)
})
// 



// Path pattern 
//   /ab?cd    : ? 앞에 있는 b문자가 있거나 없어도됨. 하지만 a cd는 반드시 있어야함. 
//   /ab+cd    : b가 몇번이 반복되도 상관없음.    /abbbbbbcd , 근데 b가 없으면 안됨. 
//   /ab*cd    :  ab와 cd 중간에 어떤게 와도 상관없음. /absdklfjsecd   , ab로시작해서 cd로 끝나기만 하면됨.
//   /a(bc)?d  : ?의 적용을 받을 문자 bc
//   app.get(['/abc', '/xyz']) 배열을 사용해도 가능 , regex 도 사용가능 



//Router 사용하기
//main.js
// @ts-checks
const express = require("express")
const fs = require("fs")
const bodyParser = require("body-parser") //npm install body-parser

const userRouter = express.Router() //path pattern이 유사한 경로들 묶어서 처리하기

const app = express()
//app.use(bodyParser.json())    //req.body를 파싱해주는 패키지 사용
app.use(express.json()) //14.16부터 express 자체기능으로 사용 가능

const PORT = 4000

userRouter.get("/", (req, res) => {
  res.send("Get users list")
})

const USERS = {
  15: {
    nickname: "foo",
  },
}

userRouter.param("id", (req, res, next, value) => {
  console.log("id parameter", value) //  users/1235 url요청하면 1235가 value로 오게되고 이 코드가 먼저실행됨.
  // 그 이후에 밑에 userRouter get ID 코드 실행됨.
  // @ts-ignore
  req.user = USERS[value]
  next()
})

userRouter.get("/:id", (req, res) => {
  // /users/:id
  console.log("userRouter get ID")
  // @ts-ignore
  res.send(req.user)
})

userRouter.post("/", (req, res) => {
  res.send("User registered")
})

userRouter.post("/:id/nickname", (req, res) => {
  // req.body: {"nickname": "bar"}
  // @ts-ignore
  const { user } = req
  const { nickname } = req.body

  user.nickname = nickname

  res.send(`User nickname updated: ${nickname}`)
})

app.use("/users", userRouter) // /users 가 공통된 path

app.listen(PORT, () => {
  console.log(`The Express server is listening at port : ${PORT}`)
})
// http POST localhost:4000/15/nickname nickname=bar   요청보내면 USER 데이터 업데이트 










// pug 사용하기 npm install pug
// src폴더안에 views폴더 생성.
// index.pug 파일 생성 
html
    head 
        link(rel="stylesheet" href="/public/index.css")   //css 적용
    body 
        h1 User profile page 
        h2.gold Nickname        //.gold는 classname으로 gold가 오게됨
        div.green.big= nickname //이런식으로 여러개의 classname 생성 가능 
// src폴더안에 public폴더 생성
// index.css 파일생성
body {
  background-color: grey;
}

.gold {
  color: gold;
}

.green {
  color: green;
}

.big {
  font-size: 24px;
}

//main.js
// @ts-check

const express = require("express")
const fs = require("fs")
const bodyParser = require("body-parser")

const userRouter = express.Router() //path pattern이 유사한 경로들 묶어서 처리하기

const app = express()
//app.use(bodyParser.json())    //req.body를 파싱해주는 패키지 사용
app.use(express.json()) //14.16부터 express 자체기능으로 bodyParser 사용 가능
app.use("/public", express.static("src/public")) //static 파일 서빙하기, 첫인자로 /public을 붙여줘야 url에서 users라는 경로로 요청할때
//만약 src폴더에도 users라는 폴더가 있고 15라는 파일이 있을때, 보안상 이슈가 발생하지 않음.

app.set("views", "src/views") //views 폴더가 src폴더에 있을때 이거 설정해줘야함
app.set("view engine", "pug") //pug사용한다는 설정

const PORT = 4000

userRouter.get("/", (req, res) => {
  res.send("Get users list")
})

const USERS = {
  15: {
    nickname: "foo",
  },
}

userRouter.param("id", (req, res, next, value) => {
  console.log("id parameter", value) //  users/1235 url요청하면 1235가 value로 오게되고 이 코드가 먼저실행됨.
  // 그 이후에 밑에 userRouter get ID 코드 실행됨.
  // @ts-ignore
  req.user = USERS[value]
  next()
})

userRouter.get("/:id", (req, res) => {
  // /users/:id
  const resMimeType = req.accepts(["json", "html"])

  if (resMimeType === "json") {
    // @ts-ignore
    res.send(req.user)
  } else if (resMimeType === "html") {
    res.render("index", {
      // @ts-ignore
      nickname: req.user.nickname,  //index.pug와 연결해주는 부분 nickname 변수를 전해줄수 있음.
    })
  }
  console.log("userRouter get ID")
})

userRouter.post("/", (req, res) => {
  res.send("User registered")
})

userRouter.post("/:id/nickname", (req, res) => {
  // req.body: {"nickname": "bar"}
  // @ts-ignore
  const { user } = req
  const { nickname } = req.body

  user.nickname = nickname

  res.send(`User nickname updated: ${nickname}`)
})

app.use("/users", userRouter) // /users 가 공통된 path

app.get("/", (req, res) => {
  res.render("index", {         //pug에서는 res.send가 아닌  res.render를 사용 
    message: "Hello, PUG!",
  })
})

app.listen(PORT, () => {
  console.log(`The Express server is listening at port : ${PORT}`)
})
///

















//에러 핸들링하기 
//src폴더에 routers폴더 생성 후 users.js
// @ts-check
const express = require("express")
const userRouter = express.Router() //path pattern이 유사한 경로들 묶어서 처리하기

userRouter.get("/", (req, res) => {
  res.send("Get users list")
})

const USERS = {
  15: {
    nickname: "foo",
  },
}

userRouter.param("id", async(req, res, next, value) => {
  //만약 async함수로 사용할거면 반드시 try catch문을 사용해야함 
  try{
    console.log("id parameter", value) //  users/1235 url요청하면 1235가 value로 오게되고 이 코드가 먼저실행됨.
    // 그 이후에 밑에 userRouter get ID 코드 실행됨.
  
    // @ts-ignore
    const user = USERS[value]
  
    if (!user) {
      //error 핸들링 : 만약 db에 없는 id값을 url로 찾으면 에러 발생시킴
      const err = new Error("User not found.")
      // @ts-ignore
      err.statusCode = 404
      throw err
    }
  
    // @ts-ignore
    req.user = user
    next()
  }catch(err){
    next(err)
  }
 
})

userRouter.get("/:id", (req, res) => {
  // /users/:id
  const resMimeType = req.accepts(["json", "html"])

  if (resMimeType === "json") {
    // @ts-ignore
    res.send(req.user)
  } else if (resMimeType === "html") {
    res.render("index", {
      // @ts-ignore
      nickname: req.user.nickname,
    })
  }
  console.log("userRouter get ID")
})

userRouter.post("/", (req, res) => {
  res.send("User registered")
})

userRouter.post("/:id/nickname", (req, res) => {
  // req.body: {"nickname": "bar"}
  // @ts-ignore
  const { user } = req
  const { nickname } = req.body

  user.nickname = nickname

  res.send(`User nickname updated: ${nickname}`)
})

module.exports = userRouter


//main.js
// @ts-check

const express = require("express")

const app = express()
app.use(express.json())
app.set("views", "src/views")
app.set("view engine", "pug")

const PORT = 4000

const userRouter = require("./routers/user")

app.use("/users", userRouter)
app.use("/public", express.static("src/public"))

// 인자가 4개면 error핸들링 콜백함수로 인식함, error 발생시 여기서 catch함
app.use((err, req, res, next) => {
  res.statusCode = err.statusCode || 500
  res.send(err.message)
})

app.listen(PORT, () => {
  console.log(`The Express server is listening at port: ${PORT}`)
})
















/// jest 사용해보기 (javascript test package)
// npm install --save-dev jest @types/jest supertest @types/supertest
// src폴더에 app.spec.js 파일 생성 (내가 만들 main.js app의 규격을 미리 규정해 놓는것임.)
// package.json 파일 scripts에 "test": "jest" 추가 / npm run test 하면 app.spec.js파일이 실행됨.

//app.js
// @ts-check

const express = require("express")

const app = express()
app.use(express.json())
app.set("views", "src/views")
app.set("view engine", "pug")

const userRouter = require("./routers/user")

app.use("/users", userRouter)
app.use("/public", express.static("src/public"))

// 인자가 4개면 error핸들링 콜백함수로 인식함, error 발생시 여기서 catch함
app.use((err, req, res, next) => {
  res.statusCode = err.statusCode || 500
  res.send(err.message)
})

module.exports = app


//app.spec.js 
const supertest = require("supertest")
const app = require("./app")

const request = supertest(app)

test("retrieve user json", async () => {
  //expect(1 + 2).toBe(3)
  const result = await request.get("/users/15").accept("application/json")
  console.log(result.body)

  expect(result.body).toMatchObject({
    //json 형식 규정해서, response 온거랑 다르면 test 통과못함.
    nickname: expect.any(String),
  })
  //요청해서 온 result.body가 toMatchObject로 정한 형식과 맞지 않으면 test통과 못함.
})

test("retrieve user page", async () => {
  const result = await request.get("/users/15").accept("text/html")
  console.log(result.text)

  expect(result.text).toMatch(/^<html>.*<\/html>$/) //정규식 표현, html로 시작해서 html로 끝나면 통과
})

test("update nickname", async () => {
  const newNickname = "newNickname"
  const res = await request
    .post("/users/15/nickname")
    .send({ nickname: newNickname })

  expect(res.status).toBe(200)

  const userResult = await request.get("/users/15").accept("application/json")
  expect(userResult.status).toBe(200)
  expect(userResult.body).toMatchObject({
    nickname: newNickname,
  })
})

//main.js
//서버 listen 부분을 분리한 이유는 app.js에 이 부분이 들어가게되면 exports할때 서버가 자동으로 실행되기때문에 test에 영향을 끼침.
// @ts-check
const app = require("./app")

const PORT = 4000

app.listen(PORT, () => {
  console.log(`The Express server is listening at port: ${PORT}`)
})













/// websocket 사용해보기 
// npm install koa koa-pug koa-websocket koa-route koa-static koa-mount tailwindcss
// koa는 express와 같은 웹서버프레임워크이다.
// vscode extension tailwind css 설치

// main.js ( koa 기본 동작)
const koa = require("koa")
const app = new koa()
const Pug = require("koa-pug")
const path = require("path")

new Pug({
  viewPath: path.resolve(__dirname, "./views"), // path.resolve는 이 main.js파일위치를 뜻하는 __dirname 에서 상대경로를 지정해주는 역할.(./views)
  app,
})

app.use(async (ctx, next) => {
  ctx.body = "Hello World"
  await next() // 여기서 next하면 다음 미들웨어로 가게됨.
  ctx.body = `[${ctx.body}]` // 미들웨어 동작이 다 끝나면 다시 돌아와서 이 코드도 실행함. express와의 차이점. express는 next() 다음에 쓴 코드는 실행되지않음.
})

app.use(async (ctx) => {
  ctx.body = `<${ctx.body}>`
})

app.use(async (ctx) => {
  await ctx.render("index")   //koa-pug 역시 send가 아닌 render함수를 사용 
})

app.listen(3000)



// tailwind css setting 
// 작업폴더 안에 tailwind.config.js 파일생성
module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}

//.vscode setting.json 안에 "tailwindCSS.emmetCompletions": true  추가   //tailwind css 자동완성 기능 활성화 




// koa websocket 사용









///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




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

//ejs

//index.js
const express = require('express');
const app = express();
const port = 3000;

//app.set("view engine","pug");
app.set("view engine","ejs");             //ejs 모듈 사용하기
app.use(express.static("public"));
app.use(express.urlencoded({ extended: false }));


app.get('/', (req,res)=>{
    //res.sendFile(__dirname+"/public/index.html")
    res.render("index",{
      text: "hi hongsa"
      arrayData : [1,2,3]
    });
});
//index는 views폴더에 있는 index.ejs 파일을 말함.
// index.ejs에 {} 오브젝트형식으로 데이터를 보낼 수 있음.


app.listen(port, ()=>{
  console.log(`Example app listening on port ${port}`);
});


//index.ejs
<link rel="stylesheet" href="style.css"></link>

<body>
    <h1>ejs start</h1>
    <h3><%= text %></h3>
    <% if (true) {%>
        <h4>참입니다!</h4>
    <%} else {%>
        <h4>거짓입니다!</h4>
    <%} %>

    <% for(let i=0; i < arrayData.length; i++){ %>
        <h2><%= arrayData[i] %></h2>
    <% } %>
</body>
// 이런식으로 <%= text%>  =이 있어야지 text 변수값을 화면상으로 보여줌. 
// <% %>  =이 없으면 저런식으로 js언어에 있는 if문을 쓸수가 있음.
