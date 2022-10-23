<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
  import ItemCard from './ItemCard.svelte';
</script>



<div class="columns">
  <div class = "column is-one-third">
    <p class = "title">Itemization</p> 
  </div>
  <div class = "column is-one-third">
    <div class = "item"><button class="button">+Add Item</button></div>
  </div>
  </div>  
  <div class="columns">
    <div class = "column is-one-third">
      <img src="https://picsum.photos/300/500" margin = "1em">
    </div>
    <div class = "column is-one fifth">

      <ItemCard></ItemCard>
      <ItemCard></ItemCard>
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
  
  * {box-sizing: border-box;}
  </style>