<script>
  import ItemCard from './ItemCard.svelte';
  let src = 'http://www.example.com/demo-image.jpg';
</script>

<body>
  <div class="columns">
    <div class = "column is-one-third">
      <img src="https://picsum.photos/400/600">
    </div>
    <div class="rows">
      <div class = "column is-one quarter">
        <ItemCard></ItemCard>
      </div>
    </div>
  </div>
  <ItemCard></ItemCard>
</body>