//html 코드에 아래 library import 해줘야함.
//<script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
//<script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
//<script src="https://unpkg.com/@babel/standalone/babel.min.js."></script>

//import update 
// <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
// <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
// <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
// <script src="https://unpkg.com/prop-types@15.7.2/prop-types.js"></script>
// <script type="text/babel"></script>


//react-dom은 react로 만든 html 태그들을 html body로 옮겨주는 역할을 함. 

const root = document.getElementById("root");
const span = React.createElement("span", {
    id: "sexy-span"
}, "hello, im honglion"); //인자로 들어가는 span은 실제 html 태그이름을 적어줘야함. 
//가운데는 property 설정할 수 있는 곳임. id, style, onClick 같은 반응형 property도 설정가능, 3번째 인자는, tag의 내용을 적어줌.

ReactDOM.render(span, root); //html body에 id가 root인 태그안에 span태그를 넣어주기.


////////////////////////////////////////////////////////////////////////////////////////////////
const root = document.getElementById("root");
const h3 = React.createElement("h3", null, "hello im honglion"); //인자로 들어가는 span은 실제 html 태그이름을 적어줘야함. 
const btn = React.createElement(
    "button", {
        onClick: () => console.log("im clicked")       //console.dir로 onClick property 확인가능. eventlistner 대체하는 코드.
    },
    "Click me"
)
const container = React.createElement("div", null, [h3, btn])
ReactDOM.render(container, root); //html body에 root 태그안에 span태그를 넣어주기.


////////////////////////////////////////////////////////////////////////////////////////////////

const root = document.getElementById("root");
const Title = ()=>(<h3 id="title"
onMouseEnter = {
    () => console.log("mouse enter")
}>Hello im honglion</h3>);

const Btn = ()=>(<button onClick = {()=>console.log("im clicked")}>Click me</button>);
//중요한점은 Title과 Btn 은 앞글자가 대문자로 이루어져있음. 이는 html에서 이 변수를 활용할때 tag name과 구별하기 위해서임.
//arrow function이지만 ()=>() 이렇게 만들어야하는듯. ()이렇게하면 return한다는 의미 ()=>{} 이걸쓰면 {}안에 return이 있어야함.

const Container = <div><Title /> <Btn /></div>;         //대문자여서 태그와 구별됨.
ReactDOM.render(Container, root); //root 요소안에 Container를 넣어주기.

////////////////////////////////////////////////////////////////////////////////////////////////

const root = document.getElementById("root");
let counter = 0;
function countUp(){
    counter = counter + 1;
    render();           //이코드가 없으면 counter는 늘어나지만 웹페이지상에 리렌더링을 안해주기때문에 계속 0임. 
}

function render() {
    ReactDOM.render(<Container />, root);
}

const Container = ()=>(
    <div>
        <h3>Total Click : {counter}</h3>
        <button onClick={countUp}>Click me</button>
    </div>
);

render();

//react가 좋은 이유는 리렌더링을 할때 바뀐부분만 html에 업데이트해주기 때문임.


///////////////////////////////////////////////////////////////////////////////////////////////////

//리렌더링 코드 생략할 수 있는 방법. useState
const root = document.getElementById("root");
    function App(){
        let [counter, setCounter] = React.useState(0);      //counter는 0이 되고, setCounter는 함수가된다.
                                                            //setCounter(x)를 실행하면 counter의 값을 x로 바꾸고 리렌더링 해준다.
        const onClick = ()=>{
            //setCounter(counter + 1);
            setCounter((current)=>current + 1);             //함수를 전달해주기, counter의 값이 다른곳에서 바뀔수있기때문에 현재값을 로드해서 더해주기.
        };
        return(
            <div>
                <h3>Total clicks: {counter}</h3> 
                <button onClick={onClick}>Click me</button>
            </div>
        );
    }
    ReactDOM.render(<App />, root);

///////////////////////////////////////////////////////////////////////////////////////////////////

