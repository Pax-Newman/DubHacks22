<meta name="viewport" content="width=device-width, initial-scale=1">
<script>
  import ItemCard from './ItemCard.svelte';
  import AddItemCard from './AddItemCard.svelte';

</script>



<div class="columns">
  <div class = "column is-one fifth offset-3">
    <h1>Itemization of Receipt</h1>
    <div></div>

</div>
</div>

  <div class="columns">
    <div class = "column is-one-third">
      <img src="https://picsum.photos/300/500" margin = "1em">
    </div>
    <div class = "column is-one fifth">

      <ItemCard></ItemCard>
      <ItemCard></ItemCard>
      <AddItemCard></AddItemCard>
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

.h1{
  text-align: center;
}

.head{
  text-align: center;
}
  
  * {box-sizing: border-box;}
  </style>