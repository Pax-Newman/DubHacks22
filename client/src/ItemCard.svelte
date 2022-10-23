<script>
import { user } from './stores';

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
  ],
  userClaims: [
    0, 1
  ],
  uuid: ""
}

const url = `data/?${itemObj.uuid}`
const body = {
  userName:$user,
  claims:itemObj.userClaims,
  updates:[],
  additions:[],
  removals:[],
}

let clicked = 0

function getPrice(price) {
  return (price / 100).toFixed(2)
}

function patch(data) {
  return fetch(url, {
    method: 'PATCH',
    body: JSON.stringify(data),
  })
}

function claim() {
  let data = body
  itemObj.tags = [...itemObj.tags, $user]
  data.claims = [...data.claims, itemObj.id]
  patch(data)
}

function unclaim() {
  let data = body
  itemObj.tags = itemObj.tags.filter((tag) => tag != $user)
  data.claims = data.claims.filter((id) => id != itemObj.id)
  patch(data)
}
</script>

<div class="box">
  <div class="block">
    <div class="level is-mobile">
      <div class="level-item has-text-centered">
        <p class="title">{itemObj.title}</p>
      </div>
      <div class="level-item has-text-centered">
        <p class="subtitle">{getPrice(itemObj.price)}</p>
      </div>
    </div>
    <div class="level-right is-mobile">
      <!-- check this for correctness -->
      {#if !itemObj.tags.includes($user)}
      <div class="level-item has-text-centered">
        <button class="button is-primary" on:click={claim}>Mine!</button>
      </div>
      {:else}
      <div class="level-item has-text-centered">
        <button class="button is-danger" on:click={unclaim}>Not Mine!</button>
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