//converter 만들기
function MinutesToHours(){
    const [amount, setAmount] = React.useState();
    const [flipped, setFlipped] = React.useState(false);
    const onChange = (event)=>{
            setAmount(event.target.value);
    }
    const reset = ()=>{
        setAmount(0);
    }
    const onFlip = ()=>{
        reset();
        //setFliped(!flipped)
        setFlipped((current)=>!current);
    }
    return(
        <div>
            <div>
                <label htmlFor="minutes">Minutes</label>
                <input 
                    value={flipped ? amount*60 : amount}
                    id="minutes"
                    placeholder="Minutes" 
                    type="number"
                    onChange={onChange} 
                    disabled={flipped === true} />
            </div>

            <div>
                <label htmlFor="hours">Hours</label>
                <input
                    value={flipped ? amount : Math.round(amount/60)}
                    id="hours" 
                    placeholder="Hours" 
                    type="number"
                    onChange={onChange} 
                    disabled= {flipped === false} />
            </div>
            <button onClick={reset}>Reset</button>
            <button onClick={onFlip}>Flip</button>
        </div>
    );
}

function KmToMiles(){

}

function App(){
    const [index, setIndex] = React.useState("0");
    const onSelect = (event)=>{
        setIndex(event.target.value);
    }

    return(
        <div>
            <h1 className="hi">Super Converter</h1>
            <select value={index} onChange={onSelect}>
                <option value="0">Minutes & Hours</option>
                <option value="1">Km & Miles</option>
            </select>
            <hr />
            {index === "0" ? <MinutesToHours /> : null}
            {index === "1" ? <KmToMiles /> : null}
        </div>
    );
}
ReactDOM.render(<App />, root);

//htmlFor, className은 jsx언어에서 html의 for와 class 언어랑 겹치기때문에 다르게 이름을 만들어준것임. 
//disabled는 input 입력창 비활성화

///////////////////////////////////////////////////////////////////////////////////////////////////
//부모컴포넌트 App에서 자식컴포넌트 Btn으로 prop 넘겨주기 

function Btn(props){
    return (
        <button
            style={{
                backgroundColor: "tomato",
                color: "white",
                padding: "10px 20px",
                border: 0,
                borderRadius: 10,
                fontSize: props.big? 18 : 15,
            }}>
            {props.banana}
        </button>
    )
}

//JSX 에서도 style을 설정할 수 있는데 object형식으로 넘겨줘야함. css의 형식이랑 다름.
//여기서 props는 {banana: "Save change"}, {banana: "Continue"} 이렇게 object로 온다.
//그래서 Btn(props)를 Btn({banana, big})로 바꾸고, {props.banana}를 {banana} 이렇게 바꿀 수 있음.

function App(){
    return(
        <div>
            <Btn banana="Save change" big={true}/>
            <Btn banana="Continue" big={false}/>
        </div>
    );
}
ReactDOM.render(<App />, root);

///////////////////////////////////////////////////////////////////////////////////////////////////
function Btn({text, changeValue}){
    return (
        <button
            onClick={changeValue}
            style={{
                backgroundColor: "tomato",
                color: "white",
                padding: "10px 20px",
                border: 0,
                borderRadius: 10,
            }}>
            {text}
        </button>
    )
}

const MemorizedBtn = React.memo(Btn);

function App(){
    const [value, setValue] = React.useState("Save Chnages");
    const changeValue = ()=>{setValue("Revert Changes")};
    return(
        <div>
            <MemorizedBtn text={value} changeValue={changeValue}/>
            <MemorizedBtn text="Continue" />
        </div>
    );
}
ReactDOM.render(<App />, root);

//props로 함수도 넘길수 있다. 즉 object 자체를 넘겨주는 것이기때문에 object안에 함수가 있던 변수가 있던 상관없다.
//React.memo를 쓰는 이유는 Continue 버튼은 state변화가 없어서 원래는 갱신되면 안되는데
//App 컴포넌트 특성상. 한 State가 바뀌면 return부분을 전체 리렌더링 하기때문에 continue 버튼도 리렌더링한다.
//이를 막기위해 memo를 쓰고, continue버튼의 state가 바뀌지 않는 이상 리렌더링 하지 않는다. 
// 이는 나중에 웹이 커졌을때 최적화에 중요한 부분이다. 

