<head>
  <title>Home</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  
  <style>
    body, html {height: 100%}
    .bgimg {
      min-height: 100%;
      background-position: center;
      background-size: cover;
    }
  </style>
</head>

<script>
import Home from './Home.svelte';
import Scan from './Scan.svelte';
import ItemCard from './ItemCard.svelte';
import { onMount } from 'svelte';

const STATES = {
  home:1,
  preview:2,
  receipt:3,
}

let state = STATES.home

// Vars
let homeView = true;

// When the component is rendered
onMount(() => {
  isParamEmpty();
})

function isParamEmpty() {
  const queryString = window.location.search;
  console.log(queryString);
  if (queryString.length == 0) {
    homeView = true;
  } else {
    homeView = false;
  }
}

function toggleView (){
  homeView = !homeView;
}
    
</script>

<!-- Load based on  -->
<body>
  
  {#if state === STATES.home }
    <Home/>
  {:else if state === STATES.preview}
    <Scan/>
  {:else if state === STATES.receipt}
    <p>beeps</p>
  {/if}
  </body>
  <title>Home</title>

  

  


  

