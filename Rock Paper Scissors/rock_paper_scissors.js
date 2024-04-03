let userscore=0;
let compscore=0;
const choices=document.querySelectorAll(".choice");
const info=document.querySelector("#reason");
const msg=document.querySelector("#msg");
const us=document.querySelector("#userscore");
const cs=document.querySelector("#compscore");


const gencompchoice=()=>{
    let c=['rock','paper','scissors'];
    return c[(Math.floor(Math.random()*3))];
}

const draw=(compchoice)=>{
    info.innerText=`You and the computer made the same choice ${compchoice}`;
    msg.innerText="It's a Draw";
    msg.style.backgroundColor='blue';
    
};

const userwin=(win,userchoice,compchoice)=>{
    console.log(win?msg.innerText="You Win":msg.innerText="You Lose");
    if (win){
        info.innerText=`Your choice: ${userchoice} beats computer's choice: ${compchoice}`;
        msg.style.backgroundColor='green';
        userscore+=1;
        us.innerText=userscore;
        
    } else{
        info.innerText=`Computer's choice: ${compchoice} beats your choice: ${userchoice}`;
        msg.style.backgroundColor='red';
        compscore+=1;
        cs.innerText=compscore; 
    }
};
const playgame=(userchoice)=>{
    const compchoice=gencompchoice();
    console.log("computer:" ,compchoice);
    console.log("user:" ,userchoice);
    if (userchoice===compchoice){
        draw(compchoice);
    } else{
        let win=true;
        if (userchoice==="rock"){
            win=compchoice==="paper"?false:true;
        } else if (userchoice==="paper"){
            win=compchoice==="scissors"?false:true;
        } 
        else{
            win=compchoice==="rock"?false:true;
        }
        userwin(win,userchoice,compchoice);
    }
};

choices.forEach((choice)=>{
    choice.addEventListener("click",()=>{
        const userchoice=choice.getAttribute("id");
        playgame(userchoice);
    });
});