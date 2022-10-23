<script>
  // title, price, tags
  export let itemObj = {
    id: -1,
    title: 'Oat Milk Beeswax',
    price: 13.75,
    tags: [
      "Dylan",
      "Pax",
      "Natalie",
      "Jonas",
      "Being X",
    ]
  }
</script>

<div class="box">
  <div class="block">
    <div class="level is-mobile">
      <div class="level-item has-text-centered">
        <p class="title">{itemObj.title}</p>
      </div>
      <div class="level-item has-text-centered">
        <p class="subtitle">{itemObj.price}</p>
      </div>
    </div>
    <div class="level-right is-mobile">
      <!-- check this for correctness -->
      {#if !itemObj.tags.includes("Pax")}
      <div class="level-item has-text-centered">
        <button class="button is-primary">Mine!</button>
      </div>
      {:else}
      <div class="level-item has-text-centered">
        <button class="button is-danger">Not Mine!</button>
      </div>
      {/if}
    </div>
  </div>
  <div class="block">
    <div class="columns is-mobile is-multiline is-centered">
      <div class="column is-three-quarters">
        {#each itemObj.tags as tag}
          <div class="tag is-medium">
            <p>{tag}</p>
          </div>
        {/each}
      </div>
    </div>
  </div>
</div>

