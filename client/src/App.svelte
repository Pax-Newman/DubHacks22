
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">

  <title>W3.CSS Template</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  <style>

  body, html {height: 100%}
  .bgimg {
    min-height: 100%;
    background-position: center;
    background-size: cover;
  }
  </style>

<head>
  
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">

  <title>Home</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

  </head>
  
  {#if homeView }
  <Home></Home>
  {/if}

  {#if !homeView }
<h1>Scan View</h1>
  {/if}
  <title>Home</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">


      <script>
        	import Home from './Home.svelte';

          let homeView = true;
        function isParamEmpty() {
            const queryString = window.location.search;
          
            if (queryString.length == 0){
              homeView = true;
            }else{
              homeView = false;
            }
             
            }
        function toggleView (){
          homeView = !homeView;
        }
    
      </script>
    
  

  

