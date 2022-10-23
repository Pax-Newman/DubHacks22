<script>

let homeView = true;
let files;

function isParamEmpty() {
  const queryString = window.location.search;
  console.log(queryString);
  if (queryString.length == 0){
    homeView = true;
  } else {
    homeView = false;
  }               
}

window.addEventListener('load', (event) => {
  isParamEmpty();
});
            
function toggleView (){
  homeView = !homeView;
}
</script>
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
 
  
<div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
  <div class="w3-display-topleft w3-padding-large w3-xlarge">
    Logo
  </div>
  <div class="w3-display-middle">
    <h1 class="w3-jumbo w3-animate-top">Welcome, </h1>
      <label for="file-upload">
        <span type="btn" class="button is-primary">Scan a receipt!</span>
        <input
              id="file-upload"
              type="file"
              alt="camera"
              accept="image/*"
              capture="environment"
              style="display: none"
              bind:files
            />
      </label>
      {#if files && files[0]}
        <p>
          {files[0].name}
        </p>
      {/if}
  </div>
  <div class="w3-display-bottomleft w3-padding-large"></div>
</div>