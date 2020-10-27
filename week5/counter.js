 // let counter=0;
          /* function count(){
               const heading = document.querySelector('h1');
               if(heading.innerHTML === 'Hello!'){
               heading.innerHTML = "Goodbye";
              // counter++;
               //alert(counter);
           }else{
               heading.innerHTML = 'Hello!';
           }*/
if(localStorage.getItem('counter')){
    localStorage.setItem('counter',0);
}
let counter=0;
           function count(){
               counter++;
               document.querySelector('h1').innerHTML = counter;
               localStorage.setItem('counter', counter); 
               /*if(counter%10 === 0){
                   alert(`Count is now ${counter}`); //bactag
               }*/
           }
           document.addEventListener('DOMContentLoaded',function(){
            document.querySelector('button').onclick = count; 

            setInterval(count,1000);
           });
            