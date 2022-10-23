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

<body on:load={isParamEmpty}>
  {#if homeView }
    <Home/>
  {:else}
    <Scan/>
  {/if}
  <title>Home</title>
</body>

<script>
function isParamEmpty() {
  const queryString = window.location.search;
  console.log(queryString);
  if (queryString.length == 0) {
    homeView = true;
  } else {
    homeView = false;
  }
}

window.addEventListener('load', (event) => {
    isParamEmpty();
});
        	import Home from './Home.svelte';
          import Scan from './Scan.svelte';
          let homeView = true;
       
        function toggleView (){
          homeView = !homeView;
        }
    
</script>
  
{#if homeView }
  <Home/>
{:else if !homeView }
<h1>Scan View</h1>
{/if}
  


  