///////////////////////////////////////////////////////////////////////////////////////////////////
//propTypes
//property들의 type이 잘못전달되는 것을 막기 위해 에러메세지를 띄워주는 역할. 
//terminal에서는 작업위치에 npm i prop-types 설치. node_module 생김.

function Btn({text, changeValue, fontSize = 16}){           //default값을 주는 것도 가능.
    return (
        <button
            onClick={changeValue}
            style={{
                backgroundColor: "tomato",
                color: "white",
                padding: "10px 20px",
                border: 0,
                borderRadius: 10,
                fontSize,
            }}>
            {text}
        </button>
    )
}

const MemorizedBtn = React.memo(Btn);
MemorizedBtn.propTypes = {
    text: PropTypes.string,
    fontSize: PropTypes.number.isRequired,              //isRequired는 MemorizedBtn에 fontSize prop이 꼭 있어야한다는 뜻.
}

function App(){
    const [value, setValue] = React.useState("Save Chnages");
    const changeValue = ()=>{setValue("Revert Changes")};
    return(
        <div>
            <MemorizedBtn text={value} changeValue={changeValue} fontSize={18}/>
            <MemorizedBtn text="Continue" />
        </div>
    );
}
ReactDOM.render(<App />, root);















///////////////////////////////////////////////////////////////////////////////////////////////////
//CRA 

//nodejs 설치 
//작업할 위치에 가서 npx creat-react-app 작업폴더이름.
///////////////////////////////////////////////////////////////////////////////////////////////////
//Css module 사용하기 

//Button.module.css //module.css로 파일 저장해야함.
.btn {
    color: white;
    background-color: tomato;
}

//Button.js
import PropTypes from "prop-types";
import styles from "./Button.module.css";   //import

function Button({text}){
    return (
    <button className={styles.btn}>{text}</button>
    );
}

Button.propTypes = {
    text: PropTypes.string, 
}

export default Button;

//styles.btn 에서 btn은 css 파일의 .btn 부분이다.
//이렇게하면 실제 html element에서는 react가 button의 class name을 랜덤으로 생성해 낸다. 
//Button.module.css에 버튼의 여러가지 버전의 스타일을 저장해놓으면, 그때그때 다른 스타일의 버튼을 설정해줄수 있음.
//module화 하는 이유는 css파일 하나에 수많은 tag들의 스타일을 저장해놓으면 관리가 힘들기 때문임.

///////////////////////////////////////////////////////////////////////////////////////////////////

// useEffect 사용하기 
//App.js
import Button from "./Button";
import styles from "./App.module.css"
import { useState, useEffect } from "react";

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] =useState("");
  const onClick = ()=>setValue((prev)=>prev +1);

  console.log("i run all the time");
  
  useEffect(()=>{
    console.log("Call the api...");
  }, []);
  //처음에만 실행되고, 그 후로 실행안됨.

  useEffect(()=>{
    console.log("when counter changes")
  },[counter])

  useEffect(()=>{
    if (keyword !== "" && keyword.length > 5){
      console.log("Search for", keyword);
    }
  }, [keyword])
//keyword값이 변하면 실행됨.

  useEffect(()=>{
    console.log("when keyword and counter changes")
  },[keyword, counter])
// keyword나 counter 둘중에 하나가 바뀌면 실행됨


  const onChange = (event) =>{
    setKeyword(event.target.value);
  }

  return (
    <div>
      <input
        value={keyword} 
        onChange={onChange}
        type="text"
        placeholder="search here..." />
      <h1 className={styles.title}>Hello! counter : {counter}</h1>
      <Button text="btn" />
      <button onClick={onClick}>Click me!</button>
    </div>
  );
}

export default App;

///////////////////////////////////////////////////////////////////////////////////////////////////
//Clean up function  컴포넌트가 사라질때 실행되는 코드.
import { useEffect, useState } from "react";
import Button from "./Button";

