<script>
import { createEventDispatcher } from 'svelte'
import { state, STATES } from './stores';

const dispatch = createEventDispatcher()

let files;

function changeView(newState) {
  dispatch('state-event', {
    state: newState
  })
}
</script>

<style>

</style>


  
<div class="bgimg w3-display-container w3-animate-opacity">

  <div class="w3-display-middle">

    

    <div class="columns">
     
      <img src="public/images/receipt-man-nooutline.svg">
      <div class="column is-half">
        <h1 class="w3-jumbo w3-animate-top">Welcome!</h1>
        <button on:click={() => state.set(STATES.preview)} class="button is-primary is-large">Scan a receipt!</button>
      </div>
       
    </div>
  </div>


      
 

      {#if files && files[0]}
        <p>
          {files[0].name}
        </p>
      {/if}
  </div>



