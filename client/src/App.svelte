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
import Scan from './Preview.svelte';
import { onMount } from 'svelte';
import { state, STATES } from './stores'

// When the component is rendered
onMount(() => {
  // Set state based on url
  // TODO change this so it also checks if the query is valid with the API
  const querying = isParamEmpty();
  if (!querying) {
    $state = STATES.receipt
  } else {
    $state = STATES.home
  }
})

// Check if the query is empty
function isParamEmpty() {
  const queryString = window.location.search;
  console.log(queryString);
  return queryString.length == 0
}
    
</script>

<!-- Load based on state var -->
<body>
  <button on:click={() => {$state = STATES.home}} class="button is-primary">To Home</button>
  <button on:click={() => $state = STATES.preview} class="button is-primary">To Preview</button>
  <button on:click={() => $state = STATES.receipt} class="button is-primary">To Receipt</button>
  <p>{$state}</p>

  {#if state === state }
    <Home/>
  {:else if state === STATES.preview}
    <Scan/>
  {:else if state === STATES.receipt}
    <p>butts</p>
  {/if}
  <title>Home</title>
</body>
  

  


  

