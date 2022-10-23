<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
  import ItemCard from './ItemCard.svelte';
</script>

<body>
  <p class = "title">Itemization</p> 
  <button class="button">+Add Item</button>
  <div class="columns">
    <div class = "column is-one-third">
      <img src="https://picsum.photos/300/500" margin = "1em">
    </div>
    <div class = "column is-one fifth">

      <ItemCard></ItemCard>
      <ItemCard></ItemCard>
      </div>
</div>
</body>
  <style>
  
  </style>