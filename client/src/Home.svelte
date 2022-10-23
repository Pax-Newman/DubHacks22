<script>
import { createEventDispatcher } from 'svelte'

const dispatch = createEventDispatcher()

let files;

function changeView(newState) {
  dispatch('state-event', {
    state: newState
  })
}
</script>
  
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
  <div class="bgimg w3-display-container w3-animate-opacity w3-text-white">
    <div class="w3-display-topleft w3-padding-large w3-xlarge">
      Logo
    </div>
    <div class="w3-display-middle">
      <h1 class="w3-jumbo w3-animate-top">Welcome, </h1>

      <p class="w3-large w3-center"> <button on:click={toggleView}>
        Scan or Add Receipt
      </button>
      

    </div>


    <div class="w3-display-bottomleft w3-padding-large">

    </div>
  </div>


