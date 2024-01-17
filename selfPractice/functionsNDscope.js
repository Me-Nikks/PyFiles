function getReminder(){
    console.log('Water the plants');
    
    }
    
    function greetInSpanish(){
      console.log('Buenas tardes.');
    }
getReminder();
greetInSpanish();

let customer ='Nikhil'
function sayThanks(){
console.log(`Thank you ${customer} for your purchase! We appreciate your business.`)
}
sayThanks();
sayThanks();
sayThanks();
sayThanks();
sayThanks();
sayThanks();
sayThanks();


// parameters and arguments
let name ='';
function sayThanks(name){
console.log('Thank you for your purchase '+ name + '! We appreciate your business.');
}

sayThanks('Cole');

// Default Parameters

function makeShoppingList(item1= 'milk', item2= 'bread', item3='eggs'){
    console.log(`Remember to buy ${item1}`);
    console.log(`Remember to buy ${item2}`);
    console.log(`Remember to buy ${item3}`);
  }
  
  makeShoppingList();

//   Return

function monitorCount (rows,columns){
    return rows * columns;
  
  }
  
  const numOfMonitors = monitorCount(5,4);
  console.log(numOfMonitors);

//   Helper Functions

function multiplyByNineFifths(number) {
    return number * (9/5);
  };
  
  function getFahrenheit(celsius) {
    return multiplyByNineFifths(celsius) + 32;
  };
  
  getFahrenheit(15);

// Example 2
  function monitorCount(rows, columns) {
    return rows * columns;
  };
  
  function costOfMonitors(rows,columns){
    return monitorCount(rows,columns)*200;
     
  };
  
  const totalCost = costOfMonitors(5,4);
  console.log(totalCost);
  
//   Function Expressions, anynomous fun
  const plantNeedsWater = function(day){
    if(day === 'Wednesday'){
      return true;
    }else{
      return false;
    }
  
  };
  
  console.log(plantNeedsWater('Tuesday'));

// arrow fun 
  const plantNeedWater = (day) =>{
    if (day === 'Wednesday') {
     return true;
   } else {
     return false;
   }
 
 }
 
 console.log(plantNeedWater('wednesday'));

 const PlantNeedsWater = day => day === 'Wednesday' ? true :false;
  
 const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];

 const listItem = famousSayings[0];
 console.log(listItem);
 console.log(famousSayings[2]);
 console.log(famousSayings[3]);

 let groceryList = ['bread', 'tomatoes', 'milk'];
groceryList[1]='avocados'

const concept = ['arrays', 'can', 'be', 'mutated'];

function changeArr(arr){
  arr[3] = 'MUTATED';
}

changeArr(concept);
console.log(concept);

function removeElement(newArr){
  newArr.pop();
}
removeElement(concept);
console.log(concept);


  