function Hello(){

    // function byeFn(){
    //     console.log("Bye");
    // }

    // function hiFn(){
    //     console.log("Hi");
    //     return byeFn;
    // }

    // useEffect(hiFn,[]);

    useEffect(()=>{
        console.log("Hi");
        return ()=>console.log("Bye");
    },[]);
    //보통 useEffect 함수안에 다 넣는 경향이 있음.
    //중요한건 return (함수) 이여야함. 


    return <h1>Hello!</h1>;
}


function App(){
    const [showing, setShowing] = useState(false);

    const onClick = ()=>{
        setShowing((prev)=>!prev);
    }

    return(
        <div>
            {showing ? <Hello /> : null}
            <Button 
                text={showing ? "Hide":"Show"}
                onClick= {onClick} />
        </div>
    )
    //이때 Hello 컴포넌트가 다시 생길때마다 useEffect() 도 계속 실행된다는 것임.
}

export default App;

///////////////////////////////////////////////////////////////////////////////////////////////////
//To Do List , map 응용 
import { useState } from "react";


function App(){
    const [toDo, setToDo] =useState("");
    const [toDos, setToDos] =useState([]);

    const onChange = (event)=>{
        setToDo(event.target.value);
    }

    const onSubmit = (event)=>{
        event.preventDefault();
        if (toDo === ""){
            return;
        }

        setToDos((currentArray)=>[...currentArray, toDo]);  
        // ...currentArray는 안에 요소를 풀어서 리스트에 넣어줌. 그냥 currentArray 하면 리스트안에 리스트가 들어간채로 데이터만들어짐.

        setToDo("");
    }

    console.log(toDos);

    return(
        <div>
            <h1>To Do List ({toDos.length})</h1>
            <form onSubmit={onSubmit}>
                <input onChange={onChange} value={toDo} type="text" placeholder="write your to do..." />
                <button>Add To Do</button>
            </form>
            <hr />
            <ul>
            {toDos.map((item, index)=><li key={index}>{item}</li>)}
            </ul>
        </div>
        //jsx에서 리스트변수를 집어넣으면 리스트에 있는 요소들을 나열해서 html에 띄워줌.
        //이를 이용해서 map을 활용해서 리스트안에 요소를 <li> 태그로 만들어내면, 그대로 html의 태그로 적용됨. 
        //map 사용할때 index 요소를 <li> 태그의 key로 넣어줘야지 warning이 안뜸. 
    )
}


export default App;

///////////////////////////////////////////////////////////////////////////////////////////////////
//async 

useEffect(()=>{
    fetch(`https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`)
    .then((response)=>response.json())
    .then((json)=>{
        setMovies(json.data.movies);
        setLoading(false);
    });
},[]);

//위에 코드와 동일하게 작동하는 async 코드 
const getMovies = async () => {
    const response = await fetch(`https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`);
    const json = await response.json();
    setMovies(json.data.movies);
    setLoading(false);
}

useEffect(()=>{
    getMovies();
},[]);

///////////////////////////////////////////////////////////////////////////////////////////////////
//react router 
//npm install react-router-dom 

//App.js
import {
    BrowserRouter as Router,                //BrowserRouter, hashrouter가 있는데 브라우저 라우터는 url에 /movie 이런식으로 덧붙여서 이동하는것.
    Routes,
    Route,
} from "react-router-dom";
import Home from './routes/Home';           //page들 import
import Detail from './routes/Detail';       //page

function App(){
    return <Router>
        <Routes>
            <Route path="/movie/:id" element={<Detail />} />        
            <Route path="/" element={<Home />} />
        </Routes>
    </Router>;
}
//Router로 각 route들 (page) 경로설정해놓는다.
// /:id  를 통해 id를 이용한 url를 만들 수 있다. 
export default App;

//Router의 Link 는 하이퍼링크를 통해 다른 페이지로 갈때 새로고침을 하지않고 넘겨줌.

///////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
