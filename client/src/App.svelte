<head>
  <title>Home</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  
  <style>
    body, html {
      background-color: #9eedf7;;
      height: 100%;
    }
    .bgimg {
      min-height: 100%;
      background-position: center;
      background-size: cover;
    }
 
  </style>
</head>

<script>
import Home from './Home.svelte';
import Preview from './Preview.svelte';
import Receipt from './Receipt.svelte';
import { onMount, onDestroy } from 'svelte';
import { state, STATES } from './stores';
import { fade } from 'svelte/transition';

// When the component is rendered
onMount(() => {
  // Set state based on url
  // TODO change this so it also checks if the query is valid with the API
  const querying = isParamEmpty();
  if (!querying) {
    state.set(STATES.receipt)
  } else {
    state.set(STATES.home)
  }
})

const unsubscribe = state.subscribe(value => {
  console.log(value)
})

onDestroy(() => {
  unsubscribe()
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
  <div class=" w3-padding-large w3-xlarge">
    Receiptly


  <button on:click={() => state.set(STATES.preview)} class="button is-primary">Add and Scan</button>
  <button on:click={() => state.set(STATES.receipt)} class="button is-primary">Receipt</button>
</div>
  {#if $state === STATES.home }
    <Home/>
  {:else if $state === STATES.preview}
  <div class="column is-full is-offset-3" transition:fade>
    <Preview/>
  </div>
  {:else if $state === STATES.receipt}
 <div class="column is-full is-offset-0.5" transition:fade>
  <Receipt/>
</div>
  {/if}

</body>


