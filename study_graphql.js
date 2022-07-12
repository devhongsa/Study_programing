// 작업폴더 
// npm init 
// npm install express 
// npm install graphql express-graphql 
// npm install nodemon -g 
// npm install lodash
// npm install mongoose   // mongoDB 사용시 
// npm install cors 
// 작업 폴더에서 app.js 폴더 생성 
// server 폴더 생성 
// server 폴더에서 shcema 폴더생성후 schema.js 파일 생성 

//graphql query 문 

// query{
//     user(id:1){
//       id
//       name
//       age
//       profession
//       posts{
//         comment
//       }
//     }
//     hobby(id:1){
//       title
//       description
//       user{
//         age
//         name
//       }
//     }
//   }
  
// mutation{
//     createUser(name:"Hongsa", age:31, profession:"Developer"){
//       name
//       age
//       profession
//     }
    
//     createPost(comment:"hi hongsa", userId: 13){
//       comment
//       user{
//         name
//       }
//     }
    
//     createHobby(title: "Playing Guitar", description: "have fun with..",userId:13){
//       title
//       user{
//         name
//       }
//     }
//   }



////// app.js //////.
const express = require('express');
const {graphqlHTTP} = require('express-graphql');
const schema = require('./schema/schema');

const app = express();
app.use('/graphql', graphqlHTTP({
    graphiql:true,
    schema: schema
}))

app.listen(4000, ()=> {
    console.log('Listening for requests on my awesome port 4000');
})

/////  schema.js //////////
const graphql = require('graphql');
var _ = require('lodash');

//dummy data
let usersData = [
    {id: '1', name: 'Bond', age:36, profession:'Programmer'},
    {id: '13', name: 'Anna', age:26, profession:'Baker'},
    {id: '211', name: 'Bella', age:16, profession:'Mechanic'},
    {id: '19', name: 'Gina', age:26, profession:'Painter'},
    {id: '150', name: 'Georgina', age:36, profession:'Doctor'},
]
let hobbiesData = [
    {id: '1', title: 'Programing', description: 'Using', userId: '1'},
    {id: '2', title: 'Rowing', description: 'Sweat', userId: '13'},
    {id: '3', title: 'Swimming', description: 'Get', userId: '211'},
    {id: '4', title: 'Fencing', description: 'Hobby', userId: '19'},
    {id: '5', title: 'Hiking', description: 'Wear', userId: '150'},
]

let postsData = [
    {id: '1', comment: 'Building', userId: '1'},
    {id: '2', comment: 'GraphQL', userId: '13'},
    {id: '3', comment: 'How to change the world!', userId: '211'},
    {id: '4', comment: 'How to change the world!', userId: '1'},
    {id: '5', comment: 'How to change the world!', userId: '150'},
]

const {
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLList,
    GraphQLID,
    GraphQLString,
    GraphQLInt,
} = graphql

//Create types 
const UserType = new GraphQLObjectType({
    name: 'User',
    description: 'Documentation for user...',
    fields: () => ({
        id: {type:GraphQLID},
        name: {type:GraphQLString},
        age: {type:GraphQLInt},
        profession: {type:GraphQLString},

        posts:{
            type: new GraphQLList(PostType),
            resolve(parent, args){
                return _.filter(postsData, {userId: parent.id})         // postsData의 userId가 usersData의 id인 데이터 리스트로 리턴, type이 GraphQLList 이여야함.
            }
        },

        hobbies: {
            type: new GraphQLList(HobbyType),
            resolve(parent, args){
                return _.filter(hobbiesData, {userId: parent.id})
            }
        }
    })
})

const HobbyType = new GraphQLObjectType({
    name: 'Hobby',
    description: 'Hobby description',
    fields: () => ({
        id: {type:GraphQLID},
        title: {type: GraphQLString},
        description: {type:GraphQLString},
        user: {
            type: UserType,
            resolve(parent, args){
                return _.find(usersData, {id:parent.userId})            // usersData의 id가 postsData의 userId인 데이터 리턴
            }
        }
    })
})

const PostType = new GraphQLObjectType({
    name:'Post',
    description: 'Post description',
    fields: () => ({
        id: {type:GraphQLID},
        comment: {type:GraphQLString},
        user: {
            type: UserType,
            resolve(parent, args){
                return _.find(usersData, {id:parent.userId})
            }
        }
    })
})

//RootQuery 
const RootQuery = new GraphQLObjectType({
    name: 'RootQueryType',
    description: 'Description',
    fields: {
        user: {
            type: UserType,
            args: {id: {type: GraphQLID}},

            resolve(parent, args){
                return _.find(usersData, {id: args.id})
                //resolve with data
                //get and return data from a datasource
            }
        },

        users: {
            type: new GraphQLList(UserType),                    //모든 데이터 가져오기 
            resolve(parent,args){
                return usersData;
            }
        },

        hobby: {
            type: HobbyType,
            args: {id: {type: GraphQLID}},

            resolve(parent, args){
                return _.find(hobbiesData, {id: args.id})
                //return data for hobby
            }
        },

        hobbies: {
            type: new GraphQLList(HobbyType),
            resolve(parent,args){
                return hobbiesData;
            }
        },
        
        post: {
            type: PostType,
            args: {id: {type: GraphQLID}},

            resolve(parent,args){
                return _.find(postsData, {id: args.id})
            }
        }
    }
})


//Mutations
const Mutation = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        createUser: {
            type: UserType,
            args: {
                //id: {type: GraphQLID},
                name: {type: GraphQLString},
                age: {type: GraphQLInt},
                profession: {type: GraphQLString}
            },

            resolve(parent, args){
                let user = {
                    name: args.name,
                    age: args.age,
                    profession: args.profession
                    
                }
                return user;
            }
        },

        createPost: {
            type: PostType,
            args: {
                //id: {type: GraphQLID},
                comment: {type:GraphQLString},
                userId: {type:GraphQLID}
            },

            resolve(parent,args){
                let post = {
                    comment: args.comment,
                    userId: args.userId
                }
                return post;
            }
        },

        createHobby: {
            type: HobbyType,
            args: {
                //id: {type: GraphQLID},
                title: {type:GraphQLString},
                description: {type:GraphQLString},
                userId: {type:GraphQLID}
            },

            resolve(parent,args){
                let hobby = {
                    title: args.title,
                    description: args.description,
                    userId: args.userId
                }
                return hobby;
            }
        }
    }
})

module.exports = new GraphQLSchema({
    query: RootQuery,
    mutation: Mutation
})





///////////////////  apollo graphql ///////////////////////

npm install apollo-server graphql
vscode extension  graphql for vscode 설치 

const { ApolloServer, gql } = require("apollo-server")

const typeDefs = gql`

  type Book {
    title: String
    author: String
  }

  type Query {
    books(search: String): [Book]
  }

  type Mutation {
    addBook(title: String!, author: String!): Book
  }
`
const books = [
  {
    title: "The Awakening",
    author: "Kate Chopin",
  },
  {
    title: "City of Glass",
    author: "Paul Auster",
  },
]

const resolvers = {
  Query: {
    books: (_, { search }) =>
      search
        ? books.filter(
            ({ title, author }) =>
              title.includes(search) || author.includes(search)
          )
        : books,
  },
  Mutation: {
    addBook: (_, { title, author }) => {
      const newBook = {
        title,
        author,
      }
      books.push(newBook)
    },
  },
}

const server = new ApolloServer({
  typeDefs,
  resolvers,
  csrfPrevention: true,
  cache: "bounded",
})

server.listen(5000).then(({ url }) => {
  console.log(`🚀  Server ready at ${url}`)
})
