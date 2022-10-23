

<script>
  // title, price, tags
  export let itemObj = {
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
        <p class="subtitle">{itemObj.title}</p>
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

<!-- <div class="card has-background-primary " >
  <div class="card-content">
    <div class="row">
    <div class="columns is-mobiile">
 
      <div class="column is-two-thirds">
        <p class="title">Oat Milk</p>
        <p class="subtitle"> Dylan, Pax, Natalie</p>
      </div>
      <div class="column is-5 ">
        <p class="title" > $6.45</p>
     </div>
    </div>
    </div>
  </div>
</div> -->
