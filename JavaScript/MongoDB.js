// mongoDB 에서 구글 로그인 
// 새 데이터베이스 create free 버전으로 
// database로 가서 connect 클릭 후 ,  ip , username, password 설정 
// connect application 누르고 url 복사 

// useNewUrlParser , useUnifiedTopology , and useCreateIndex are true , and useFindAndModify is false   //설정값이 이 값으로 디폴트되었음. 저 세팅옵션들은 이제 없어짐.

// nodejs에서 사용시 

//app.js
const mongoose = require('mongoose');
const {MongoClient} =  require('mongodb')

mongoose.connect(`mongodb+srv://${process.env.mongoUserName}:${process.env.mongoUserPassword}@cluster0.3y6bvww.mongodb.net/?retryWrites=true&w=majority`).then(() => {
    app.listen({port: port}, ()=> {
        console.log('Listening for requests on my awesome port 4000');
    })
}).catch((e)=> console.log("Error:::" + e))

// or

const uri = `mongodb+srv://${config.env.mongoUserName}:${config.env.mongoUserPassword}@cluster0.3y6bvww.mongodb.net/${config.env.mongoDatabase}?retryWrites=true&w=majority`
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})

module.exports = client


//CRUD 
async function main() {
    await client.connect()
  
    //Create
    const users = client.db("fc22").collection("users") //존재하지않는 db,컬렉션이라도 자동으로 생성함
  
    //Delete
    await users.deleteMany()
  
    //Create
    await users.insertMany([
      {
        name: "Foo",
        birthYear: 2000,
      },
      {
        name: "Boo",
        birthYear: 1995,
      },
      {
        name: "Doo",
        birthYear: 2001,
      },
    ])
  
    //Update
    await users.updateOne(
      {
        name: "Boo",
      },
      {
        $set: {
          name: "Baza",
        },
      }
    )
  
    await users.deleteOne({
      name: "Foo",
    })
  
    //Read
    const cursor = users.find(
      {
        birthYear: {
          $gte: 1994, //1994 보다 큰
        },
      },
      {
        sort: {
          birthYear: -1, //내림차순 정렬
        },
      }
    )
    await cursor.forEach(console.log)
  
    await client.close()
  }
  
  main()