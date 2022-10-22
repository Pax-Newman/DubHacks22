<script>
	import Home from './Home.svelte';
</script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">

  <title>W3.CSS Template</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">


<head>
  
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">

  <title>Home</title>
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
  </head>
 
  
  <div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
    <div class="w3-display-topleft w3-padding-large w3-xlarge">
      Logo
    </div>
    <div class="w3-display-middle">
      <h1 class="w3-jumbo w3-animate-top">Welcome, </h1>

      <p class="w3-large w3-center">  <a href="main.html" class="button">Scan Receipt</a></p>
      <script>
        function isParamEmpty() {
            const queryString = window.location.search;
              return queryString.length  == 0;
            }
    
      </script>
    </div>


    <div class="w3-display-bottomleft w3-padding-large">

    </div>
  </div>
  

