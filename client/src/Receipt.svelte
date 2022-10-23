<script>
  import ItemCard from './ItemCard.svelte';
  let src = 'http://www.example.com/demo-image.jpg';
</script>
<head>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
  <p class = "title">Itemization</p> 
  <button class="button">+Add Item</button>

  <div class="columns">
      <div class = "column is-one-third">
      <img src="https://picsum.photos/300/500" margin = "1em">
      </div>
    <div class="cards">

        <div class = "column is-one fifth">

          <ItemCard></ItemCard>
          <ItemCard></ItemCard>
          <div class = "column is-one-fifth is-offset-10">
           
      </div>
    </div>


    </div>
  </div>
 
</body>

<style>
  
  row{
    align-items: left;
  }
</style>