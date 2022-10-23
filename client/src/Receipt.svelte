<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
import ItemCard from './ItemCard.svelte';
import Form from './Form.svelte';
import AddItemCard from './AddItemCard.svelte';
import { onMount } from 'svelte';
import { user } from './stores';

let receipt = {
  title: "Minco",
  UUID: 123890281321,
  lines: [
    {
      lineID:0,
      itemName:"Oat Milk Beeswax",
      price: 1200
    },
    {
      lineID:1,
      itemName:"Goat Flower Mix",
      price: 1576
    },
  ],
  tax: 120,
  users: [
    {
      userName: "Pax",
      claims: [0],
      totalPrice: 1320,
      image: "",
    },
  ],
}

function setReceipt(query) {
  const url = `data/${query.slice(1)}`
  
  fetch(url)
    .then((response) => response.json())
    .then((data) => receipt = data)
}

onMount(() => {
  const queryString = window.location.search;
  setReceipt(queryString)
})

$: ourUser = $user

function toItem(receipt, lineID) {

  const queryString = window.location.search;
  let line = receipt.lines.find(line => line.lineID == lineID)
  
  let userData = receipt.users.find((user) => user.userName == ourUser)

  if (userData == undefined) {
    userData = {
      userName: "",
      claims: [],
      totalPrice: 0,
      image: "",
    }
  }

  return {
    uuid: queryString.slice(1),
    userClaims: userData.claims,
    id: line.lineID,
    price: line.price,
    title: line.itemName,
    tags: receipt.users.filter(
      (user) => user.claims.includes(line.lineID)
      ).map(
        (user) => user.userName
      )
  }
}


</script>

<div class="columns">
  <div class = "column is-one fifth">
    <Form/>
  </div>
</div>

<div class="columns">
  <div class = "column is-one fifth offset-3">
    <h1>Itemization of Receipt</h1>


</div>
</div>

  <div class="columns">
    <div class = "column is-one-third">
      <img src="https://picsum.photos/300/500" margin = "1em">
    </div>
    <div class = "column is-one fifth">
      {#each receipt.lines as line}
        <ItemCard itemObj={toItem(receipt, line.lineID)}/>
      {/each}      
      <AddItemCard/>
    </div>
  </div>
  <style>
    
.header {  
  padding: 10px;
  display: flex;
  justify-content: start;
  align-items:  left;
}

.item {
  padding: 10px;
  border: 2px solid rgba(111,41,97,.5);

}

.h1{
  text-align: center;
}

.head{
  text-align: center;
}
  
  * {box-sizing: border-box;}
  </style>