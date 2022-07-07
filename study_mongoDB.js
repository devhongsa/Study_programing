// mongoDB 에서 구글 로그인 
// 새 데이터베이스 create free 버전으로 
// database로 가서 connect 클릭 후 ,  ip , username, password 설정 
// connect application 누르고 url 복사 

// useNewUrlParser , useUnifiedTopology , and useCreateIndex are true , and useFindAndModify is false   //설정값이 이 값으로 디폴트되었음. 저 세팅옵션들은 이제 없어짐.

// nodejs에서 사용시 

//app.js
const mongoose = require('mongoose');

mongoose.connect(`mongodb+srv://${process.env.mongoUserName}:${process.env.mongoUserPassword}@cluster0.3y6bvww.mongodb.net/?retryWrites=true&w=majority`).then(() => {
    app.listen({port: port}, ()=> {
        console.log('Listening for requests on my awesome port 4000');
    })
}).catch((e)=> console.log("Error:::" + e))





//CRUD 
