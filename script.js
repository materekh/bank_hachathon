let loggedin=document.getElementById("loggedin");
let loggedout=document.getElementById("loggedout");
let btn=document.getElementById("submit");
let btn2=document.getElementById("deposit");
let btn3=document.getElementById("withdraw");
let main=document.getElementById("main");
let logout=document.getElementById("log");
let baldis=document.getElementById("bal");
let tran=document.getElementById("tran");
let namedis=document.getElementById("namediss");
let accounts=[]
let ind=0
loggedin.remove()
btn.addEventListener("click",() => {
    if(form.elements.name.value!='' && form.elements.pass.value!='' && form.elements.email.value!=''){
        ind=accounts.length;
        let flag=false;
        for(let i=0;i<=accounts.length-1;i++){
            if(accounts[i][0]==form.elements.name.value){
                ind=i;
                flag=true;
                break;
            }
        }
        namedis.textContent=form.elements.name.value+"("+ind+")";
        if(!flag) accounts.push([form.elements.name.value,0]);
        // document.write(accounts)
        loggedout.remove();
        main.appendChild(loggedin);
        baldis.textContent=accounts[ind][1]; 
    }
});
btn2.addEventListener("click",() => {
    accounts[ind][1]+=Number(form2.elements.amt.value);
    baldis.textContent=accounts[ind][1]; 
});
btn3.addEventListener("click",() => {
    if(accounts[ind][1]<Number(form2.elements.amt.value)){
        alert("insufficient funds")
    }
    else{
        accounts[ind][1]-=Number(form2.elements.amt.value);
        baldis.textContent=accounts[ind][1]; 
    }
});
logout.addEventListener("click",() => {
    namedis.textContent="Not sighed in";
    loggedin.remove();
    main.appendChild(loggedout);
});
tran.addEventListener("click",()=>{
    if(accounts[ind][1]<Number(form2.elements.trrr.value)){
        alert("insufficient funds")
    }
    else{
        let id = Number(form2.elements.man.value)
        accounts[id][1]+=Number(form2.elements.trrr.value)
        accounts[ind][1]-=Number(form2.elements.trrr.value)
        baldis.textContent=accounts[ind][1]; 
    }
})