 // Data Types:  
 /* /Multiline comment in Javascript
 1. string
 2. Intergers/numbers
 3. booleans
 4. Array

 */
let name = "Jomo";
let height = 50
let input= document.getElementById("inpitField")
function submit(){
 var input =document.getElementById("inputField")
 var input = parseInt(input);
 var input = input +1;
 //console.log(typeog(height))
}
//Boolean data type
let adult = true;
let fruits =['kiwi','pineapple','apple', 30,false]
let person ={
    firstname: 'Ada',
    Secondname: 'lovelace',
    Age: 18,
    Address: {
        country:'sudan',
        City: 'Khartoum',
        street: 'Bani bani',        
    },
    children: ['Kelly' , 'mary']
}
function saveItem(){
    var input =document.getElementById("inputField").Value
    localStorage.setItem("inputField")
    showwiecomeMessage(inputField)
}
function showwiecomeMessage(inputField){
    var input =document.getElementById("show mwssage")
    messageElement.textContent ="we have saved your input as"+ input
}

var storedItem = localStorage.getItem('inputItem')
if(stored){
    showwiecomeMessage(storedItem)
}
console.log(person.Address.country)
console.log(typeof(person))
