//node.green  최근 자바스크립트 표준에 대한 기능들 

//명령어모음.
npm init : package.json 생성
npm install : package.json 파일 및 해당 종속성에 나열된 모든 모듈을 설치
npm install package_name@버전 : 특정 패키지의 특정 버전 설치
npm install 주소 : 특정 저장소 내 패키지 설치. 주로 github을 이와 같이 설치합니다.
npm install package_name -g : 옵션. 글로벌로 설치. 로컬의 다른 프로젝트도 이 패키지를 사용 가능하게 됩니다.
npm uninstall : 패키지 삭제 명령어입니다.
npm update : 설치한 패키지들을 업데이트해줍니다.
npm dedupe : 중복 설치된 패키지들을 정리해주는 명령어입니다.
npm run app.js // js파일 실행시키기 


//노드 버전 관리 패키지
npm install -g n // 노드 버전관리 설치후 터미널에 n 입력후 버전선택 
npm install core-js   // js의 신기능들을 node버전에 상관없이 사용할 수 있는 패키지  require('core-js') 해주고 기능 쓰면됨.

////// prettier vscode 설정법  (formatter) //////
//vscode extension에서 prettier 설치 
npm install --save-dev prettier // js 코드 검사 및 코드정렬 기능   --save-dev는 devDependencies 항목에 기록됨. 릴리즈때는 필요없는 패키지라는 뜻.
//이후 프로젝트 폴더에 .prettierrc 파일 생성 
{
  "semi": false,
  "singleQuote": true
}
// .vscode 폴더 생성후 settings.json 파일 생성 
{
  "[javascript]": {
      "editor.formatOnSave": true,
      "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
} 

///// ESLint /////
//npm install --save-dev eslint
//npm install --save-dev eslint-config-airbnb-base eslint-plugin-import    //airbnb에서 정의한 eslint 설정 
//npm install --save-dev eslint-config-prettier   // prettier가 고친거에 대해서 굳이 오류표시를 하지않음. 
//npm install --save-dev eslint-plugin-node
//작업폴더에 eslintrc.js 파일 생성 
module.exports = {
  extends: ['airbnb-base', 'prettier'],
}
// 만약 ESLint 가 원하지않은 부분을 오류처리한다면 /* eslint-disable-next-line [오류이름]*/   이거를 바로 윗줄에 넣어주면됨. 오류이름을 넣으면 그 오류만 무시함.


/// typescript /// 
npm install --save-dev typescript
npm install --save-dev @types/node 
// 작업폴더에 jsconfig.json 파일 생성 
{
  "compilerOptions": {
      "strict":true         //코드를 더욱 깐깐하게 보겠다
  },
  "include":[
      "src/**/*"            //src에 있는 모든 파일에 적용 
  ]
}
//구글에 jsconfing.json 치면 레퍼런스 잘 나와있음. 참고 

// js파일에서 맨윗줄에 // @ts-check  넣어서 사용 


//
//package-lock.json 파일도 깃에 같이 올려주는것이 좋음. 다른사람과 협업시 버전차이로 인한 오류를 방지할 수 있음.
//npm install시 npm이 package-lock.json 파일을 보고 우선적으로 모듈을 설치함. 그리고 이파일에 실제 내가 설치한 버전이 나와있음.

//Cannot use import statement outside a module
//package.json에 "type":"module"  써 넣으면 해결됨.

//cmd에서 node -v 버전확인
//node 명령어 node 시작
console.log(1+1);   //2 
//Ctrl + C 2번입력 node 종료
// node main.js          노드야 main.js 파일 실행시켜라
// dir/w    node syntax\Number.js      현재 디렉토리에서 syntax폴더에 있는 Number.js를 실행시켜라
// cd 디렉토리이름      폴더이동 
// cd ..               뒤로이동
// dir                 현재디렉토리에 뭐가있는지

//npm root -g               //전역설치시 설치경로 
//npm install pm2 -g        //여기서 -g는 컴퓨터어디에서는 pm2가 실행가능해야된다는 의미?
//pm2 start main.js         // js 파일 실행시키기 (서버가동)
//pm2 monit                 // 현재 실행되고 있는 서버 상세정보들.   Q버튼 누르면 다시 명령어 입력창으로 돌아감.
//pm2는 프로그램이 꺼져도 자동으로 재시작해줌.
//pm2 list                  // 현재 실행되고 있는 서버 간략리스트
//pm2 stop main             // main.js 종료  
//pm2 start main.js --watch  // main.js를 수정할때마다 자동으로 껐다 켜줌.
//pm2 log                   //error 사항들 보여줌.
//touch main.js             // main.js 파일 만들기.

//writehead 200: 성공했다 , 403: 이페이지는 없다. 302: 다른페이지로 가라 301: 이페이지는 다른페이지로 바뀌었다.



////////////////////////// nodejs에서 postgresql db연동. //////////////////////////
npm install pg 

const { Client } = require("pg")

async function main() {
  const client = new Client({
    user: "",
    password:
      "",
    database: "",
    host: "",
    port: 5432,
    ssl: {
      rejectUnauthorized: false,          //localhost가 아닌경우 이거 넣어줘야함 .
    },
  })
  await client.connect()
  const res = await client.query("SELECT $1::text as message", ["Hello world!"])
  console.log(res.rows[0].message) // Hello world!
  await client.end()
}

main()
// 터미널에서 디비 접속 psql -U [username] -d [dbname] -h [host] --password


//nodejs에서 기본 CRUD 
const { Client } = require("pg")
const program = require("commander")
const prompts = require("prompts")

async function connect() {
  const client = new Client({
    user: "",
    password:
      "",
    database: "",
    host: "",
    port: 5432,
    ssl: {
      rejectUnauthorized: false,
    },
  })
  await client.connect()
  const res = await client.query("SELECT $1::text as message", ["Hello world!"])
  console.log(res.rows[0].message) // Hello world!
  return client
}

program.command("add").action(async () => {
  const client = await connect()
  const userName = await prompts({
    type: "text",
    name: "userName",
    message: "Provide a user name to insert",
  })

  //const query = `INSERT INTO public.userfollow (uid) VALUES ('${userName.userName}')`
  const query = `INSERT INTO public.userfollow (uid) VALUES ($1::text)`
  await client.query(query, [userName.userName])

  await client.end()
})

program.command("remove").action(async () => {
  const client = await connect()
  const userName = await prompts({
    type: "text",
    name: "userName",
    message: "Provide a user name to delete",
  })

  //const query = `DELETE FROM public.userfollow WHERE uid = '${userName.userName}'`
  const query = `DELETE FROM public.userfollow WHERE uid = $1::text` //사용자의 입력으로 의도하지 않은 쿼리문이 실행되는 것을 방지하기위해

  await client.query(query, [userName.userName])

  await client.end()
})

program.command("list").action(async () => {
  const client = await connect()

  const query = `SELECT * FROM public.userfollow`
  const result = await client.query(query)
  console.log(result)

  await client.end()
})

program.parseAsync()


////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////// nodejs에서 postgresql db스키마 관리, 마이그레이션 //////////////////////////
https://sequelize.org/docs/v6/core-concepts/model-querying-basics/
////////////////////////// sequelize //////////////////////////
npm install sequelize sequelize-cli
scripts에 "seq" : "sequelize-cli" 추가 
npm run seq init 입력 
config 폴더에 config.json 내용 수정 
{
  "development": {
    "username": "",
    "password": "",
    "database": "",
    "host": "",
    "dialect": "postgres",
    "port": 5432,
    "dialectOptions": {
      "ssl": { "rejectUnauthorized": false }
    }
  }
}
npx sequelize-cli migration:generate --name initialize
OR  npm run seq -- migration:generate --name add-cities

migrations 폴더에 생성된 파일에서 up down 마이그레이션 코드 작성
npm run seq db:migrate   // up 
npm run seq db:migrate:undo // down 

//template literal
// 템플릿 리터럴은 ~표시 밑에 있는 ` 이걸로 표현하며, 문자열안에서 \n 으로 줄바꿈 안하고, enter를 쳐도 줄바꿈 표현 가능.
// 또한 ${} 를 통해 문자열 안에서 변수 투입가능  기존 문자열이면 ' +name+ ' 이런식으로 넣어줬어야 함.
var name = "hongsa";
var letter = `Lorem ipsum dolor sit amet, ${name} ${1+1}
consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.`


//URL

// http://opentutorials.org:3000/main?id=HTML&page=12 
//http : hypertext transfer protocol의 약자이다. http는 웹서버와 웹브라우저가 서로 통신하기위해 만들어진 규칙
//opentutorials.org : host(domain) 이라고 한다. 인터넷에 연결되어 있는 컴퓨터의 주소.IP
//3000 : port번호이다. 1대의 컴퓨터안에 여러개의 서버가 존재할 수 있다. 그러므로 서버 port번호를 통해 어떤 서버에 접속할건지를 정하는것. default는 80이다.
//main : Path이다. 어떤 디렉토리에 어떤html파일을 불러올것인가.
//?id=HTML&page=12 : query string이다.  main이라는 html에서 어떤 부분을 불러올 것인가라는 정보. ?으로 시작하고, 값과 값은 &로 연결하기로 되어있다.


// hoisting?
// 함수선언, 변수 선언이 코드에 어느 줄에 위치해있던지 맨위에 선언된걸로 치는 것


//nodejs에서 파일은 모듈을 의미함 . 파일 밑에 module.exports = 함수나 변수 등  써놓으면 다른 파일에서 사용가능 
//package.json 에서 패키지 버전정보에서 ^3.2.0  처럼 꺽새표시를 하면  npm update했을때 major 버전은 업데이트하지않고 minor버전을 최신업데이트함.
// ^ 말고 ~ 하면 patch 버전의 최신버전을 업데이트함.

// eslint 깔고, package.json  scripts에 "lint":"eslint src/**/*"  넣고, npm run lint 하면, 에러들을 잡아줌 

// npm install -g yarn
// yarn add 패키지이름
// yarn remove 패키지이름 
// yarn add -D 패키지이름  =  npm install --save-dev


// nodejs convention 컨벤션 
// 파일이름은 소문자, _, - 3개만 쓰도록 한다. 대문자로 쓰게되면 여러문제 발생할 수 있음. javascript는 모듈 require할때 대소문자 구분없이 require해주지만 이로인한 문제 발생.

// buffer?
const fs = require("fs")

const result = fs.readFileSync("src/test")

console.log(result)

//utf-8 인코딩을 사용하지 않으면 16진수 buffer값이 출력됨.
// 1 byte = 8 bit, 0 이상 255이하의 값          0 ~ 2^8-1

const buf = Buffer.from([97, 98, 99, 100, 101]) //리스트에 10진수 아스키코드 넣어야함.
console.log(buf)

console.log(buf.compare(result)) // 0이 나오면 완전히 같은 내용이라는 뜻, 1이나 -1 나오면 다른 buffer

// stream? 
// 기본 form
// const fs = require("fs")
// const rs = fs.createReadStream("test", { encoding: "utf-8" })

// rs.on("data", (data) => {
//   // do something with data
//   // encoding 설정 안해주면 data가 버퍼로 떨어짐.
// })

// rs.on("error", (error) => {})
// rs.on("end", () => {})


// 스트림 큰 파일 처리하기 



// github 레포 참고 

// nodejs 내장객체
// __dirname : 이걸 쓴 파일이 있는 폴더위치 , __filename : 이걸 쓴 파일의 위치 
// process
// setInterval : 일정시간 간격마다 실행해라 , setTimeout : 일정시간 후에 실행해라 
// clearInterval

let count = 0
const handle = setInterval(() => {
  console.log('Interval')
  count += 1 

  if (count == 4){
    console.log('done!')
    clearInterval(handle)
  }
}, 1000)

/// 스탠다드 라이브러리 

const os = require('os')
os.arch()          // 32비트 64비트 
os.platform()     //platform 리눅스 윈도우 
os.cpus()         //cpu 정보

//// child_process    : 파이썬 멀티프로세스랑 같은거 
//dns 
//Path



























var http = require('http');
var fs = require('fs');
var url = require('url');
//사이트 도메인에 localhost:3000/?id=HTML 입력한상태
var app = http.createServer(function(request,response){
    var _url = request.url;                        // _url = /?id=HTML
    var querydata = url.parse(_url, true).query;  // _url 부분을 query로 파싱 { id : 'HTML'}
    console.log(querydata.id);                    // querydata에서 id 부분 출력 // HTML 출력 
    if(_url == '/'){
      _url = '/index.html';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    response.end(fs.readFileSync(__dirname + _url));  //서버컴퓨터에 저장된 html파일 읽어오는 부분.  respond.end('string') 이렇게하면 그냥 화면에 string 출력
});
app.listen(3000);


//동적 웹페이지 만들기
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var title = querydata.id;
    console.log(title);
    
    if(_url == '/'){
      title = 'Welcome';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        <li><a href="/?id=HTML">HTML</a></li>
        <li><a href="/?id=CSS">CSS</a></li>
        <li><a href="/?id=JavaScript">JavaScript</a></li>
      </ol>
      <h2>${title}</h2>
      <p><a href="https://www.w3.org/TR/html5/" target="_blank" title="html5 speicification">Hypertext Markup
        Language (HTML)</a> is the standard markup language for <strong>creating <u>web</u> pages</strong>
        and web applications.Web browsers receive HTML documents from a web server or from local storage and
        render them into multimedia web pages. HTML describes the structure of a web page semantically and
        originally included cues for the appearance of the document.
      <img src="coding.jpg" width="100%">
      </p>
      <p style="margin-top:45px;">HTML elements are the building blocks of HTML pages.
        With HTML constructs, images and other objects, such as interactive forms, may be embedded into
        the rendered page. It provides a means to create structured documents by denoting structural
        semantics for text such as headings, paragraphs, lists, links, quotes and other items.
        HTML elements are delineated by tags, written using angle brackets.
      </p>
    </body>
    </html>
    `;
    response.end(template);
});
app.listen(3000);

// 파일 읽기
var fs = require('fs');
fs.readFile('sample.txt','utf8', function(err,data){      //여기서 data는 sample.txt 의 내용 
  console.log(data);
});

//최종 
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var title = querydata.id;
    console.log(title);
    
    if(_url == '/'){
      title = 'Welcome';
    }
    if(_url == '/favicon.ico'){
      return response.writeHead(404);
    }
    response.writeHead(200);
    fs.readFile(`data/${title}`,'utf8', function(err,description){      //readFile 함수 안에 html 내용 들어가야됨.
      var template = `
    <!doctype html>
    <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ol>
        <li><a href="/?id=HTML">HTML</a></li>
        <li><a href="/?id=CSS">CSS</a></li>
        <li><a href="/?id=JavaScript">JavaScript</a></li>
      </ol>
      <h2>${title}</h2>
      <p>${description}</p>
    </body>
    </html>
    `;
    response.end(template);
    });
});
app.listen(3000);


//not found 404
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;
    var title = querydata.id;
    
    if(pathname === '/'){
      if(querydata.id === undefined){
          var title = 'Welcome';
          var description = 'Hello, Node.js';
          var template = `
          <!doctype html>
          <html>
          <head>
            <title>WEB1 - ${title}</title>
            <meta charset="utf-8">
          </head>
          <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
              <li><a href="/?id=HTML">HTML</a></li>
              <li><a href="/?id=CSS">CSS</a></li>
              <li><a href="/?id=JavaScript">JavaScript</a></li>
            </ol>
            <h2>${title}</h2>
            <p>${description}</p>
          </body>
          </html>
          `;
          response.writeHead(200);
          response.end(template);
      }
      else {
        fs.readFile(`data/${title}`,'utf8', function(err,description){      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
          var template = `
        <!doctype html>
        <html>
        <head>
          <title>WEB1 - ${title}</title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="/">WEB</a></h1>
          <ol>
            <li><a href="/?id=HTML">HTML</a></li>
            <li><a href="/?id=CSS">CSS</a></li>
            <li><a href="/?id=JavaScript">JavaScript</a></li>
          </ol>
          <h2>${title}</h2>
          <p>${description}</p>
        </body>
        </html>
        `;
        response.writeHead(200);
        response.end(template);
        });
       }
      }
    
    else {
    response.writeHead(404);
    response.end('Not Found');
    }
});

app.listen(3000);

//폴더 읽기
var testFolder = './data';
var fs = require('fs');

fs.readdir(testFolder, function(error, filelist){
  console.log(flielist);
})
//return ['CSS','HTML','JavaScript']


//list 생성 자동화 
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용
var qs = require('querystring') //data 수신해서 쓰기위한 모듈.

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    function templateHTML(title, list, description){
      return `
            <!doctype html>
            <html>
            <head>
              <title>WEB1 - ${title}</title>
              <meta charset="utf-8">
            </head>
            <body>
              <h1><a href="/">WEB</a></h1>
              ${list}
              <a href="/create">create</a>
              <h2>${title}</h2>
              <p>${description}</p>
            </body>
            </html>
            `;
    }

    function templateList(filelist){
      var list = '<ul>';
      var i = 0;
      while(i < filelist.length){
        list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
        i = i + 1;
      }
      list = list + '</ul>';
      return list;
    }
   
    if(pathname === '/'){
      if(querydata.id === undefined){
        fs.readdir('./data', function(error, filelist){
          var title = 'Welcome';
          var description = 'Hello, Node.js';
          var list = templateList(filelist);
          var template = templateHTML(title,list,description);
            response.writeHead(200);
            response.end(template);
        })
      }
      else {
        fs.readdir('./data', function(error, filelist){
          fs.readFile(`data/${querydata.id}`,'utf8', function(err,description){
            var title = querydata.id;
            var list = templateList(filelist);      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
            var template = templateHTML(title,list,description);
          response.writeHead(200);
          response.end(template);
          });
        });
       }
      }
    else if(pathname === '/create'){              // create버튼 눌렀을때 나오는 html 페이지 설정.
      fs.readdir('./data', function(error, filelist){
        var title = 'WEB - create';
        var description = `<form action="http://localhost:3000/create_process" method="post">       
        <p><input type="text" name="title" placeholder="title"></p>
        <p>
          <textarea name="description" placeholder="text"></textarea>
        </p>
        <p>
          <input type="submit">
        </p>
        </form>
        `;   //action에서의 주소는 submit을 눌렀을때 /create_process 페이지로 넘어가고 여기에 input 정보를 보냄.
        var list = templateList(filelist);
        var template = templateHTML(title,list,description);
        response.writeHead(200);
        response.end(template);
      })
    }
    else if(pathname === '/create_process'){      //submit을 눌렀을때 /create_process로 넘어오게되고 이페이지를 설정
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var title = post.title;             //이렇게 post 쿼리스트링으로 변환된 데이터를 변수에 저장해서 사용가능.
        var description = post.description;
        fs.writeFile(`data/${title}`,description, 'utf8', function(err){        //파일만들고 쓰는 작업.
          response.writeHead(302, {Location: `/?id=${title}`});                 // 다른페이지로 이동해라.
          response.end();
        })
      });
    }
    
    else {
    response.writeHead(404);
    response.end('Not Found');
    }
});

app.listen(3000);


// 비동기 vs 동기
//readFileSync
console.log('A');
var result = fs.readFileSync('syntax/sample.txt', 'utf8');    //동기 return이 있기 때문에 변수에 넣는것이 가능.
console.log(result);
console.log('C');
//결과 : A B C 출력 , 동기이기때문에 파일을 읽어오고 변수에 넣을때까지 기다림 

//readFile
console.log('A');
fs.readFile('syntax/sample.txt', 'utf8', function(err, result){     //비동기는 return이 없기때문에 변수에 넣는것불가능. 
  console.log(result);
});
console.log('C');
// 결과 : A C B 출력 , 비동기이기때문에 파일을 읽어오라고 시킨후 바로 다음코드로 넘어가고, 응답이오면 그때 콜백함수가 실행됨.


//promises.readFile 
async function main() {
  const result = await fs.promises.readFile('syntax/sample.txt', 'utf-8')
  console.log(result)
}
main() 
// 현재는 promises.readFile만 써도 전혀 문제가 되지 않음 . 이거쓰면 좋음.




//콜백함수

var a = function(){console.log('a');}

function func(callback){
  console.log('b');
  callback();
}

func(a);


//npm(node package manager)과 PM2 패키지

//npm install pm2 -g        //여기서 -g는 컴퓨터어디에서는 pm2가 실행가능해야된다는 의미?
//pm2 start main.js         // js 파일 실행시키기 (서버가동)
//pm2 monit                 // 현재 실행되고 있는 서버 상세정보들.   Q버튼 누르면 다시 명령어 입력창으로 돌아감.
//pm2는 프로그램이 꺼져도 자동으로 재시작해줌.
//pm2 list                  // 현재 실행되고 있는 서버 간략리스트
//pm2 stop main             // main.js 종료  
//pm2 start main.js --watch  // main.js를 수정할때마다 자동으로 껐다 켜줌.
//pm2 log                   //error 사항들 보여줌.


//HTML form
/* 
  <form action="http://localhost:3000/process_create" method="post">   //만약 method없이 보내면 url에 input정보들이 쿼리스트링으로 바껴서 보내짐.
  <p><input type="text" name="title"></p>                             //name을 정해주고 보내줘야 서버에서 데이터를 받아서 사용할 수 있음.
  <p>
    <textarea name="description"></textarea>
  </p>
  <p>
    <input type="submit">
  </p>
</form> 
*/

//정보생성, 업데이트
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용
var qs = require('querystring') //data 수신해서 쓰기위한 모듈.

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    function templateHTML(title, list, description, control){
      return `
            <!doctype html>
            <html>
            <head>
              <title>WEB1 - ${title}</title>
              <meta charset="utf-8">
            </head>
            <body>
              <h1><a href="/">WEB</a></h1>
              ${list}
              ${control}
              <h2>${title}</h2>
              <p>${description}</p>
            </body>
            </html>
            `;
    }

    function templateList(filelist){
      var list = '<ul>';
      var i = 0;
      while(i < filelist.length){
        list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
        i = i + 1;
      }
      list = list + '</ul>';
      return list;
    }
   
    if(pathname === '/'){
      if(querydata.id === undefined){
        fs.readdir('./data', function(error, filelist){
          var title = 'Welcome';
          var description = 'Hello, Node.js';
          var list = templateList(filelist);
          var template = templateHTML(title,list,description,
            `<a href="/create">create</a>`);
            response.writeHead(200);
            response.end(template);
        })
      }
      else {
        fs.readdir('./data', function(error, filelist){
          fs.readFile(`data/${querydata.id}`,'utf8', function(err,description){
            var title = querydata.id;
            var list = templateList(filelist);      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
            var template = templateHTML(title,list,description,
              `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`);
          response.writeHead(200);
          response.end(template);
          });
        });
       }
      }
    else if(pathname === '/create'){              // create버튼 눌렀을때 나오는 html 페이지 설정.
      fs.readdir('./data', function(error, filelist){
        var title = 'WEB - create';
        var description = `<form action="/create_process" method="post">       
        <p><input type="text" name="title" placeholder="title"></p>
        <p>
          <textarea name="description" placeholder="text"></textarea>
        </p>
        <p>
          <input type="submit">
        </p>
        </form>
        `;   //action에서의 주소는 submit을 눌렀을때 /create_process 페이지로 넘어가고 여기에 input 정보를 보냄.
        var list = templateList(filelist);
        var template = templateHTML(title,list,description,'');
        response.writeHead(200);
        response.end(template);
      })
    }
    else if(pathname === '/create_process'){      //submit을 눌렀을때 /create_process로 넘어오게되고 이페이지를 설정
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var title = post.title;             //이렇게 post 쿼리스트링으로 변환된 데이터를 변수에 저장해서 사용가능.
        var description = post.description;
        fs.writeFile(`data/${title}`,description, 'utf8', function(err){        //파일만들고 쓰는 작업.
          response.writeHead(302, {Location: `/?id=${title}`});                 // 다른페이지로 이동해라.
          response.end();
        })
      });
    }
    else if(pathname === '/update'){          //update 눌렀을때 페이지에 뭐 띄울건지 
      fs.readdir('./data', function(error, filelist){
        fs.readFile(`data/${querydata.id}`,'utf8', function(err,description){
          var title = querydata.id;
          var list = templateList(filelist);      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
          var template = templateHTML(title,list,
            `
            <form action="/update_process" method="post">
            <input type="hidden" name="id" value="${title}">
            <p><input type="text" name="title" placeholder="title" value=${title}></p>    
            <p>
              <textarea name="description" placeholder="text">${description}</textarea>
            </p>
            <p>
              <input type="submit">
            </p>
            </form>
            `,
            `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`);   //input태그 type의 hidden은 화면에 출력x
        response.writeHead(200);
        response.end(template);
        });
      });
    }
    else if(pathname === '/update_process'){    //수정된 정보를 업데이트하는 과정
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var id = post.id;                   //파일제목이 수정되기 전 파일제목.
        var title = post.title;             //수정된 파일제목
        var description = post.description; //수정한 파일내용
        fs.rename(`data/${id}`,`data/${title}`, function(error){                  
          fs.writeFile(`data/${title}`,description, 'utf8', function(err){        //수정된 제목과 내용들 업데이트
            response.writeHead(302, {Location: `/?id=${title}`});                 // 다른페이지로 이동해라.
            response.end();
          })
        })
        console.log(post);
      });
    }
    
    else {
    response.writeHead(404);
    response.end('Not Found');
    }
});

app.listen(3000);


//파일삭제하기
var http = require('http');     // http 모듈 사용
var fs = require('fs');         //file system 모듈 사용
var url = require('url');       //url 모듈 사용
var qs = require('querystring') //data 수신해서 쓰기위한 모듈.

var app = http.createServer(function(request,response){
    var _url = request.url;
    var querydata = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    function templateHTML(title, list, description, control){
      return `
            <!doctype html>
            <html>
            <head>
              <title>WEB1 - ${title}</title>
              <meta charset="utf-8">
            </head>
            <body>
              <h1><a href="/">WEB</a></h1>
              ${list}
              ${control}
              <h2>${title}</h2>
              <p>${description}</p>
            </body>
            </html>
            `;
    }

    function templateList(filelist){
      var list = '<ul>';
      var i = 0;
      while(i < filelist.length){
        list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
        i = i + 1;
      }
      list = list + '</ul>';
      return list;
    }
   
    if(pathname === '/'){
      if(querydata.id === undefined){
        fs.readdir('./data', function(error, filelist){
          var title = 'Welcome';
          var description = 'Hello, Node.js';
          var list = templateList(filelist);
          var template = templateHTML(title,list,description,
            `<a href="/create">create</a>`);
            response.writeHead(200);
            response.end(template);
        })
      }
      else {
        fs.readdir('./data', function(error, filelist){
          fs.readFile(`data/${querydata.id}`,'utf8', function(err,description){
            var title = querydata.id;
            var list = templateList(filelist);      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
            var template = templateHTML(title,list,description,
              `<a href="/create">create</a> <a href="/update?id=${title}">update</a> 
              <form action="delete_process" method="post">
                <input type="hidden" name="id" value="${title}">
                <input type="submit" value="delete">
              </form>`);
              //무언가를 삭제하는거는 링크로 만들면 절대안됨.!! 그 링크를 따라 들어가면 delete버튼을 안눌러도 지울수 있기때문 그래서 form으로 만들어야함.
              
          response.writeHead(200);
          response.end(template);
          });
        });
       }
      }
    else if(pathname === '/create'){              // create버튼 눌렀을때 나오는 html 페이지 설정.
      fs.readdir('./data', function(error, filelist){
        var title = 'WEB - create';
        var description = `<form action="/create_process" method="post">       
        <p><input type="text" name="title" placeholder="title"></p>
        <p>
          <textarea name="description" placeholder="text"></textarea>
        </p>
        <p>
          <input type="submit">
        </p>
        </form>
        `;   //action에서의 주소는 submit을 눌렀을때 /create_process 페이지로 넘어가고 여기에 input 정보를 보냄.
        var list = templateList(filelist);
        var template = templateHTML(title,list,description,'');
        response.writeHead(200);
        response.end(template);
      })
    }
    else if(pathname === '/create_process'){      //submit을 눌렀을때 /create_process로 넘어오게되고 이페이지를 설정
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var title = post.title;             //이렇게 post 쿼리스트링으로 변환된 데이터를 변수에 저장해서 사용가능.
        var description = post.description;
        fs.writeFile(`data/${title}`,description, 'utf8', function(err){        //파일만들고 쓰는 작업.
          response.writeHead(302, {Location: `/?id=${title}`});                 // 다른페이지로 이동해라.
          response.end();
        })
      });
    }
    else if(pathname === '/update'){          //update 눌렀을때 페이지에 뭐 띄울건지 
      fs.readdir('./data', function(error, filelist){
        fs.readFile(`data/${querydata.id}`,'utf8', function(err,description){
          var title = querydata.id;
          var list = templateList(filelist);      //readFile 함수 안에 html 내용 들어가야됨. description에는 파일읽은내용들어감.
          var template = templateHTML(title,list,
            `
            <form action="/update_process" method="post">
            <input type="hidden" name="id" value="${title}">
            <p><input type="text" name="title" placeholder="title" value=${title}></p>    
            <p>
              <textarea name="description" placeholder="text">${description}</textarea>
            </p>
            <p>
              <input type="submit">
            </p>
            </form>
            `,
            `<a href="/create">create</a> <a href="/update?id=${title}">update</a>`);   //input태그 type의 hidden은 화면에 출력x
        response.writeHead(200);
        response.end(template);
        });
      });
    }
    else if(pathname === '/update_process'){    //수정된 정보를 업데이트하는 과정
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var id = post.id;                   //파일제목이 수정되기 전 파일제목.
        var title = post.title;             //수정된 파일제목
        var description = post.description; //수정한 파일내용
        fs.rename(`data/${id}`,`data/${title}`, function(error){                  
          fs.writeFile(`data/${title}`,description, 'utf8', function(err){        //수정된 제목과 내용들 업데이트
            response.writeHead(302, {Location: `/?id=${title}`});                 // 다른페이지로 이동해라.
            response.end();
          })
        })
        console.log(post);
      });
    }
    else if(pathname === '/delete_process'){
      var body = ''
      request.on('data', function(data){
        body += data;
        if (body.length > 1e6){                   //너무 많은 데이터는 html이 수용할 수 없기때문에 예외처리
          request.connection.destroy();}
      });
      request.on('end', function(){
        var post = qs.parse(body);          //body를 쿼리스트링으로 변환.
        var id = post.id
        fs.unlink(`data/${id}`, function(err){        // 파일 삭제 
          response.writeHead(302, {Location:`/`});
          response.end();
        })
      });
    }
    
    else {
    response.writeHead(404);
    response.end('Not Found');
    }
});

app.listen(3000);



//refactoring
//각자 존재했던 function들을 비슷한 기능을하는 function 끼리 모아서 객체에 모아놓는다.
var template = {
  HTML: function(){},
  list: function(){},
};

template.HTML();
template.list();



//module//

//mpart.js 파일에서 작성
var M = {
  v:'v',
  f:function(){
    console.log(this.v);
  }
}

module.exports = M;
//혹은
module.exports = {
  v:'v',
  f:function(){
    console.log(this.v);
  }
}

//muse.js 파일에서 사용
var part = require('./mpart.js');   //mpart.js와 muse.js가 같은 위치에 있을때.  ./  사용
console.log(part); //{v:'v', f:[Function: f]}
part.f(); //v 


//보안//

//만약 사용자가 url에 ../ 이런식으로 기입해서 서버컴퓨터의 파일, 폴더들을 탐색하면, 컴퓨터가 털리기때문에
// ../ 이런걸 입력해도 서버컴퓨터를 탐색하지못하게 해야됨.

var path = require('path');

var filteredId = path.parse(queryData.id).base; // queryData.id 파일 분석. base는 ../ 이런 경로설정 명령어를 빼고 파일이름만 추출.
fs.readFile(`data/${filteredId}`, ...)          // 그러면 사용자가 url을 통해 서버컴퓨터의 폴더를 탐색하고 다닐 수 없게됨.


// 외부 package 사용하기// 

//프로젝트 폴더안에서 npm init 명령어 실행 //
//package.json 파일 생김.
//npm install -s sanitize-html   명령어 실행. 여기서 -s는 -g과는 다르게 이프로젝트에서만 쓰는 package로 설정.
//node_modules 폴더 생기고, package-lock.json 파일생김.. 
//package.json에서 dependencies 라는 key가 생기는데 이는 나의 프로젝트가 의존하는 package들의 정보가 들어가게된다.
//node_modules 폴더에 가면 sanitize-html 뿐만 아니라 다른 package도 많이 생기는데 이것들은 모두 sanitize-html의 의존관계에 있는 package들이 설치된거.

//만약 다른환경에서 실행해야될 경우 package.json이랑 package-lock.json만 옮기고나서, npm install 명령어 실행하면 모든 디펜던시 알아서 설치하게됨.




// API (Application Programing Interface) //

var http = require('http');

var app = http.createServer(function(request, response){});
//웹브라우저에서 서버로 요청한 데이터(request)
//웹서버가 웹브라우저로 응답한 데이터(response)

app.listen(3000);


//node.js AWESOME    핫한 모듈들 




const path = require('path');
path.resolve("path","path2","path3");     //패스경로를 합쳐서 스트링으로 만들어줌. join도 같은역할



// util // 

const util = require('util')
const { config } = require("process")

console.log(util.inspect(objectname,{depth:5}));      //nodejs에서 출력할때, object가 생략되는것을 보이게 할 수 있음.
